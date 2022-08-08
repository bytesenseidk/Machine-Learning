import os
import sys
import random
import sqlite3
import datetime
from cryptography.fernet import Fernet


class PasswordSecurity(object):
    def __init__(self):
        pass
    

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
        """ Changes directory to script_path, creates a connection to the database if it exists, if not, it creates a new database.
        Creates a single table inside your database file called 'Table_1' if it dosen't exists already."""
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.cursor, self.connection = self.connect()
        
        self.table_name = "Table_1"
        self.time = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} (column_1 TEXT, column_2 INT, column_3 REAL)")
        
        
    def connect(self):
        """ Makes sure to make a connection to the database, if no connection is active. """
        if self.connection is None:
            self.connection = sqlite3.connect("Database_file.db")
            self.cursor = self.connection.cursor()
        return self.cursor, self.connection
    
    
    def insert_data(self):
        """ Inserts data into our table. """
        column_1 = self.time
        column_2 = 45
        column_3 = 45.77
        self.cursor.execute(f"INSERT INTO {self.table_name} (column_1, column_2, column_3) VALUES(?,?,?)", (column_1, column_2, column_3))
        self.connection.commit()

        
    def read_data(self):
        """ Reads data from our table. """
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        for row in self.cursor.fetchall():
            print(row)


class Hashing(object):
    def __init__(self, password):
        self.password = password
        
    def hash_password(self):
        """
        Argon2 hash password.
        return hashed password.
        """
        pass

    def verify_password(self, hashed_password):
        """
        Argon2 hash password.
        Compare new hashed password to old hashed password.
        return comparison.
        """
        pass


class Salting(object):
    def __init__(self, password):
        self.password = password
        
    def generate_salt(self):
        """ Generate a random salt. (Random set of characters) """
        pass
    
    def salt(self):
        """ 
        Append salt to a hashed password.
        Return the salted password.
        """
        pass


class Peppering(object):
    def __init__(self):
        self.current_pepper = self.locate_pepper()
        self.pepper_rotation_check()
        
    def locate_pepper(self):
        """
        Locate newest pepper in db (a cryptographically random key).
        Return pepper.
        """
        pass
    
    def pepper_rotation_check(self):
        """
        Check if the pepper has been rotated.
        If not, rotate the pepper.
        """
        pass
    
    def pepper_rotation(self):
        """
        Encrypt the pepper with a new pepper.
        Encrypt the pepper with the old pepper.
        Store the new pepper in the database.
        Store the old pepper in the database.
        """
        pass


class Encryption(object):
    def __init__(self, file):
        self.file = file
        try:
            self.key = self.key_reader()
        except:
            self.key_generator()
            self.key = self.key_reader()
            
    def key_reader(self):
        with open("keyfile.txt", "rb") as filekey:
            key = filekey.read()
        return key
    
    def key_generator(self):
        key = Fernet.generate_key()
        with open("keyfile.txt", "wb") as filekey:
            filekey.write(key)
    
    def encryption(self):
        with open("keyfile.txt", "rb") as filekey:
            key = filekey.read()
        
        fernet = Fernet(self.key)
        with open(self.file, "rb") as file:
            origional = file.read()
        
        encrypted = fernet.encrypt(origional)
        with open(self.file, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
    
    
    def decryption(self):
        fernet = Fernet(self.key)
        with open(self.file, "rb") as enc_file:
            encrypted = enc_file.read()
        
        decrypted = fernet.decrypt(encrypted)
        with open(self.file, "wb") as dec_file:
            dec_file.write(decrypted)  
    

if __name__ == "__main__":
    temp = PasswordSecurity()
    