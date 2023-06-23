# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import Slot, Signal, QThread, QObject
from PySide6.QtGui import *
import pyqtgraph as pg
import sys
import numpy as np
import time

# from testui import Ui_Form
# class controller(QObject):
#     def __init__(self):
#         super().__init__()
#     def closeEvent(self):
#         print("controller destroyed")
# class AttocubeScanning(QMainWindow, Ui_Form):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.pushButton.clicked.connect(self.print_hi)
#         self.pushButton_2.clicked.connect(self.plot_random)
#         self.graphicsView.show()
#         # self.graphicsView.view.setRange(xRange=(-100, 300), yRange=(-100, 300))
#     @Slot()
#     def print_hi(self):
#         # Use a breakpoint in the code line below to debug your script.
#         print(self.graphicsView.imageItem.pixelSize())  # Press Ctrl+F8 to toggle the breakpoint.
#     @Slot()
#     def plot_random(self):
#         data = np.random.rand(100, 100)
#         self.graphicsView.setImage(data)
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = AttocubeScanning()
#     window.show()  # IMPORTANT!!!!! Windows are hidden by default.
#     app.exec()

from scan_UI import Ui_Scan_UI
from Setup import Setup
from attocube import Controller


class AttocubeScanning(QWidget, Ui_Scan_UI):
    # Signals
    Enable_signal = Signal(int, bool)
    MeasureCap_signal = Signal(int)
    FrequencyChanging_signal = Signal(int, int)
    AmplitudeChanging_signal = Signal(int, int)
    Stepping_signal = Signal(int, int)
    MoveTo_signal = Signal(float, float, float)
    StartScan_signal = Signal(list, float, int, list, float, list,
                              int)  # (center step_size, pixel_num, delays, move_speed, end, scan_dir)
    ControlClose_signal = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup = Setup()
        self.thread = QThread()
        self.control = Controller(attocube_addr='COM4', sr860_addr='GPIB0::1::INSTR')
        self.control.moveToThread(self.thread)

        # Variables
        self.data = np.array([[]])
        self.darkest = 0

        # Connect signal
        # Enable signal
        self.setup.X_coarse_status_button.clicked.connect(lambda: self.enable_axis(4))
        self.setup.Y_coarse_status_button.clicked.connect(lambda: self.enable_axis(5))
        self.setup.Z_coarse_status_button.clicked.connect(lambda: self.enable_axis(6))
        self.setup.X_scan_status_button.clicked.connect(lambda: self.enable_axis(1))
        self.setup.Y_scan_status_button.clicked.connect(lambda: self.enable_axis(2))
        self.setup.Z_scan_status_button.clicked.connect(lambda: self.enable_axis(3))
        self.setup.gnd_all_button.clicked.connect(lambda: self.enable_axis(7))

        # Capacitance measurement signal
        self.setup.X_coarse_cap_button.clicked.connect(lambda: self.measure_cap(4))
        self.setup.Y_coarse_cap_button.clicked.connect(lambda: self.measure_cap(5))
        self.setup.Z_coarse_cap_button.clicked.connect(lambda: self.measure_cap(6))
        self.setup.X_scan_cap_button.clicked.connect(lambda: self.measure_cap(1))
        self.setup.Y_scan_cap_button.clicked.connect(lambda: self.measure_cap(2))
        self.setup.Z_scan_cap_button.clicked.connect(lambda: self.measure_cap(3))
        self.setup.all_cap_button.clicked.connect(lambda: self.measure_cap(7))

        # Parameters signal
        self.setup.X_frequency_spinbox.editingFinished.connect(lambda: self.change_frequency(4))
        self.setup.Y_frequency_spinbox.editingFinished.connect(lambda: self.change_frequency(5))
        self.setup.Z_frequency_spinbox.editingFinished.connect(lambda: self.change_frequency(6))
        self.setup.X_amplitude_spinbox.editingFinished.connect(lambda: self.change_amplitude(4))
        self.setup.Y_amplitude_spinbox.editingFinished.connect(lambda: self.change_amplitude(5))
        self.setup.Z_amplitude_spinbox.editingFinished.connect(lambda: self.change_amplitude(6))

        # Step
        self.setup.X_up_button.clicked.connect(lambda: self.step(4, True))
        self.setup.Y_up_button.clicked.connect(lambda: self.step(5, True))
        self.setup.Z_up_button.clicked.connect(lambda: self.step(6, True))
        self.setup.X_down_button.clicked.connect(lambda: self.step(4, False))
        self.setup.Y_down_button.clicked.connect(lambda: self.step(5, False))
        self.setup.Z_down_button.clicked.connect(lambda: self.step(6, False))

        # Sync
        self.setup.sync_button.clicked.connect(self.control.sync_info)

        # Scan
        self.start_move_button.clicked.connect(self.move_to)
        self.start_scan_button.clicked.connect(self.scan)
        self.setup_button.clicked.connect(self.setup.show)

        # Control
        self.Enable_signal.connect(self.control.enable)
        self.MeasureCap_signal.connect(self.control.measure_cap)
        self.FrequencyChanging_signal.connect(self.control.atto.set_frequency)
        self.AmplitudeChanging_signal.connect(self.control.atto.set_voltage)
        self.Stepping_signal.connect(self.control.atto.move_by)
        self.MoveTo_signal.connect(self.control.move_to)
        self.StartScan_signal.connect(self.control.scan)
        self.ControlClose_signal.connect(self.control.close)

        # Update
        self.control.AxisStatusChanged.connect(self.status_update)
        self.control.CapMeasured.connect(self.cap_update)
        self.control.CapMeasuredAll.connect(self.cap_update_all)
        self.control.ParaSync.connect(self.para_update)
        self.control.data_signal.connect(self.data_update)
        self.control.MoveFinished.connect(lambda: self.start_move_button.setText('Move to'))
        self.control.ScanFinished.connect(lambda: self.start_scan_button.setText('Start'))

        # Start preparation
        self.setup.show()
        self.thread.start()

    # Emitting operation slots
    def enable_axis(self, axis=7):
        button_list = [self.setup.X_scan_status_button, self.setup.Y_scan_status_button,
                       self.setup.Z_scan_status_button, self.setup.X_coarse_status_button,
                       self.setup.Y_coarse_status_button, self.setup.Z_coarse_status_button]
        if axis < 7:
            button = button_list[axis - 1]
            if button.text() == 'Enable':
                enable = True
            else:
                enable = False
            self.Enable_signal.emit(axis, enable)
        else:
            self.Enable_signal.emit(axis, False)

    def status_update(self, status):
        button_list = [self.setup.X_scan_status_button, self.setup.Y_scan_status_button,
                       self.setup.Z_scan_status_button, self.setup.X_coarse_status_button,
                       self.setup.Y_coarse_status_button, self.setup.Z_coarse_status_button]
        for i, button in enumerate(button_list):
            button.setText('Disable' if status[i] else 'Enable')

    def measure_cap(self, axis=7):
        self.MeasureCap_signal.emit(axis)

    def cap_update(self, axis, cap):
        text_list = ['X: ', 'Y: ', 'Z: ', 'X: ', 'Y: ', 'Z: ']
        label_list = [self.setup.X_scan_cap_label, self.setup.Y_scan_cap_label,
                      self.setup.Z_scan_cap_label, self.setup.X_coarse_cap_label,
                      self.setup.Y_coarse_cap_label, self.setup.Z_coarse_cap_label]
        label_list[axis-1].setText(text_list[axis-1] + str(int(cap*10e8)) + 'nF')

    def cap_update_all(self, cap_list):
        text_list = ['X: ', 'Y: ', 'Z: ', 'X: ', 'Y: ', 'Z: ']
        label_list = [self.setup.X_scan_cap_label, self.setup.Y_scan_cap_label,
                      self.setup.Z_scan_cap_label, self.setup.X_coarse_cap_label,
                      self.setup.Y_coarse_cap_label, self.setup.Z_coarse_cap_label]
        for i, cap in enumerate(cap_list):
            label_list[i].setText(text_list[i] + str(int(cap*10e8))  + 'nF')

    def change_frequency(self, axis):
        spinbox_list = [self.setup.X_frequency_spinbox, self.setup.Y_frequency_spinbox,
                        self.setup.Z_frequency_spinbox]
        spinbox = spinbox_list[axis - 4]
        self.FrequencyChanging_signal.emit(axis, spinbox.value())

    def change_amplitude(self, axis):
        spinbox_list = [self.setup.X_amplitude_spinbox, self.setup.Y_amplitude_spinbox,
                        self.setup.Z_amplitude_spinbox]
        spinbox = spinbox_list[axis - 4]
        self.AmplitudeChanging_signal.emit(axis, spinbox.value())

    def step(self, axis, direction=True):
        spinbox_list = [self.setup.X_stp_spinbox, self.setup.Y_stp_spinbox,
                        self.setup.Z_stp_spinbox]
        step_num = spinbox_list[axis - 4].value()
        if not direction:
            step_num = -step_num
        self.Stepping_signal.emit(axis, step_num)

    def scan(self):
        if self.start_scan_button.text() == 'Start':
            center = [self.Xcenter_scan_spinbox.value(), self.Ycenter_scan_spinbox.value()]
            pixel_num = self.pixelnum_scan_spinbox.value()
            scan_size = self.range_scan_spinbox.value()
            move_speed = self.speed_move_spinbox.value()
            delays = [self.readdelay_scan_spinbox.value(), self.linedelay_scan_spinbox.value()]
            self.data = np.zeros((pixel_num, pixel_num))
            # (center step_size, pixel_num, delays, move_speed, end, scan_dir)
            self.StartScan_signal.emit(center, scan_size, pixel_num, delays, move_speed, [0, 0], 0)
            self.start_scan_button.setText('Stop')
        else:
            self.control.scan_flag = True
            self.control.ramp_flag = True
            self.start_scan_button.setText('Start')

    def move_to(self):
        if self.start_move_button.text() == 'Move to':
            x, y = self.X_move_spinbox.value(), self.Y_move_spinbox.value()
            speed = self.speed_move_spinbox.value()
            self.MoveTo_signal.emit(x, y, speed)
            self.start_move_button.setText('Stop')
        else:
            self.control.ramp_flag = True
            self.start_move_button.setText('Move to')

    # Updating UI slot
    def para_update(self, frequency_list, amplitude_list):
        frequency_spinbox_list = [self.setup.X_frequency_spinbox, self.setup.Y_frequency_spinbox,
                                  self.setup.Z_frequency_spinbox]
        amplitude_spinbox_list = [self.setup.X_amplitude_spinbox, self.setup.Y_amplitude_spinbox,
                                  self.setup.Z_amplitude_spinbox]
        for i in range(3):
            frequency_spinbox_list[i].setValue(frequency_list[i])
            amplitude_spinbox_list[i].setValue(amplitude_list[i])

    def data_update(self, x, i, j):
        self.data[i, j] = x
        if i == 0 and j == 0:
            self.darkest = x
        else:
            self.darkest = min(x, self.darkest)
        self.data[i, j + 1:] = self.darkest
        self.data[i + 1:, :] = self.darkest
        self.Image_View.setImage(self.data)

    def closeEvent(self, event):
        self.setup.close()
        self.ControlClose_signal.emit()
        time.sleep(0.2)
        self.thread.exit()
        event.accept()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AttocubeScanning()
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.
    app.exec()
