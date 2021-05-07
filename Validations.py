import os
import hashlib


class HashGenerator(object):
    def __init__(self, file):
        self.file = file
        self.BUF_SIZE = 65536
        try:
            drive = str(file.split("/")[0])
            file_name = str(file.split("/")[-1])
            file_path = os.path.join(file.strip(file_name))
            if str(file_path.split("/")[0]) != drive:
                file_path = str(drive.strip(":") + file_path)
            os.chdir(file_path)
        except Exception as E:
            print(E)

    def generate(self):
        


class MD5(HashGenerator):



    def hash_generator(self):
        drive = str(self.check_file.split("\\")[0])
        file_name = str(self.check_file.split("\\")[-1])
        file_path = os.path.join(self.check_file.strip(file_name))
        if str(file_path.split("\\")[0]) != drive:
            file_path = str(drive.strip(":") + file_path)
        os.chdir(file_path)
        with open(file_name, 'rb') as file:
            while True:
                data = file.read(self.BUF_SIZE)
                if not data:
                    break
                self.md5.update(data)
                self.sha1.update(data)
                self.sha256.update(data)
