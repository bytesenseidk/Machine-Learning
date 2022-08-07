import sys
import Login
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow


class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi('LoginScreen.ui', self)
        self.setWindowTitle("Login")
        self.login_button.clicked.connect(self.login)
        self.sign_up_button.clicked.connect(self.sign_up)
        self.exit_button.clicked.connect(self.exit)

    def login(self):
        self.username = self.username_input.text()
        self.password = self.password_input.text()
        try:
            user = Login.Login(self.username, self.password)
            if user.valid_user():
                self.close()
                self.welcome_screen = WelcomeScreen(self.username)
                self.welcome_screen.show()
            else:
                self.feedback_label.setText("Invalid Username or Password")
        except Exception as e:
            self.feedback_label.setText(e)
    
    def sign_up(self):
        self.close()
        self.sign_up_screen = SignUpScreen()
        self.sign_up_screen.show()
    
    def exit(self):
        sys.exit()


class WelcomeScreen(QMainWindow):
    def __init__(self, username):
        self.username = username.split('@')[0]
        super(WelcomeScreen, self).__init__()
        loadUi('WelcomeScreen.ui', self)
        self.setWindowTitle("Email Manager | Welcome")
        self.welcome_label.setText(f"Welcome {self.username}")
        self.logout_button.clicked.connect(self.logout)
        self.exit_button.clicked.connect(self.exit)
        
    def logout(self):
        self.close()
        self.login_screen = LoginScreen()
        self.login_screen.show()
        
    def exit(self):
        sys.exit()
        
class SignUpScreen(QMainWindow):
    def __init__(self):
        super(SignUpScreen, self).__init__()
        loadUi('SignUpScreen.ui', self)
        self.setWindowTitle("Sign Up")
        self.create_button.clicked.connect(self.sign_up)
        self.exit_button.clicked.connect(self.exit)
        
    def sign_up(self):
        pass
    
    def exit(self):
        sys.exit()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginScreen()
    window.show()
    sys.exit(app.exec_())
