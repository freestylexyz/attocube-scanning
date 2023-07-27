# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QObject, Signal, Slot
import sys
# from setup_UI import Ui_attocube_UI
from setup_UI_v2 import Ui_attocube_UI

class Setup(QWidget, Ui_attocube_UI):
    # Signals
    Enable_signal = Signal(int, bool)
    MeasureCap_signal = Signal(int)
    FrequencyChanging_signal = Signal(int, int)
    AmplitudeChanging_signal = Signal(int, int)
    Stepping_signal = Signal(int, int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect signal
        # Enable signal
        self.X_coarse_status_button.clicked.connect(lambda: self.enable_axis(4))
        self.Y_coarse_status_button.clicked.connect(lambda: self.enable_axis(5))
        self.Z_coarse_status_button.clicked.connect(lambda: self.enable_axis(6))
        self.X_scan_status_button.clicked.connect(lambda: self.enable_axis(1))
        self.Y_scan_status_button.clicked.connect(lambda: self.enable_axis(2))
        self.Z_scan_status_button.clicked.connect(lambda: self.enable_axis(3))
        self.gnd_all_button.clicked.connect(lambda: self.enable_axis(7))

        # Capacitance measurement signal
        self.X_coarse_cap_button.clicked.connect(lambda: self.measure_cap(4))
        self.Y_coarse_cap_button.clicked.connect(lambda: self.measure_cap(5))
        self.Z_coarse_cap_button.clicked.connect(lambda: self.measure_cap(6))
        self.X_scan_cap_button.clicked.connect(lambda: self.measure_cap(1))
        self.Y_scan_cap_button.clicked.connect(lambda: self.measure_cap(2))
        self.Z_scan_cap_button.clicked.connect(lambda: self.measure_cap(3))
        self.all_cap_button.clicked.connect(lambda: self.measure_cap(7))

        # Parameters signal
        self.X_frequency_spinbox.editingFinished.connect(lambda: self.change_frequency(4))
        self.Y_frequency_spinbox.editingFinished.connect(lambda: self.change_frequency(5))
        self.Z_frequency_spinbox.editingFinished.connect(lambda: self.change_frequency(6))
        self.X_amplitude_spinbox.editingFinished.connect(lambda: self.change_amplitude(4))
        self.Y_amplitude_spinbox.editingFinished.connect(lambda: self.change_amplitude(5))
        self.Z_amplitude_spinbox.editingFinished.connect(lambda: self.change_amplitude(6))

        # Step
        self.X_up_button.clicked.connect(lambda: self.step(4, True))
        self.Y_up_button.clicked.connect(lambda: self.step(5, True))
        self.Z_up_button.clicked.connect(lambda: self.step(6, True))
        self.X_down_button.clicked.connect(lambda: self.step(4, False))
        self.Y_down_button.clicked.connect(lambda: self.step(5, False))
        self.Z_down_button.clicked.connect(lambda: self.step(6, False))

        # Emitting operation slots

    def enable_axis(self, axis=7):
        button_list = [self.X_scan_status_button, self.Y_scan_status_button,
                       self.Z_scan_status_button, self.X_coarse_status_button,
                       self.Y_coarse_status_button, self.Z_coarse_status_button]
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
        button_list = [self.X_scan_status_button, self.Y_scan_status_button,
                       self.Z_scan_status_button, self.X_coarse_status_button,
                       self.Y_coarse_status_button, self.Z_coarse_status_button]
        for i, button in enumerate(button_list):
            button.setText('Disable' if status[i] else 'Enable')

    def measure_cap(self, axis=7):
        self.MeasureCap_signal.emit(axis)

    def cap_update(self, axis, cap):
        text_list = ['X: ', 'Y: ', 'Z: ', 'X: ', 'Y: ', 'Z: ']
        label_list = [self.X_scan_cap_label, self.Y_scan_cap_label,
                      self.Z_scan_cap_label, self.X_coarse_cap_label,
                      self.Y_coarse_cap_label, self.Z_coarse_cap_label]
        label_list[axis - 1].setText(text_list[axis - 1] + str(int(cap * 10e8)) + 'nF')

    def cap_update_all(self, cap_list):
        text_list = ['X: ', 'Y: ', 'Z: ', 'X: ', 'Y: ', 'Z: ']
        label_list = [self.X_scan_cap_label, self.Y_scan_cap_label,
                      self.Z_scan_cap_label, self.X_coarse_cap_label,
                      self.Y_coarse_cap_label, self.Z_coarse_cap_label]
        for i, cap in enumerate(cap_list):
            label_list[i].setText(text_list[i] + str(int(cap * 10e8)) + 'nF')

    def change_frequency(self, axis):
        spinbox_list = [self.X_frequency_spinbox, self.Y_frequency_spinbox,
                        self.Z_frequency_spinbox]
        spinbox = spinbox_list[axis - 4]
        self.FrequencyChanging_signal.emit(axis, spinbox.value())

    def change_amplitude(self, axis):
        spinbox_list = [self.X_amplitude_spinbox, self.Y_amplitude_spinbox,
                        self.Z_amplitude_spinbox]
        spinbox = spinbox_list[axis - 4]
        self.AmplitudeChanging_signal.emit(axis, spinbox.value())

    def step(self, axis, direction=True):
        spinbox_list = [self.X_stp_spinbox, self.Y_stp_spinbox,
                        self.Z_stp_spinbox]
        step_num = spinbox_list[axis - 4].value()
        if not direction:
            step_num = -step_num
        self.Stepping_signal.emit(axis, step_num)

    # Updating UI slot
    def para_update(self, frequency_list, amplitude_list):
        frequency_spinbox_list = [self.X_frequency_spinbox, self.Y_frequency_spinbox,
                                  self.Z_frequency_spinbox]
        amplitude_spinbox_list = [self.X_amplitude_spinbox, self.Y_amplitude_spinbox,
                                  self.Z_amplitude_spinbox]
        for i in range(3):
            frequency_spinbox_list[i].setValue(frequency_list[i])
            amplitude_spinbox_list[i].setValue(amplitude_list[i])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Setup()
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.
    app.exec()