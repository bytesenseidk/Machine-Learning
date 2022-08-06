# from PySide2.QtCore import QCoreApplication, QMetaObject, QRect, Qt
# from PySide2.QtGui import QFont
# from PySide2.QtWidgets import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Email Manager | Login")
        self.initUi()
        
    def initUi(self):
        self.top_label = QtWidgets.QLabel(self)
        self.top_label.setObjectName("top_label")
        self.top_label.setGeometry(QtCore.QRect(0, 0, 800, 100))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.top_label.setFont(font)
        self.top_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.top_label.setStyleSheet("")
        self.top_label.setAlignment(QtCore.Qt.AlignCenter)
        self.top_label.setText("Email Manager")
        
        
        self.username_label = QtWidgets.QLabel(self)
        self.username_label.setObjectName("username_label")
        self.username_label.setGeometry(QtCore.QRect(350, 120, 100, 30))
        label_font = QtGui.QFont()
        label_font.setPointSize(14)
        label_font.setBold(True)
        label_font.setWeight(75)
        self.username_label.setFont(label_font)
        self.username_label.setStyleSheet("")
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setText("Email")
        
        self.username_input = QtWidgets.QLineEdit(self)
        self.username_input.setObjectName("username_input")
        self.username_input.setGeometry(QtCore.QRect(200, 150, 400, 30))
        input_font = QtGui.QFont()
        input_font.setPointSize(14)
        input_font.setBold(True)
        input_font.setWeight(50)
        self.username_input.setFont(input_font)
        self.username_input.setStyleSheet("")
        self.username_input.setMaxLength(100)
        self.username_input.setPlaceholderText("")
        
        self.password_label = QtWidgets.QLabel(self)
        self.password_label.setObjectName("password_label")
        self.password_label.setGeometry(QtCore.QRect(345, 200, 110, 30))
        self.password_label.setFont(label_font)
        self.password_label.setStyleSheet("")
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setText("Password")

        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setObjectName("password_input")
        self.password_input.setGeometry(QtCore.QRect(200, 230, 400, 30))
        self.password_input.setFont(input_font)
        self.password_input.setMaxLength(100)
        self.password_input.setPlaceholderText("")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.signin_button = QtWidgets.QPushButton(self)
        self.signin_button.setObjectName("signin_button")
        self.signin_button.setGeometry(QtCore.QRect(350, 280, 100, 50))
        font3 = QtGui.QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.signin_button.setFont(font3)
        self.signin_button.setText("Login")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
