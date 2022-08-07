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
        self.login_button.clicked.connect(self.login)

    def login(self):
        self.email = self.email_input.text()
        password = self.password_input.text()
        try:
            user = Login.Login(self.email, password)
            test = user.login()
            if test:
                self.feedback_label.setText("Login Successful")
                self.close()
                self.goto_welcome()
                
        except Exception as e:
            self.feedback_label.setText("Invalid Email or Password")
            print(e)
    
    def goto_welcome(self):
        self.hide()
        self.welcome_screen = WelcomeScreen(self.email)
        self.welcome_screen.show()

class WelcomeScreen(QMainWindow):
    def __init__(self, username):
        self.username = username.split('@')[0]
        super(WelcomeScreen, self).__init__()
        loadUi('WelcomeScreen.ui', self)
        self.setWindowTitle("Email Manager | Welcome")
        self.welcome_label.setText(f"Welcome {self.username}")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginScreen()
    window.show()
    sys.exit(app.exec_())
