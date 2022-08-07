import sys
import Login
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow

class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi('LoginScreen.ui', self)
        self.setWindowTitle("Email Manager | Login")

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        try:
            user = Login.Login(email, password)
            test = user.login()
            if test:
                self.status_label.setText("Login Successful")
        except Exception as e:
            self.status_label.setText("Invalid Email or Password")
            print(e)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginScreen()
    window.show()
    sys.exit(app.exec_())
