# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scan_UI_v2.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

from pyqtgraph import ImageView

class Ui_Scan_UI(object):
    def setupUi(self, Scan_UI):
        if not Scan_UI.objectName():
            Scan_UI.setObjectName(u"Scan_UI")
        Scan_UI.resize(1409, 753)
        self.horizontalLayout_2 = QHBoxLayout(Scan_UI)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.Image_View_2 = ImageView(Scan_UI)
        self.Image_View_2.setObjectName(u"Image_View_2")

        self.gridLayout.addWidget(self.Image_View_2, 1, 0, 1, 1)

        self.Image_View_1 = ImageView(Scan_UI)
        self.Image_View_1.setObjectName(u"Image_View_1")

        self.gridLayout.addWidget(self.Image_View_1, 0, 0, 1, 1)

        self.groupBox = QGroupBox(Scan_UI)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(300, 0))
        self.groupBox.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Move_groupbox = QGroupBox(self.groupBox)
        self.Move_groupbox.setObjectName(u"Move_groupbox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Move_groupbox.sizePolicy().hasHeightForWidth())
        self.Move_groupbox.setSizePolicy(sizePolicy1)
        self.Move_groupbox.setMinimumSize(QSize(0, 200))
        self.gridLayout_3 = QGridLayout(self.Move_groupbox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.Move_groupbox)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.Move_groupbox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.X_move_spinbox = QDoubleSpinBox(self.Move_groupbox)
        self.X_move_spinbox.setObjectName(u"X_move_spinbox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.X_move_spinbox.sizePolicy().hasHeightForWidth())
        self.X_move_spinbox.setSizePolicy(sizePolicy3)
        self.X_move_spinbox.setMaximum(150.000000000000000)

        self.gridLayout_2.addWidget(self.X_move_spinbox, 0, 1, 1, 1)

        self.Y_move_spinbox = QDoubleSpinBox(self.Move_groupbox)
        self.Y_move_spinbox.setObjectName(u"Y_move_spinbox")
        sizePolicy3.setHeightForWidth(self.Y_move_spinbox.sizePolicy().hasHeightForWidth())
        self.Y_move_spinbox.setSizePolicy(sizePolicy3)
        self.Y_move_spinbox.setMaximum(150.000000000000000)

        self.gridLayout_2.addWidget(self.Y_move_spinbox, 1, 1, 1, 1)

        self.label_3 = QLabel(self.Move_groupbox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 2)

        self.speed_move_spinbox = QDoubleSpinBox(self.Move_groupbox)
        self.speed_move_spinbox.setObjectName(u"speed_move_spinbox")
        sizePolicy3.setHeightForWidth(self.speed_move_spinbox.sizePolicy().hasHeightForWidth())
        self.speed_move_spinbox.setSizePolicy(sizePolicy3)
        self.speed_move_spinbox.setDecimals(2)
        self.speed_move_spinbox.setMinimum(0.100000000000000)
        self.speed_move_spinbox.setValue(10.000000000000000)

        self.gridLayout_2.addWidget(self.speed_move_spinbox, 2, 2, 1, 1)

        self.start_move_button = QPushButton(self.Move_groupbox)
        self.start_move_button.setObjectName(u"start_move_button")
        sizePolicy3.setHeightForWidth(self.start_move_button.sizePolicy().hasHeightForWidth())
        self.start_move_button.setSizePolicy(sizePolicy3)
        self.start_move_button.setFont(font)

        self.gridLayout_2.addWidget(self.start_move_button, 0, 2, 2, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.Move_groupbox)

        self.poslabel = QLabel(self.groupBox)
        self.poslabel.setObjectName(u"poslabel")

        self.verticalLayout.addWidget(self.poslabel)

        self.Image_groupbox = QGroupBox(self.groupBox)
        self.Image_groupbox.setObjectName(u"Image_groupbox")
        self.gridLayout_5 = QGridLayout(self.Image_groupbox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_8 = QLabel(self.Image_groupbox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 7, 0, 1, 1)

        self.label_9 = QLabel(self.Image_groupbox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 8, 0, 1, 1)

        self.range_scan_spinbox = QDoubleSpinBox(self.Image_groupbox)
        self.range_scan_spinbox.setObjectName(u"range_scan_spinbox")
        sizePolicy3.setHeightForWidth(self.range_scan_spinbox.sizePolicy().hasHeightForWidth())
        self.range_scan_spinbox.setSizePolicy(sizePolicy3)
        self.range_scan_spinbox.setMaximum(150.000000000000000)
        self.range_scan_spinbox.setValue(68.000000000000000)

        self.gridLayout_4.addWidget(self.range_scan_spinbox, 2, 1, 1, 1)

        self.readdelay_scan_spinbox = QSpinBox(self.Image_groupbox)
        self.readdelay_scan_spinbox.setObjectName(u"readdelay_scan_spinbox")
        sizePolicy3.setHeightForWidth(self.readdelay_scan_spinbox.sizePolicy().hasHeightForWidth())
        self.readdelay_scan_spinbox.setSizePolicy(sizePolicy3)
        self.readdelay_scan_spinbox.setMaximum(1000)
        self.readdelay_scan_spinbox.setValue(40)

        self.gridLayout_4.addWidget(self.readdelay_scan_spinbox, 5, 1, 1, 1)

        self.label_5 = QLabel(self.Image_groupbox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_7 = QLabel(self.Image_groupbox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 6, 0, 1, 1)

        self.Ycenter_scan_spinbox = QDoubleSpinBox(self.Image_groupbox)
        self.Ycenter_scan_spinbox.setObjectName(u"Ycenter_scan_spinbox")
        sizePolicy3.setHeightForWidth(self.Ycenter_scan_spinbox.sizePolicy().hasHeightForWidth())
        self.Ycenter_scan_spinbox.setSizePolicy(sizePolicy3)
        self.Ycenter_scan_spinbox.setValue(35.000000000000000)

        self.gridLayout_4.addWidget(self.Ycenter_scan_spinbox, 1, 1, 1, 1)

        self.corner_scan_combobox = QComboBox(self.Image_groupbox)
        self.corner_scan_combobox.addItem("")
        self.corner_scan_combobox.addItem("")
        self.corner_scan_combobox.addItem("")
        self.corner_scan_combobox.addItem("")
        self.corner_scan_combobox.setObjectName(u"corner_scan_combobox")
        self.corner_scan_combobox.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.corner_scan_combobox.sizePolicy().hasHeightForWidth())
        self.corner_scan_combobox.setSizePolicy(sizePolicy4)

        self.gridLayout_4.addWidget(self.corner_scan_combobox, 8, 1, 1, 1)

        self.dir_scan_combobox = QComboBox(self.Image_groupbox)
        self.dir_scan_combobox.addItem("")
        self.dir_scan_combobox.addItem("")
        self.dir_scan_combobox.setObjectName(u"dir_scan_combobox")
        self.dir_scan_combobox.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.dir_scan_combobox.sizePolicy().hasHeightForWidth())
        self.dir_scan_combobox.setSizePolicy(sizePolicy4)

        self.gridLayout_4.addWidget(self.dir_scan_combobox, 7, 1, 1, 1)

        self.label_10 = QLabel(self.Image_groupbox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_6 = QLabel(self.Image_groupbox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 5, 0, 1, 1)

        self.linedelay_scan_spinbox = QSpinBox(self.Image_groupbox)
        self.linedelay_scan_spinbox.setObjectName(u"linedelay_scan_spinbox")
        sizePolicy3.setHeightForWidth(self.linedelay_scan_spinbox.sizePolicy().hasHeightForWidth())
        self.linedelay_scan_spinbox.setSizePolicy(sizePolicy3)
        self.linedelay_scan_spinbox.setMaximum(10000)
        self.linedelay_scan_spinbox.setValue(100)

        self.gridLayout_4.addWidget(self.linedelay_scan_spinbox, 6, 1, 1, 1)

        self.Xcenter_scan_spinbox = QDoubleSpinBox(self.Image_groupbox)
        self.Xcenter_scan_spinbox.setObjectName(u"Xcenter_scan_spinbox")
        sizePolicy3.setHeightForWidth(self.Xcenter_scan_spinbox.sizePolicy().hasHeightForWidth())
        self.Xcenter_scan_spinbox.setSizePolicy(sizePolicy3)
        self.Xcenter_scan_spinbox.setValue(35.000000000000000)

        self.gridLayout_4.addWidget(self.Xcenter_scan_spinbox, 0, 1, 1, 1)

        self.pixelnum_scan_spinbox = QSpinBox(self.Image_groupbox)
        self.pixelnum_scan_spinbox.setObjectName(u"pixelnum_scan_spinbox")
        sizePolicy3.setHeightForWidth(self.pixelnum_scan_spinbox.sizePolicy().hasHeightForWidth())
        self.pixelnum_scan_spinbox.setSizePolicy(sizePolicy3)
        self.pixelnum_scan_spinbox.setMinimum(2)
        self.pixelnum_scan_spinbox.setMaximum(4096)
        self.pixelnum_scan_spinbox.setValue(35)

        self.gridLayout_4.addWidget(self.pixelnum_scan_spinbox, 3, 1, 1, 1)

        self.label_4 = QLabel(self.Image_groupbox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_11 = QLabel(self.Image_groupbox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_12 = QLabel(self.Image_groupbox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 4, 0, 1, 1)

        self.angle_scan_spinbox = QDoubleSpinBox(self.Image_groupbox)
        self.angle_scan_spinbox.setObjectName(u"angle_scan_spinbox")
        self.angle_scan_spinbox.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.angle_scan_spinbox.sizePolicy().hasHeightForWidth())
        self.angle_scan_spinbox.setSizePolicy(sizePolicy3)
        self.angle_scan_spinbox.setMaximum(180.000000000000000)

        self.gridLayout_4.addWidget(self.angle_scan_spinbox, 4, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.start_scan_button = QPushButton(self.Image_groupbox)
        self.start_scan_button.setObjectName(u"start_scan_button")
        self.start_scan_button.setMinimumSize(QSize(0, 100))
        font1 = QFont()
        font1.setPointSize(48)
        self.start_scan_button.setFont(font1)

        self.gridLayout_5.addWidget(self.start_scan_button, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.Image_groupbox)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.setup_button = QPushButton(self.groupBox)
        self.setup_button.setObjectName(u"setup_button")
        self.setup_button.setMinimumSize(QSize(0, 50))
        self.setup_button.setFont(font)

        self.verticalLayout_2.addWidget(self.setup_button)


        self.gridLayout.addWidget(self.groupBox, 0, 2, 2, 1)

        self.Image_View_3 = ImageView(Scan_UI)
        self.Image_View_3.setObjectName(u"Image_View_3")

        self.gridLayout.addWidget(self.Image_View_3, 0, 1, 1, 1)

        self.Image_View_4 = ImageView(Scan_UI)
        self.Image_View_4.setObjectName(u"Image_View_4")

        self.gridLayout.addWidget(self.Image_View_4, 1, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)


        self.retranslateUi(Scan_UI)

        QMetaObject.connectSlotsByName(Scan_UI)
    # setupUi

    def retranslateUi(self, Scan_UI):
        Scan_UI.setWindowTitle(QCoreApplication.translate("Scan_UI", u"Scan", None))
        self.groupBox.setTitle(QCoreApplication.translate("Scan_UI", u"Scan control", None))
        self.Move_groupbox.setTitle(QCoreApplication.translate("Scan_UI", u"Move", None))
        self.label.setText(QCoreApplication.translate("Scan_UI", u"X", None))
        self.label_2.setText(QCoreApplication.translate("Scan_UI", u"Y", None))
        self.label_3.setText(QCoreApplication.translate("Scan_UI", u"speed (V/s)", None))
        self.start_move_button.setText(QCoreApplication.translate("Scan_UI", u"Move to", None))
        self.poslabel.setText(QCoreApplication.translate("Scan_UI", u"Position:", None))
        self.Image_groupbox.setTitle(QCoreApplication.translate("Scan_UI", u"Image", None))
        self.label_8.setText(QCoreApplication.translate("Scan_UI", u"Scan direction", None))
        self.label_9.setText(QCoreApplication.translate("Scan_UI", u"Starting corner", None))
        self.label_5.setText(QCoreApplication.translate("Scan_UI", u"Pixel number", None))
        self.label_7.setText(QCoreApplication.translate("Scan_UI", u"Line delay (ms)", None))
        self.corner_scan_combobox.setItemText(0, QCoreApplication.translate("Scan_UI", u"upper left", None))
        self.corner_scan_combobox.setItemText(1, QCoreApplication.translate("Scan_UI", u"upper right", None))
        self.corner_scan_combobox.setItemText(2, QCoreApplication.translate("Scan_UI", u"lower left", None))
        self.corner_scan_combobox.setItemText(3, QCoreApplication.translate("Scan_UI", u"lower right", None))

        self.dir_scan_combobox.setItemText(0, QCoreApplication.translate("Scan_UI", u"X fast Y slow", None))
        self.dir_scan_combobox.setItemText(1, QCoreApplication.translate("Scan_UI", u"Y fast X slow", None))

        self.label_10.setText(QCoreApplication.translate("Scan_UI", u"X center (V)", None))
        self.label_6.setText(QCoreApplication.translate("Scan_UI", u"Read delay (ms)", None))
        self.label_4.setText(QCoreApplication.translate("Scan_UI", u"Scan range (V)", None))
        self.label_11.setText(QCoreApplication.translate("Scan_UI", u"Y center  (V)", None))
        self.label_12.setText(QCoreApplication.translate("Scan_UI", u"Angle (degree)", None))
        self.start_scan_button.setText(QCoreApplication.translate("Scan_UI", u"Start", None))
        self.setup_button.setText(QCoreApplication.translate("Scan_UI", u"Setup up", None))
    # retranslateUi

