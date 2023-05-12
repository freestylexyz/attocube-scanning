# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
import sys
from setup_UI import Ui_attocube_UI

class Setup(QWidget, Ui_attocube_UI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Setup()
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.
    app.exec()