# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SystemStopperVeKFAJ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(526, 294)
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_top = QLabel(self.centralwidget)
        self.label_top.setObjectName(u"label_top")
        self.label_top.setGeometry(QRect(80, 0, 351, 51))
        font1 = QFont()
        font1.setFamily(u"Rockwell Extra Bold")
        font1.setPointSize(24)
        self.label_top.setFont(font1)
        self.label_top.setAlignment(Qt.AlignCenter)
        self.entry_minutes = QLineEdit(self.centralwidget)
        self.entry_minutes.setObjectName(u"entry_minutes")
        self.entry_minutes.setGeometry(QRect(170, 70, 171, 31))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.entry_minutes.setFont(font2)
        self.entry_minutes.setAlignment(Qt.AlignCenter)
        self.radio_shutdown = QRadioButton(self.centralwidget)
        self.radio_shutdown.setObjectName(u"radio_shutdown")
        self.radio_shutdown.setGeometry(QRect(350, 60, 141, 17))
        self.radio_restart = QRadioButton(self.centralwidget)
        self.radio_restart.setObjectName(u"radio_restart")
        self.radio_restart.setGeometry(QRect(350, 80, 141, 17))
        self.label_minutes = QLabel(self.centralwidget)
        self.label_minutes.setObjectName(u"label_minutes")
        self.label_minutes.setGeometry(QRect(28, 70, 141, 31))
        font3 = QFont()
        font3.setFamily(u"Rockwell Extra Bold")
        font3.setPointSize(16)
        self.label_minutes.setFont(font3)
        self.label_minutes.setAlignment(Qt.AlignCenter)
        self.label_activation = QLabel(self.centralwidget)
        self.label_activation.setObjectName(u"label_activation")
        self.label_activation.setGeometry(QRect(90, 110, 331, 31))
        self.label_activation.setFont(font3)
        self.label_activation.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(180, 160, 151, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 526, 34))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"System Stopper", None))
        self.label_top.setText(QCoreApplication.translate("MainWindow", u"System Stopper", None))
        self.entry_minutes.setText("")
        self.radio_shutdown.setText(QCoreApplication.translate("MainWindow", u"Shutdown", None))
        self.radio_restart.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.label_minutes.setText(QCoreApplication.translate("MainWindow", u"Minutes:", None))
        self.label_activation.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
    # retranslateUi

