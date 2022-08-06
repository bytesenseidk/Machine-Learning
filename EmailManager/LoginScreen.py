# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginScreenCaISgP.ui'
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
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 10, 801, 111))
        self.TitleLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.TitleLayout.setObjectName(u"TitleLayout")
        self.TitleLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.TitleLayout.addWidget(self.label)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(60, 140, 681, 201))
        self.CenterLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.CenterLayout.setObjectName(u"CenterLayout")
        self.CenterLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.CenterLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"")
        self.lineEdit.setMaxLength(100)

        self.CenterLayout.addWidget(self.lineEdit)

        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.CenterLayout.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font2)
        self.lineEdit_3.setMaxLength(100)

        self.CenterLayout.addWidget(self.lineEdit_3)

        self.verticalWidget_3 = QWidget(self.centralwidget)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        self.verticalWidget_3.setGeometry(QRect(300, 410, 201, 80))
        self.BottomLayout = QVBoxLayout(self.verticalWidget_3)
        self.BottomLayout.setObjectName(u"BottomLayout")
        self.pushButton = QPushButton(self.verticalWidget_3)
        self.pushButton.setObjectName(u"pushButton")
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton.setFont(font3)

        self.BottomLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Email Manager", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_3.setPlaceholderText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

