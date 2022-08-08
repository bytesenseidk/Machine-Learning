import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
from UserBank import *


class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi('Screens/LoginScreen.ui', self)
        screens.setWindowTitle("Login System | Login")
        self.login_button.clicked.connect(self.login)
        self.signup_button.clicked.connect(self.sign_up)
        self.exit_button.clicked.connect(self.exit)
        self.database = Database()
        
    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        user_data = self.database.get_account(username)
        if user_data["username"] == username and self.database.verify_password(user_data["password"], password):
            self.close()
            self.welcome_screen = WelcomeScreen(username)
            screens.addWidget(self.welcome_screen)
            screens.setCurrentIndex(screens.currentIndex() + 1)
        else:
            self.feedback_label.setText("Invalid username or password")
    
    def sign_up(self):
        self.close()
        self.signup_screen = SignUpScreen()
        screens.addWidget(self.signup_screen)
        screens.setCurrentIndex(screens.currentIndex() + 1)
    
    def exit(self):
        self.closeDb()
        sys.exit()
        
    def closeDb(self):
        self.database.cursor.close()
        self.database.connection.close()


class WelcomeScreen(QMainWindow):
    def __init__(self, username):
        self.username = username.split('@')[0]
        super(WelcomeScreen, self).__init__()
        loadUi('Screens/WelcomeScreen.ui', self)
        screens.setWindowTitle("Login System | Welcome")
        self.welcome_label.setText(f"Welcome {self.username}")
        self.logout_button.clicked.connect(self.logout)
        self.exit_button.clicked.connect(self.exit)
        self.database = Database()
        
    def logout(self):
        self.close()
        self.login_screen = LoginScreen()
        screens.addWidget(self.login_screen)
        screens.setCurrentIndex(screens.currentIndex() + 1)
              
    def exit(self):
        self.closeDb()
        sys.exit()
    
    def closeDb(self):
        self.database.cursor.close()
        self.database.connection.close()
        
class SignUpScreen(QMainWindow):
    def __init__(self):
        super(SignUpScreen, self).__init__()
        loadUi('Screens/SignUpScreen.ui', self)
        screens.setWindowTitle("Login System | Sign Up")
        self.create_button.clicked.connect(self.sign_up)
        self.login_button.clicked.connect(self.login)
        self.exit_button.clicked.connect(self.exit)
        self.database = Database()   
        
    def sign_up(self):
        if len(self.username_input.text()) > 4 and len(self.password_input.text()) > 4:
            if self.password_input.text() == self.confirm_password_input.text():    
                username = self.username_input.text()
                password = self.password_input.text()
                user_data = self.database.get_account(username)
                if user_data["username"] is None:
                    self.database.save_account(username, password)
                    self.close()
                    self.login_screen = LoginScreen()
                    screens.addWidget(self.login_screen)
                    screens.setCurrentIndex(screens.currentIndex() + 1)
                else:
                    self.feedback_label.setText("Username already exists!")
            else:
                self.feedback_label.setText("Passwords do not match")
        else:
            self.feedback_label.setText("Username and Password must be at least 5 characters")
            
    def login(self):
        # self.closeDb()
        self.close()
        self.login_screen = LoginScreen()
        screens.addWidget(self.login_screen)
        screens.setCurrentIndex(screens.currentIndex() + 1)
    
    def exit(self):
        self.closeDb()
        sys.exit()
        
    def closeDb(self):
        self.database.cursor.close()
        self.database.connection.close()
    
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    screens = QtWidgets.QStackedWidget()
    login_window = LoginScreen()
    
    screens.addWidget(login_window)
    screens.setFixedHeight(600)
    screens.setFixedWidth(800)
    screens.show()
    sys.exit(app.exec_())