import os
import string
import random
import sqlite3
import datetime
from argon2 import PasswordHasher

    
class MetaSingleton(type):
    """ Insures only a single connection to the database is available at the time. """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None
    def __init__(self):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.cursor, self.connection = self.connect()
        self.table_name = "Users"
        self.time = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} (user_id int, username TEXT, password TEXT, salt TEXT, created TEXT)")
        
    def connect(self):
        """ Makes sure to make a connection to the database, if no connection is active. """
        if self.connection is None:
            self.connection = sqlite3.connect("UserBank.db")
            self.cursor = self.connection.cursor()
        return self.cursor, self.connection
    
    def get_account(self, username):
        """ Fetches the account from the database. """
        try:
            user_data = self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE username = {username}").fetchone()
            return user_data
        except:
            return False
        
        # self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE username = {username}")
        # if self.cursor.fetchone() is not None:
        #     return self.cursor.fetchone()
        # else:
        #     return False
        
    def save_account(self, username, password, salt):
        """ Saves the account to the database. """
        user_id = self.cursor.execute(f"SELECT MAX(user_id) FROM {self.table_name}").fetchone()[0] + 1
        created = self.time
        self.cursor.execute(f"INSERT INTO {self.table_name} (user_id, username, password, salt, created) VALUES(?,?,?,?,?)", (user_id, username, password, salt, created))
        self.connection.commit()
        print(f"Account {username} created successfully!")


class Hashing(object):
    def __init__(self, password):
        self.password = password
        self.hasher = PasswordHasher()

    def verify_password(self, salt, hashed_password):
        """ Compare new hashed password to old hashed password """
        hashed_pass = self.hashing_process(salt)[0]
        return self.hasher.verify(hashed_pass, hashed_password)
    
    def hashing_process(self, salt=None):
        first_hash = self.hasher.hash(self.password)
        if salt is None:
            salt = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16))
            return [self.hasher.hash(first_hash + salt), salt]
        else:
            return [self.hasher.hash(first_hash + salt), salt]
        