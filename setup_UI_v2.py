# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setup_UI_v2.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLayout, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_attocube_UI(object):
    def setupUi(self, attocube_UI):
        if not attocube_UI.objectName():
            attocube_UI.setObjectName(u"attocube_UI")
        attocube_UI.resize(548, 979)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(attocube_UI.sizePolicy().hasHeightForWidth())
        attocube_UI.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(attocube_UI)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.status_groupbox = QGroupBox(attocube_UI)
        self.status_groupbox.setObjectName(u"status_groupbox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.status_groupbox.sizePolicy().hasHeightForWidth())
        self.status_groupbox.setSizePolicy(sizePolicy1)
        self.status_groupbox.setMinimumSize(QSize(0, 200))
        self.gridLayout_6 = QGridLayout(self.status_groupbox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.status_layout = QGridLayout()
        self.status_layout.setObjectName(u"status_layout")
        self.Z_coarse_status_button = QPushButton(self.status_groupbox)
        self.Z_coarse_status_button.setObjectName(u"Z_coarse_status_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Z_coarse_status_button.sizePolicy().hasHeightForWidth())
        self.Z_coarse_status_button.setSizePolicy(sizePolicy2)

        self.status_layout.addWidget(self.Z_coarse_status_button, 3, 1, 1, 1)

        self.X_coarse_status_button = QPushButton(self.status_groupbox)
        self.X_coarse_status_button.setObjectName(u"X_coarse_status_button")
        sizePolicy2.setHeightForWidth(self.X_coarse_status_button.sizePolicy().hasHeightForWidth())
        self.X_coarse_status_button.setSizePolicy(sizePolicy2)

        self.status_layout.addWidget(self.X_coarse_status_button, 1, 1, 1, 1)

        self.Z_scan_status_button = QPushButton(self.status_groupbox)
        self.Z_scan_status_button.setObjectName(u"Z_scan_status_button")
        sizePolicy2.setHeightForWidth(self.Z_scan_status_button.sizePolicy().hasHeightForWidth())
        self.Z_scan_status_button.setSizePolicy(sizePolicy2)

        self.status_layout.addWidget(self.Z_scan_status_button, 3, 2, 1, 1)

        self.X_scan_status_button = QPushButton(self.status_groupbox)
        self.X_scan_status_button.setObjectName(u"X_scan_status_button")
        sizePolicy2.setHeightForWidth(self.X_scan_status_button.sizePolicy().hasHeightForWidth())
        self.X_scan_status_button.setSizePolicy(sizePolicy2)

        self.status_layout.addWidget(self.X_scan_status_button, 1, 2, 1, 1)

        self.Y_status_label = QLabel(self.status_groupbox)
        self.Y_status_label.setObjectName(u"Y_status_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Y_status_label.sizePolicy().hasHeightForWidth())
        self.Y_status_label.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setPointSize(20)
        self.Y_status_label.setFont(font)

        self.status_layout.addWidget(self.Y_status_label, 2, 0, 1, 1)

        self.Y_coarse_status_button = QPushButton(self.status_groupbox)
        self.Y_coarse_status_button.setObjectName(u"Y_coarse_status_button")
        sizePolicy2.setHeightForWidth(self.Y_coarse_status_button.sizePolicy().hasHeightForWidth())
        self.Y_coarse_status_button.setSizePolicy(sizePolicy2)

        self.status_layout.addWidget(self.Y_coarse_status_button, 2, 1, 1, 1)

        self.X_status_label = QLabel(self.status_groupbox)
        self.X_status_label.setObjectName(u"X_status_label")
        sizePolicy3.setHeightForWidth(self.X_status_label.sizePolicy().hasHeightForWidth())
        self.X_status_label.setSizePolicy(sizePolicy3)
        self.X_status_label.setFont(font)

        self.status_layout.addWidget(self.X_status_label, 1, 0, 1, 1)

        self.Z_status_label = QLabel(self.status_groupbox)
        self.Z_status_label.setObjectName(u"Z_status_label")
        sizePolicy3.setHeightForWidth(self.Z_status_label.sizePolicy().hasHeightForWidth())
        self.Z_status_label.setSizePolicy(sizePolicy3)
        self.Z_status_label.setFont(font)

        self.status_layout.addWidget(self.Z_status_label, 3, 0, 1, 1)

        self.scan_status_label = QLabel(self.status_groupbox)
        self.scan_status_label.setObjectName(u"scan_status_label")
        sizePolicy1.setHeightForWidth(self.scan_status_label.sizePolicy().hasHeightForWidth())
        self.scan_status_label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(14)
        self.scan_status_label.setFont(font1)

        self.status_layout.addWidget(self.scan_status_label, 0, 2, 1, 1)

        self.Y_scan_status_button = QPushButton(self.status_groupbox)
        self.Y_scan_status_button.setObjectName(u"Y_scan_status_button")
        sizePolicy2.setHeightForWidth(self.Y_scan_status_button.sizePolicy().hasHeightForWidth())
        self.Y_scan_status_button.setSizePolicy(sizePolicy2)

        self.status_layout.addWidget(self.Y_scan_status_button, 2, 2, 1, 1)

        self.coarse_status_label = QLabel(self.status_groupbox)
        self.coarse_status_label.setObjectName(u"coarse_status_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.coarse_status_label.sizePolicy().hasHeightForWidth())
        self.coarse_status_label.setSizePolicy(sizePolicy4)
        self.coarse_status_label.setFont(font1)

        self.status_layout.addWidget(self.coarse_status_label, 0, 1, 1, 1)

        self.gnd_all_button = QPushButton(self.status_groupbox)
        self.gnd_all_button.setObjectName(u"gnd_all_button")
        sizePolicy2.setHeightForWidth(self.gnd_all_button.sizePolicy().hasHeightForWidth())
        self.gnd_all_button.setSizePolicy(sizePolicy2)

        self.status_layout.addWidget(self.gnd_all_button, 1, 3, 3, 1)


        self.gridLayout_6.addLayout(self.status_layout, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.status_groupbox)

        self.cap_groupbox = QGroupBox(attocube_UI)
        self.cap_groupbox.setObjectName(u"cap_groupbox")
        sizePolicy1.setHeightForWidth(self.cap_groupbox.sizePolicy().hasHeightForWidth())
        self.cap_groupbox.setSizePolicy(sizePolicy1)
        self.cap_groupbox.setMinimumSize(QSize(0, 250))
        self.gridLayout_3 = QGridLayout(self.cap_groupbox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cap_layout = QGridLayout()
        self.cap_layout.setObjectName(u"cap_layout")
        self.Y_coarse_cap_button = QPushButton(self.cap_groupbox)
        self.Y_coarse_cap_button.setObjectName(u"Y_coarse_cap_button")
        sizePolicy4.setHeightForWidth(self.Y_coarse_cap_button.sizePolicy().hasHeightForWidth())
        self.Y_coarse_cap_button.setSizePolicy(sizePolicy4)

        self.cap_layout.addWidget(self.Y_coarse_cap_button, 2, 1, 1, 1)

        self.X_scan_cap_label = QLabel(self.cap_groupbox)
        self.X_scan_cap_label.setObjectName(u"X_scan_cap_label")
        sizePolicy4.setHeightForWidth(self.X_scan_cap_label.sizePolicy().hasHeightForWidth())
        self.X_scan_cap_label.setSizePolicy(sizePolicy4)
        self.X_scan_cap_label.setFont(font)

        self.cap_layout.addWidget(self.X_scan_cap_label, 1, 2, 1, 1)

        self.Y_coarse_cap_label = QLabel(self.cap_groupbox)
        self.Y_coarse_cap_label.setObjectName(u"Y_coarse_cap_label")
        sizePolicy4.setHeightForWidth(self.Y_coarse_cap_label.sizePolicy().hasHeightForWidth())
        self.Y_coarse_cap_label.setSizePolicy(sizePolicy4)
        self.Y_coarse_cap_label.setFont(font)

        self.cap_layout.addWidget(self.Y_coarse_cap_label, 2, 0, 1, 1)

        self.Y_scan_cap_button = QPushButton(self.cap_groupbox)
        self.Y_scan_cap_button.setObjectName(u"Y_scan_cap_button")
        sizePolicy2.setHeightForWidth(self.Y_scan_cap_button.sizePolicy().hasHeightForWidth())
        self.Y_scan_cap_button.setSizePolicy(sizePolicy2)

        self.cap_layout.addWidget(self.Y_scan_cap_button, 2, 3, 1, 1)

        self.scanning_cap_label = QLabel(self.cap_groupbox)
        self.scanning_cap_label.setObjectName(u"scanning_cap_label")
        sizePolicy4.setHeightForWidth(self.scanning_cap_label.sizePolicy().hasHeightForWidth())
        self.scanning_cap_label.setSizePolicy(sizePolicy4)
        self.scanning_cap_label.setFont(font1)

        self.cap_layout.addWidget(self.scanning_cap_label, 0, 2, 1, 2)

        self.Z_coarse_cap_label = QLabel(self.cap_groupbox)
        self.Z_coarse_cap_label.setObjectName(u"Z_coarse_cap_label")
        sizePolicy4.setHeightForWidth(self.Z_coarse_cap_label.sizePolicy().hasHeightForWidth())
        self.Z_coarse_cap_label.setSizePolicy(sizePolicy4)
        self.Z_coarse_cap_label.setFont(font)

        self.cap_layout.addWidget(self.Z_coarse_cap_label, 3, 0, 1, 1)

        self.Y_scan_cap_label = QLabel(self.cap_groupbox)
        self.Y_scan_cap_label.setObjectName(u"Y_scan_cap_label")
        sizePolicy4.setHeightForWidth(self.Y_scan_cap_label.sizePolicy().hasHeightForWidth())
        self.Y_scan_cap_label.setSizePolicy(sizePolicy4)
        self.Y_scan_cap_label.setFont(font)

        self.cap_layout.addWidget(self.Y_scan_cap_label, 2, 2, 1, 1)

        self.X_coarse_cap_button = QPushButton(self.cap_groupbox)
        self.X_coarse_cap_button.setObjectName(u"X_coarse_cap_button")
        sizePolicy4.setHeightForWidth(self.X_coarse_cap_button.sizePolicy().hasHeightForWidth())
        self.X_coarse_cap_button.setSizePolicy(sizePolicy4)

        self.cap_layout.addWidget(self.X_coarse_cap_button, 1, 1, 1, 1)

        self.Z_scan_cap_label = QLabel(self.cap_groupbox)
        self.Z_scan_cap_label.setObjectName(u"Z_scan_cap_label")
        sizePolicy4.setHeightForWidth(self.Z_scan_cap_label.sizePolicy().hasHeightForWidth())
        self.Z_scan_cap_label.setSizePolicy(sizePolicy4)
        self.Z_scan_cap_label.setFont(font)

        self.cap_layout.addWidget(self.Z_scan_cap_label, 3, 2, 1, 1)

        self.X_coarse_cap_label = QLabel(self.cap_groupbox)
        self.X_coarse_cap_label.setObjectName(u"X_coarse_cap_label")
        sizePolicy4.setHeightForWidth(self.X_coarse_cap_label.sizePolicy().hasHeightForWidth())
        self.X_coarse_cap_label.setSizePolicy(sizePolicy4)
        self.X_coarse_cap_label.setFont(font)

        self.cap_layout.addWidget(self.X_coarse_cap_label, 1, 0, 1, 1)

        self.coarse_cap_label = QLabel(self.cap_groupbox)
        self.coarse_cap_label.setObjectName(u"coarse_cap_label")
        sizePolicy1.setHeightForWidth(self.coarse_cap_label.sizePolicy().hasHeightForWidth())
        self.coarse_cap_label.setSizePolicy(sizePolicy1)
        self.coarse_cap_label.setFont(font1)

        self.cap_layout.addWidget(self.coarse_cap_label, 0, 0, 1, 2)

        self.Z_scan_cap_button = QPushButton(self.cap_groupbox)
        self.Z_scan_cap_button.setObjectName(u"Z_scan_cap_button")
        sizePolicy2.setHeightForWidth(self.Z_scan_cap_button.sizePolicy().hasHeightForWidth())
        self.Z_scan_cap_button.setSizePolicy(sizePolicy2)

        self.cap_layout.addWidget(self.Z_scan_cap_button, 3, 3, 1, 1)

        self.Z_coarse_cap_button = QPushButton(self.cap_groupbox)
        self.Z_coarse_cap_button.setObjectName(u"Z_coarse_cap_button")
        sizePolicy4.setHeightForWidth(self.Z_coarse_cap_button.sizePolicy().hasHeightForWidth())
        self.Z_coarse_cap_button.setSizePolicy(sizePolicy4)

        self.cap_layout.addWidget(self.Z_coarse_cap_button, 3, 1, 1, 1)

        self.X_scan_cap_button = QPushButton(self.cap_groupbox)
        self.X_scan_cap_button.setObjectName(u"X_scan_cap_button")
        sizePolicy2.setHeightForWidth(self.X_scan_cap_button.sizePolicy().hasHeightForWidth())
        self.X_scan_cap_button.setSizePolicy(sizePolicy2)

        self.cap_layout.addWidget(self.X_scan_cap_button, 1, 3, 1, 1)

        self.all_cap_button = QPushButton(self.cap_groupbox)
        self.all_cap_button.setObjectName(u"all_cap_button")
        sizePolicy4.setHeightForWidth(self.all_cap_button.sizePolicy().hasHeightForWidth())
        self.all_cap_button.setSizePolicy(sizePolicy4)

        self.cap_layout.addWidget(self.all_cap_button, 4, 2, 1, 2)


        self.gridLayout_3.addLayout(self.cap_layout, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.cap_groupbox)

        self.para_groupbox = QGroupBox(attocube_UI)
        self.para_groupbox.setObjectName(u"para_groupbox")
        sizePolicy1.setHeightForWidth(self.para_groupbox.sizePolicy().hasHeightForWidth())
        self.para_groupbox.setSizePolicy(sizePolicy1)
        self.para_groupbox.setMinimumSize(QSize(0, 200))
        self.gridLayout_2 = QGridLayout(self.para_groupbox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.para_groupbox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_3 = QLabel(self.para_groupbox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label = QLabel(self.para_groupbox)
        self.label.setObjectName(u"label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.Z_amplitude_spinbox = QSpinBox(self.para_groupbox)
        self.Z_amplitude_spinbox.setObjectName(u"Z_amplitude_spinbox")
        sizePolicy2.setHeightForWidth(self.Z_amplitude_spinbox.sizePolicy().hasHeightForWidth())
        self.Z_amplitude_spinbox.setSizePolicy(sizePolicy2)
        self.Z_amplitude_spinbox.setMaximum(150)

        self.gridLayout.addWidget(self.Z_amplitude_spinbox, 3, 2, 1, 1)

        self.X_amplitude_spinbox = QSpinBox(self.para_groupbox)
        self.X_amplitude_spinbox.setObjectName(u"X_amplitude_spinbox")
        sizePolicy2.setHeightForWidth(self.X_amplitude_spinbox.sizePolicy().hasHeightForWidth())
        self.X_amplitude_spinbox.setSizePolicy(sizePolicy2)
        self.X_amplitude_spinbox.setMaximum(150)

        self.gridLayout.addWidget(self.X_amplitude_spinbox, 1, 2, 1, 1)

        self.Y_frequency_spinbox = QSpinBox(self.para_groupbox)
        self.Y_frequency_spinbox.setObjectName(u"Y_frequency_spinbox")
        sizePolicy2.setHeightForWidth(self.Y_frequency_spinbox.sizePolicy().hasHeightForWidth())
        self.Y_frequency_spinbox.setSizePolicy(sizePolicy2)
        self.Y_frequency_spinbox.setMaximum(1500)

        self.gridLayout.addWidget(self.Y_frequency_spinbox, 2, 1, 1, 1)

        self.Z_frequency_spinbox = QSpinBox(self.para_groupbox)
        self.Z_frequency_spinbox.setObjectName(u"Z_frequency_spinbox")
        sizePolicy2.setHeightForWidth(self.Z_frequency_spinbox.sizePolicy().hasHeightForWidth())
        self.Z_frequency_spinbox.setSizePolicy(sizePolicy2)
        self.Z_frequency_spinbox.setMaximum(1500)

        self.gridLayout.addWidget(self.Z_frequency_spinbox, 3, 1, 1, 1)

        self.X_frequency_spinbox = QSpinBox(self.para_groupbox)
        self.X_frequency_spinbox.setObjectName(u"X_frequency_spinbox")
        sizePolicy2.setHeightForWidth(self.X_frequency_spinbox.sizePolicy().hasHeightForWidth())
        self.X_frequency_spinbox.setSizePolicy(sizePolicy2)
        self.X_frequency_spinbox.setMaximum(1500)

        self.gridLayout.addWidget(self.X_frequency_spinbox, 1, 1, 1, 1)

        self.Y_amplitude_spinbox = QSpinBox(self.para_groupbox)
        self.Y_amplitude_spinbox.setObjectName(u"Y_amplitude_spinbox")
        sizePolicy2.setHeightForWidth(self.Y_amplitude_spinbox.sizePolicy().hasHeightForWidth())
        self.Y_amplitude_spinbox.setSizePolicy(sizePolicy2)
        self.Y_amplitude_spinbox.setMaximum(150)

        self.gridLayout.addWidget(self.Y_amplitude_spinbox, 2, 2, 1, 1)

        self.label_4 = QLabel(self.para_groupbox)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(16)
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_5 = QLabel(self.para_groupbox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setFont(font2)

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.para_groupbox)

        self.stepping_groupbox = QGroupBox(attocube_UI)
        self.stepping_groupbox.setObjectName(u"stepping_groupbox")
        sizePolicy1.setHeightForWidth(self.stepping_groupbox.sizePolicy().hasHeightForWidth())
        self.stepping_groupbox.setSizePolicy(sizePolicy1)
        self.stepping_groupbox.setMinimumSize(QSize(0, 200))
        self.gridLayout_4 = QGridLayout(self.stepping_groupbox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stepping_layout = QGridLayout()
        self.stepping_layout.setObjectName(u"stepping_layout")
        self.stepping_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.Z_stp_label = QLabel(self.stepping_groupbox)
        self.Z_stp_label.setObjectName(u"Z_stp_label")
        self.Z_stp_label.setFont(font)

        self.stepping_layout.addWidget(self.Z_stp_label, 2, 0, 1, 1)

        self.X_stp_spinbox = QSpinBox(self.stepping_groupbox)
        self.X_stp_spinbox.setObjectName(u"X_stp_spinbox")
        sizePolicy2.setHeightForWidth(self.X_stp_spinbox.sizePolicy().hasHeightForWidth())
        self.X_stp_spinbox.setSizePolicy(sizePolicy2)
        self.X_stp_spinbox.setMaximum(10000)
        self.X_stp_spinbox.setValue(1)

        self.stepping_layout.addWidget(self.X_stp_spinbox, 0, 1, 1, 1)

        self.Y_up_button = QPushButton(self.stepping_groupbox)
        self.Y_up_button.setObjectName(u"Y_up_button")
        sizePolicy2.setHeightForWidth(self.Y_up_button.sizePolicy().hasHeightForWidth())
        self.Y_up_button.setSizePolicy(sizePolicy2)

        self.stepping_layout.addWidget(self.Y_up_button, 1, 2, 1, 1)

        self.Y_stp_label = QLabel(self.stepping_groupbox)
        self.Y_stp_label.setObjectName(u"Y_stp_label")
        self.Y_stp_label.setFont(font)

        self.stepping_layout.addWidget(self.Y_stp_label, 1, 0, 1, 1)

        self.Z_stp_spinbox = QSpinBox(self.stepping_groupbox)
        self.Z_stp_spinbox.setObjectName(u"Z_stp_spinbox")
        sizePolicy2.setHeightForWidth(self.Z_stp_spinbox.sizePolicy().hasHeightForWidth())
        self.Z_stp_spinbox.setSizePolicy(sizePolicy2)
        self.Z_stp_spinbox.setMaximum(10000)
        self.Z_stp_spinbox.setValue(1)

        self.stepping_layout.addWidget(self.Z_stp_spinbox, 2, 1, 1, 1)

        self.Z_up_button = QPushButton(self.stepping_groupbox)
        self.Z_up_button.setObjectName(u"Z_up_button")
        sizePolicy2.setHeightForWidth(self.Z_up_button.sizePolicy().hasHeightForWidth())
        self.Z_up_button.setSizePolicy(sizePolicy2)

        self.stepping_layout.addWidget(self.Z_up_button, 2, 2, 1, 1)

        self.Z_down_button = QPushButton(self.stepping_groupbox)
        self.Z_down_button.setObjectName(u"Z_down_button")
        sizePolicy2.setHeightForWidth(self.Z_down_button.sizePolicy().hasHeightForWidth())
        self.Z_down_button.setSizePolicy(sizePolicy2)

        self.stepping_layout.addWidget(self.Z_down_button, 2, 3, 1, 1)

        self.X_down_button = QPushButton(self.stepping_groupbox)
        self.X_down_button.setObjectName(u"X_down_button")
        sizePolicy2.setHeightForWidth(self.X_down_button.sizePolicy().hasHeightForWidth())
        self.X_down_button.setSizePolicy(sizePolicy2)

        self.stepping_layout.addWidget(self.X_down_button, 0, 3, 1, 1)

        self.Y_stp_spinbox = QSpinBox(self.stepping_groupbox)
        self.Y_stp_spinbox.setObjectName(u"Y_stp_spinbox")
        sizePolicy2.setHeightForWidth(self.Y_stp_spinbox.sizePolicy().hasHeightForWidth())
        self.Y_stp_spinbox.setSizePolicy(sizePolicy2)
        self.Y_stp_spinbox.setMaximum(10000)
        self.Y_stp_spinbox.setValue(1)

        self.stepping_layout.addWidget(self.Y_stp_spinbox, 1, 1, 1, 1)

        self.X_up_button = QPushButton(self.stepping_groupbox)
        self.X_up_button.setObjectName(u"X_up_button")
        sizePolicy2.setHeightForWidth(self.X_up_button.sizePolicy().hasHeightForWidth())
        self.X_up_button.setSizePolicy(sizePolicy2)

        self.stepping_layout.addWidget(self.X_up_button, 0, 2, 1, 1)

        self.X_stp_label = QLabel(self.stepping_groupbox)
        self.X_stp_label.setObjectName(u"X_stp_label")
        sizePolicy5.setHeightForWidth(self.X_stp_label.sizePolicy().hasHeightForWidth())
        self.X_stp_label.setSizePolicy(sizePolicy5)
        self.X_stp_label.setFont(font)

        self.stepping_layout.addWidget(self.X_stp_label, 0, 0, 1, 1)

        self.Y_down_button = QPushButton(self.stepping_groupbox)
        self.Y_down_button.setObjectName(u"Y_down_button")
        sizePolicy2.setHeightForWidth(self.Y_down_button.sizePolicy().hasHeightForWidth())
        self.Y_down_button.setSizePolicy(sizePolicy2)

        self.stepping_layout.addWidget(self.Y_down_button, 1, 3, 1, 1)


        self.gridLayout_4.addLayout(self.stepping_layout, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.stepping_groupbox)

        self.sync_button = QPushButton(attocube_UI)
        self.sync_button.setObjectName(u"sync_button")
        self.sync_button.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.sync_button)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(attocube_UI)

        QMetaObject.connectSlotsByName(attocube_UI)
    # setupUi

    def retranslateUi(self, attocube_UI):
        attocube_UI.setWindowTitle(QCoreApplication.translate("attocube_UI", u"Attocube setup", None))
        self.status_groupbox.setTitle(QCoreApplication.translate("attocube_UI", u"Status", None))
        self.Z_coarse_status_button.setText(QCoreApplication.translate("attocube_UI", u"Enable", None))
        self.X_coarse_status_button.setText(QCoreApplication.translate("attocube_UI", u"Enable", None))
        self.Z_scan_status_button.setText(QCoreApplication.translate("attocube_UI", u"Enable", None))
        self.X_scan_status_button.setText(QCoreApplication.translate("attocube_UI", u"Enable", None))
        self.Y_status_label.setText(QCoreApplication.translate("attocube_UI", u"Y", None))
        self.Y_coarse_status_button.setText(QCoreApplication.translate("attocube_UI", u"Enable", None))
        self.X_status_label.setText(QCoreApplication.translate("attocube_UI", u"X", None))
        self.Z_status_label.setText(QCoreApplication.translate("attocube_UI", u"Z", None))
        self.scan_status_label.setText(QCoreApplication.translate("attocube_UI", u"Scanning", None))
        self.Y_scan_status_button.setText(QCoreApplication.translate("attocube_UI", u"Enable", None))
        self.coarse_status_label.setText(QCoreApplication.translate("attocube_UI", u"Coarse", None))
        self.gnd_all_button.setText(QCoreApplication.translate("attocube_UI", u"GND All", None))
        self.cap_groupbox.setTitle(QCoreApplication.translate("attocube_UI", u"Capacitance", None))
        self.Y_coarse_cap_button.setText(QCoreApplication.translate("attocube_UI", u"Measure", None))
        self.X_scan_cap_label.setText(QCoreApplication.translate("attocube_UI", u"X: NA", None))
        self.Y_coarse_cap_label.setText(QCoreApplication.translate("attocube_UI", u"Y: NA", None))
        self.Y_scan_cap_button.setText(QCoreApplication.translate("attocube_UI", u"Measure", None))
        self.scanning_cap_label.setText(QCoreApplication.translate("attocube_UI", u"Scanning", None))
        self.Z_coarse_cap_label.setText(QCoreApplication.translate("attocube_UI", u"Z: NA", None))
        self.Y_scan_cap_label.setText(QCoreApplication.translate("attocube_UI", u"Y: NA", None))
        self.X_coarse_cap_button.setText(QCoreApplication.translate("attocube_UI", u"Measure", None))
        self.Z_scan_cap_label.setText(QCoreApplication.translate("attocube_UI", u"Z: NA", None))
        self.X_coarse_cap_label.setText(QCoreApplication.translate("attocube_UI", u"X: NA", None))
        self.coarse_cap_label.setText(QCoreApplication.translate("attocube_UI", u"Coarse", None))
        self.Z_scan_cap_button.setText(QCoreApplication.translate("attocube_UI", u"Measure", None))
        self.Z_coarse_cap_button.setText(QCoreApplication.translate("attocube_UI", u"Measure", None))
        self.X_scan_cap_button.setText(QCoreApplication.translate("attocube_UI", u"Measure", None))
        self.all_cap_button.setText(QCoreApplication.translate("attocube_UI", u"Measure All", None))
        self.para_groupbox.setTitle(QCoreApplication.translate("attocube_UI", u"Parameters", None))
        self.label_2.setText(QCoreApplication.translate("attocube_UI", u"Y", None))
        self.label_3.setText(QCoreApplication.translate("attocube_UI", u"Z", None))
        self.label.setText(QCoreApplication.translate("attocube_UI", u"X", None))
        self.label_4.setText(QCoreApplication.translate("attocube_UI", u"Frequency (Hz)", None))
        self.label_5.setText(QCoreApplication.translate("attocube_UI", u"Amplitude (V)", None))
        self.stepping_groupbox.setTitle(QCoreApplication.translate("attocube_UI", u"Stepping", None))
        self.Z_stp_label.setText(QCoreApplication.translate("attocube_UI", u"Z", None))
        self.Y_up_button.setText(QCoreApplication.translate("attocube_UI", u"Down", None))
        self.Y_stp_label.setText(QCoreApplication.translate("attocube_UI", u"Y", None))
        self.Z_up_button.setText(QCoreApplication.translate("attocube_UI", u"UP", None))
        self.Z_down_button.setText(QCoreApplication.translate("attocube_UI", u"DOWN", None))
        self.X_down_button.setText(QCoreApplication.translate("attocube_UI", u"Left", None))
        self.X_up_button.setText(QCoreApplication.translate("attocube_UI", u"Right", None))
        self.X_stp_label.setText(QCoreApplication.translate("attocube_UI", u"X", None))
        self.Y_down_button.setText(QCoreApplication.translate("attocube_UI", u"Up", None))
        self.sync_button.setText(QCoreApplication.translate("attocube_UI", u"Sync", None))
    # retranslateUi

