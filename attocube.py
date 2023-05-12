from pylablib.devices import Attocube
from PySide6.QtCore import QObject, Signal, Slot
from qcodes.instrument_drivers.stanford_research.SR860 import SR860
import time


class Controller(QObject):
    # Define signals
    AxisStatusChanged = Signal(list)
    CapMeasured = Signal(int, float)
    CapMeasuredAll = Signal(list)
    ParaSync = Signal(list, list)
    data_signal = Signal(float, int, int)
    MoveFinished = Signal()
    ScanFinished = Signal()

    def __init__(self, attocube_addr='COM5', sr860_addr='USB0::0xB506::0x2000::003476::INSTR'):
        super().__init__()
        self.ramp_flag = True
        self.scan_flag = True

        # Preparation
        try:
            self.atto = Attocube.ANC300(attocube_addr)
            self.atto_flag = True
        except:
            self.atto_flag = False
            print("Cannot connect ANC300")

        try:
            self.sr860 = SR860('SR860', sr860_addr)
            self.sr860_flag = True
        except:
            self.sr860_flag = False
            print("Cannot connect SR860")

    def enable(self, axis, flag):
        if 0 < axis < 7:
            if flag:
                if 7 > axis > 3:
                    self.atto.set_mode(axis, 'stp')
                elif 4 > axis > 0:
                    self.atto.set_mode(axis, 'off')
            else:
                self.atto.disable_axis(axis)
        else:
            self.atto.disable_axis()
        self.AxisStatusChanged.emit([i for i in self.atto.is_enabled().values()])

    def measure_cap(self, axis):
        if 7 > axis > 0:
            self.atto.measure_capacitance(axis)
            try:
                cap = self.atto.get_capacitance(axis)
                self.CapMeasured.emit(cap)
            except:
                print('axis ' + str(axis) + ' capacitance is not available')
        else:
            self.atto.measure_capacitance(all)
            try:
                cap = self.atto.get_capacitance(axis)
                self.CapMeasuredAll.emit([i for i in cap.values()])
            except:
                print('one of the axis capacitance is not available')

    def sync_info(self):
        self.AxisStatusChanged.emit([i for i in self.atto.is_enabled().values()])
        # self.CapMeasured.emit([i for i in self.atto.get_capacitance()])
        freq_list = [i for i in self.atto.get_frequency().values()]
        amp_list = [i for i in self.atto.get_voltage().values()]
        self.ParaSync.emit(freq_list[3:], amp_list[3:])

    # def ramp(self, ax, stop, step, delay):
    #     if self.atto.get_mode(ax) == 'off':             # Check if the axis is in offset mode, abort if not
    #         self.ramp_1d(ax, stop, step, delay, False)
    #         current = self.atto.get_output(ax)  # Check output
    #         return current
    #     else:
    #         print('ramp aborted because of axis disabled')
    #         return 0.0
    #
    # def ramp_stoppable(self, ax, stop, step, delay):
    #     if self.atto.get_mode(ax) == 'off':             # Check if the axis is in offset mode, abort if not
    #         self.ramp_flag = False
    #         self.ramp_1d(ax, stop, step, delay, True)
    #         current = self.atto.get_output(ax)          # Check output
    #         self.ramp_flag = True
    #         return current
    #     else:
    #         print('ramp aborted because of axis disabled')
    #         return 0.0

    def ramp_1d(self, ax, stop, step, delay, stoppable):
        current = self.atto.get_output(ax)  # Get current output
        direction = current > stop
        if direction:
            step = -step
        # start = time.time()
        while (current < stop) ^ direction:  # Ramp loop
            self.atto.set_offset(ax, current)
            current += step
            time.sleep(delay)
            # print('done' + str(time.time() - start))
            start = time.time()
            if self.ramp_flag and stoppable:
                break
        if not self.ramp_flag and stoppable:
            self.atto.set_offset(ax, stop)  # Make sure it at stop voltage

    def move_to(self, x, y, speed):
        step = 1
        delay = step / speed
        # Check if the axis is in offset mode, abort if not
        if (self.atto.get_mode(1) == 'off') and (self.atto.get_mode(2) == 'off'):
            self.ramp_flag = False
            # Move X
            self.ramp_1d(1, x, step, delay, True)
            # Move Y
            if not self.ramp_flag:
                self.ramp_1d(2, y, step, delay, True)
            self.ramp_flag = True
        else:
            print('move aborted because of axis disabled')
        self.MoveFinished.emit()

    def scan(self, center, scan_size, pixel_num, delays, move_speed, end, scan_dir):
        # Configure scan parameters
        x_center, y_center = center
        read_delay, line_delay = delays
        step_size = scan_size / (pixel_num - 1)

        # Configure moving parameters
        move_step = 1
        move_delay = move_step / move_speed

        # Configure starting and ending positions
        # scan_dir, angle
        x_start, y_start = x_center - (scan_size / 2), y_center - (scan_size / 2)
        x_end, y_end = end
        # fast_step, slow_step =

        # Check if scan doable
        start_flag1 = (self.atto.get_mode(1) == 'off') and (self.atto.get_mode(2) == 'off')
        start_flag2 = (scan_size / 2) < x_center < (150 - (scan_size / 2)) and (scan_size / 2) < y_center < (150 - (scan_size / 2))
        start_flag = start_flag1 and start_flag2

        # Check if the axis is in offset mode, abort if not
        if start_flag:
            self.scan_flag = False
            self.ramp_flag = False

            # Move to starting point
            if not self.scan_flag:
                self.ramp_1d(1, x_start, move_step, move_delay, True)  # need to figure out X and Y axis !!!
            if not self.scan_flag:
                self.ramp_1d(2, y_start, move_step, move_delay, True)
            time.sleep(0.2)

            # Scan
            for i in range(pixel_num):
                self.atto.set_offset(2, (step_size * i) + y_start)
                time.sleep(line_delay / 1000)
                for j in range(pixel_num):
                    self.atto.set_offset(1, (step_size * j) + x_start)
                    time.sleep(read_delay / 1000)
                    self.data_signal.emit(self.sr860.X(), i, j)
                    if self.scan_flag:
                        break
                if self.scan_flag or (i == (pixel_num - 1)):
                    break
                self.ramp_1d(1, x_start, move_step, move_delay, True)  # Ramp back to starting point

            # Move to ending point
            if not self.scan_flag:
                self.ramp_1d(1, x_end, move_step, move_delay, True)
            if not self.scan_flag:
                self.ramp_1d(2, y_end, move_step, move_delay, True)

            self.scan_flag = True
            self.ramp_flag = True
        else:
            if start_flag1:
                print('scan aborted because of axis disabled')
            elif start_flag2:
                print('out of scan range')
            else:
                print('you may have bugs')
        self.ScanFinished.emit()

    def close(self):
        if self.atto_flag:
            self.atto.close()
