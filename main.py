# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import Slot, Signal, QThread, QObject
import sys
import numpy as np
import time
# from scan_UI import Ui_Scan_UI
from scan_UI_v2 import Ui_Scan_UI
from Setup import Setup
from attocube import Controller
import pyqtgraph as pg


class AttocubeScanning(QWidget, Ui_Scan_UI):
    # Signals
    MoveTo_signal = Signal(float, float, float)
    StartScan_signal = Signal(list, float, int, list, float, list,
                              int)  # (center step_size, pixel_num, delays, move_speed, end, scan_dir)
    ControlClose_signal = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup = Setup()
        self.thread = QThread()
        self.control = Controller(attocube_addr='COM3', sr860_addr='GPIB0::3::INSTR', sr830_addr='GPIB0::6::INSTR')
        self.control.moveToThread(self.thread)

        # # Set up plot widget
        # lower_limit, higher_limit = 0, 70
        # self.Image_View_1.setLimits(xMin=lower_limit, xMax=higher_limit, yMin=lower_limit, yMax=higher_limit)
        # self.Image_View_1.plotItem.vb.setAspectLocked(lock=True, ratio=1)
        # self.Image_View_2.setLimits(xMin=lower_limit, xMax=higher_limit, yMin=lower_limit, yMax=higher_limit)
        # self.Image_View_2.plotItem.vb.setAspectLocked(lock=True, ratio=1)
        # self.Image_View_3.setLimits(xMin=lower_limit, xMax=higher_limit, yMin=lower_limit, yMax=higher_limit)
        # self.Image_View_3.plotItem.vb.setAspectLocked(lock=True, ratio=1)
        # self.Image_View_4.setLimits(xMin=lower_limit, xMax=higher_limit, yMin=lower_limit, yMax=higher_limit)
        # self.Image_View_4.plotItem.vb.setAspectLocked(lock=True, ratio=1)
        #
        # # Levels will be overwritten unless enableAutoLevels is set to False
        # self.map_1 = pg.PColorMeshItem(edgecolors=None, antialiasing=False, colorMap=pg.colormap.get('viridis'),
        #                                levels=(-2, 2), enableAutoLevels=True)
        # self.map_2 = pg.PColorMeshItem(edgecolors=None, antialiasing=False, colorMap=pg.colormap.get('viridis'),
        #                                levels=(-2, 2), enableAutoLevels=True)
        # self.map_3 = pg.PColorMeshItem(edgecolors=None, antialiasing=False, colorMap=pg.colormap.get('viridis'),
        #                                levels=(-2, 2), enableAutoLevels=True)
        # self.map_4 = pg.PColorMeshItem(edgecolors=None, antialiasing=False, colorMap=pg.colormap.get('viridis'),
        #                                levels=(-2, 2), enableAutoLevels=True)

        # self.Image_View_1.addItem(self.map_1)
        # self.Image_View_2.addItem(self.map_2)
        # self.Image_View_3.addItem(self.map_3)
        # self.Image_View_4.addItem(self.map_4)

        # Variables
        pixel_num = self.pixelnum_scan_spinbox.value()
        self.data = self.data = np.zeros((4, pixel_num, pixel_num))
        self.darkest = np.zeros(4)

        # Sync
        self.setup.sync_button.clicked.connect(self.control.sync_info)

        # Scan
        self.start_move_button.clicked.connect(self.move_to)
        self.start_scan_button.clicked.connect(self.scan)
        self.setup_button.clicked.connect(self.setup.show)

        # Control
        self.setup.Enable_signal.connect(self.control.enable)
        self.setup.MeasureCap_signal.connect(self.control.measure_cap)
        self.setup.FrequencyChanging_signal.connect(self.control.atto.set_frequency)
        self.setup.AmplitudeChanging_signal.connect(self.control.atto.set_voltage)
        self.setup.Stepping_signal.connect(self.control.atto.move_by)
        self.MoveTo_signal.connect(self.control.move_to)
        self.StartScan_signal.connect(self.control.scan)
        self.ControlClose_signal.connect(self.control.close)

        # Update
        self.control.AxisStatusChanged.connect(self.setup.status_update)
        self.control.CapMeasured.connect(self.setup.cap_update)
        self.control.CapMeasuredAll.connect(self.setup.cap_update_all)
        self.control.ParaSync.connect(self.setup.para_update)
        self.control.data_signal.connect(self.data_update)
        self.control.MoveFinished.connect(lambda: self.start_move_button.setText('Move to'))
        self.control.ScanFinished.connect(lambda: self.start_scan_button.setText('Start'))

        # Start preparation
        self.setup.show()
        self.thread.start()

        views = [self.Image_View_1, self.Image_View_2, self.Image_View_3, self.Image_View_4]
        for k in range(4):
            views[k].setImage(self.data[k])
            views[k].imageItem.hoverEvent = self.imageHoverEvent
        # self.Image_View_1.imageItem.hoverEvent = self.imageHoverEvent
        # self.Image_View_2.imageItem.hoverEvent = self.imageHoverEvent
        # self.Image_View_3.imageItem.hoverEvent = self.imageHoverEvent
        # self.Image_View_4.imageItem.hoverEvent = self.imageHoverEvent

    # Emitting operation slots
    def scan(self):
        if self.start_scan_button.text() == 'Start':
            center = [self.Xcenter_scan_spinbox.value(), self.Ycenter_scan_spinbox.value()]
            pixel_num = self.pixelnum_scan_spinbox.value()
            scan_size = self.range_scan_spinbox.value()
            move_speed = self.speed_move_spinbox.value()
            delays = [self.readdelay_scan_spinbox.value(), self.linedelay_scan_spinbox.value()]
            self.data = np.zeros((4, pixel_num, pixel_num))
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
    def data_update(self, x, i, j):
        views = [self.Image_View_1, self.Image_View_2, self.Image_View_3, self.Image_View_4]
        for k in range(4):
            self.data[k, i, j] = x[k]
            if i == 0 and j == 0:
                self.darkest[k] = x[k]
            else:
                self.darkest[k] = min(x[k], self.darkest[k])
            self.data[k, i, j + 1:] = self.darkest[k]
            self.data[k, i + 1:, :] = self.darkest[k]
            views[k].setImage(self.data[k])

    def imageHoverEvent(self, event):
        center = [self.Xcenter_scan_spinbox.value(), self.Ycenter_scan_spinbox.value()]
        pixel_num = self.pixelnum_scan_spinbox.value()
        scan_size = self.range_scan_spinbox.value()
        x_start, y_start = center[0] - (scan_size / 2), center[1] - (scan_size / 2)
        step_size = scan_size / (pixel_num - 1)
        if event.isExit():
            self.poslabel.setText("Position:")
            return
        pos = event.pos()
        i, j = pos.y(), pos.x()
        x, y = (i * step_size) + x_start, (j * step_size) + y_start
        self.poslabel.setText("Position: (%0.1f, %0.1f)" % (x, y))

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
