import sys
import Login
from SignUp import SignUp
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow


class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi('Screens/LoginScreen.ui', self)
        self.setWindowTitle("Login")
        self.login_button.clicked.connect(self.login)
        self.signup_button.clicked.connect(self.sign_up)
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
            print(e)
            self.feedback_label.setText(str(e))
    
    def sign_up(self):
        self.close()
        self.signup_screen = SignUpScreen()
        self.signup_screen.show()
    
    def exit(self):
        sys.exit()


class WelcomeScreen(QMainWindow):
    def __init__(self, username):
        self.username = username.split('@')[0]
        super(WelcomeScreen, self).__init__()
        loadUi('Screens/WelcomeScreen.ui', self)
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
        loadUi('Screens/SignUpScreen.ui', self)
        self.setWindowTitle("Sign Up")
        self.create_button.clicked.connect(self.sign_up)
        self.exit_button.clicked.connect(self.exit)
        self.login_button.clicked.connect(self.login)
        
    def sign_up(self):
        if SignUp.valid_username(self.username_input.text()):
            if self.password_input.text() == self.confirm_password_input.text():
                self.username = self.username_input.text()
                self.password = self.password_input.text()
                user = SignUp(self.username, self.password)
                user.save()
                self.close()
                self.login_screen = LoginScreen()
                self.login_screen.show()
            else:
                self.feedback_label.setText("Passwords do not match")
        else:
            self.feedback_label.setText("Invalid Username")
            
    
    def login(self):
        self.close()
        self.login_screen = LoginScreen()
        self.login_screen.show()
    
    def exit(self):
        sys.exit()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginScreen()
    window.show()
    sys.exit(app.exec_())
