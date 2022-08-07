import os

class SignUp(object):
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.user_id = self.account_count()
    
    def account_count(self):
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                return len(file.readlines()) + 1
        else:
            return 0
        
    def save(self):
        with open("users.txt", "a") as file:
            file.write(f"{self.username},{self.password},{self.user_id}\n")
    
    
    @staticmethod
    def valid_username(username):
        valid = True
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                text = file.readlines()
                for line in text:
                    for user in line.split("\n"):
                        if username == user.split(",")[0]:
                            valid = False
                            return valid
                    
        return valid
