import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 802, 296)
        self.setWindowTitle("Number System Converter")
        self.initUI()

    def initUI(self):
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 271))
        
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)

        self.tab_binary = QWidget()
        self.tab_binary.setObjectName(u"tab_binary")

        self.toplabel_binary = QLabel(self.tab_binary)
        self.toplabel_binary.setObjectName(u"toplabel_binary")
        self.toplabel_binary.setGeometry(QRect(280, 0, 251, 41))
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setWeight(75)
        self.toplabel_binary.setFont(font1)
        self.toplabel_binary.setAlignment(Qt.AlignCenter)

        self.entry_binary = QLineEdit(self.tab_binary)
        self.entry_binary.setObjectName(u"entry_binary")
        self.entry_binary.setGeometry(QRect(150, 60, 571, 31))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.entry_binary.setFont(font2)
        self.entry_binary.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        
        self.label_binary = QLabel(self.tab_binary)
        self.label_binary.setObjectName(u"label_binary")
        self.label_binary.setGeometry(QRect(20, 60, 121, 31))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_binary.setFont(font3)
        self.label_binary.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        
        self.entry_decimal = QLineEdit(self.tab_binary)
        self.entry_decimal.setObjectName(u"entry_decimal")
        self.entry_decimal.setGeometry(QRect(150, 100, 571, 31))
        self.entry_decimal.setFont(font2)
        self.entry_decimal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        
        self.label_decimal = QLabel(self.tab_binary)
        self.label_decimal.setObjectName(u"label_decimal")
        self.label_decimal.setGeometry(QRect(20, 100, 121, 31))
        self.label_decimal.setFont(font3)
        self.label_decimal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        
        self.button_binary = QPushButton(self.tab_binary)
        self.button_binary.setObjectName(u"button_binary")
        self.button_binary.setGeometry(QRect(350, 160, 101, 51))
        self.button_binary.setFont(font3)
        
        self.tabWidget.addTab(self.tab_binary, "")
        self.tab_hexa = QWidget()
        self.tab_hexa.setObjectName(u"tab_hexa")

        self.label_decimal_hexa = QLabel(self.tab_hexa)
        self.label_decimal_hexa.setObjectName(u"label_decimal_hexa")
        self.label_decimal_hexa.setGeometry(QRect(20, 100, 121, 31))
        self.label_decimal_hexa.setFont(font3)
        self.label_decimal_hexa.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        
        self.entry_hexa = QLineEdit(self.tab_hexa)
        self.entry_hexa.setObjectName(u"entry_hexa")
        self.entry_hexa.setGeometry(QRect(150, 60, 571, 31))
        self.entry_hexa.setFont(font2)
        self.entry_hexa.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        
        self.toplabel_hexa = QLabel(self.tab_hexa)
        self.toplabel_hexa.setObjectName(u"toplabel_hexa")
        self.toplabel_hexa.setGeometry(QRect(280, 0, 251, 41))
        self.toplabel_hexa.setFont(font1)
        self.toplabel_hexa.setAlignment(Qt.AlignCenter)
        
        self.button_hexa = QPushButton(self.tab_hexa)
        self.button_hexa.setObjectName(u"button_hexa")
        self.button_hexa.setGeometry(QRect(350, 160, 101, 51))
        self.button_hexa.setFont(font3)
        
        self.label_hexa = QLabel(self.tab_hexa)
        self.label_hexa.setObjectName(u"label_hexa")
        self.label_hexa.setGeometry(QRect(20, 60, 121, 31))
        self.label_hexa.setFont(font3)
        self.label_hexa.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        
        self.entry_decimal_hexa = QLineEdit(self.tab_hexa)
        self.entry_decimal_hexa.setObjectName(u"entry_decimal_hexa")
        self.entry_decimal_hexa.setGeometry(QRect(150, 100, 571, 31))
        self.entry_decimal_hexa.setFont(font2)
        self.entry_decimal_hexa.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        
        self.tabWidget.addTab(self.tab_hexa, "")
        self.tab_octal = QWidget()
        self.tab_octal.setObjectName(u"tab_octal")
        
        self.label_decimal_octal = QLabel(self.tab_octal)
        self.label_decimal_octal.setObjectName(u"label_decimal_octal")
        self.label_decimal_octal.setGeometry(QRect(20, 100, 121, 31))
        self.label_decimal_octal.setFont(font3)
        self.label_decimal_octal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        
        self.entry_octal = QLineEdit(self.tab_octal)
        self.entry_octal.setObjectName(u"entry_octal")
        self.entry_octal.setGeometry(QRect(150, 60, 571, 31))
        self.entry_octal.setFont(font2)
        self.entry_octal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        
        self.toplabel_octal = QLabel(self.tab_octal)
        self.toplabel_octal.setObjectName(u"toplabel_octal")
        self.toplabel_octal.setGeometry(QRect(280, 0, 251, 41))
        self.toplabel_octal.setFont(font1)
        self.toplabel_octal.setAlignment(Qt.AlignCenter)
        
        self.button_octal = QPushButton(self.tab_octal)
        self.button_octal.setObjectName(u"button_octal")
        self.button_octal.setGeometry(QRect(350, 160, 101, 51))
        self.button_octal.setFont(font3)
        
        self.label_octal = QLabel(self.tab_octal)
        self.label_octal.setObjectName(u"label_octal")
        self.label_octal.setGeometry(QRect(20, 60, 121, 31))
        self.label_octal.setFont(font3)
        self.label_octal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        
        self.entry_decimal_octal = QLineEdit(self.tab_octal)
        self.entry_decimal_octal.setObjectName(u"entry_decimal_octal")
        self.entry_decimal_octal.setGeometry(QRect(150, 100, 571, 31))
        self.entry_decimal_octal.setFont(font2)
        self.entry_decimal_octal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        
        self.tabWidget.addTab(self.tab_octal, "")
        self.tabWidget.setCurrentIndex(2)


        # QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toplabel_binary.setText(QCoreApplication.translate("MainWindow", u"Binary", None))
        self.entry_binary.setText("")
        self.label_binary.setText(QCoreApplication.translate("MainWindow", u"Binary:", None))
        self.entry_decimal.setText("")
        self.label_decimal.setText(QCoreApplication.translate("MainWindow", u"Decimal:", None))
        self.button_binary.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_binary), QCoreApplication.translate("MainWindow", u"Binary", None))
        self.label_decimal_hexa.setText(QCoreApplication.translate("MainWindow", u"Decimal:", None))
        self.entry_hexa.setText("")
        self.toplabel_hexa.setText(QCoreApplication.translate("MainWindow", u"Hexadecimal", None))
        self.button_hexa.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.label_hexa.setText(QCoreApplication.translate("MainWindow", u"Hex:", None))
        self.entry_decimal_hexa.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hexa), QCoreApplication.translate("MainWindow", u"Hexa", None))
        self.label_decimal_octal.setText(QCoreApplication.translate("MainWindow", u"Decimal:", None))
        self.entry_octal.setText("")
        self.toplabel_octal.setText(QCoreApplication.translate("MainWindow", u"Octadecimal", None))
        self.button_octal.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.label_octal.setText(QCoreApplication.translate("MainWindow", u"Octal:", None))
        self.entry_decimal_octal.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_octal), QCoreApplication.translate("MainWindow", u"Octal", None))
    # retranslateUi

