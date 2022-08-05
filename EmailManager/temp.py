class Login(object):
    mail_servers = {
        "gmail": [["smtp.gmail.com", 587], ["imap.gmail.com", 993]],
        "aol": [["smtp.aol.com", 587], ["imap.aol.com", 993]],
        "outlook": [["smtp-mail.outlook.com", 587], ["imap-mail.outlook.com", 993]],
        "bt-connect": [["smtp.btconnect.com", 25], ["imap4.btconnect.com", 143]],
        "office365": [["smtp.office365.com", 587], ["outlook.office365.com", 993]],
        "yahoo": [["smtp.mail.yahoo.com", 465], ["imap.mail.yahoo.com", 993]],
        "yahoo-plus": [["plus.smtp.mail.yahoo.com", 465], ["plus.imap.mail.yahoo.com", 993]],
        "yahoo-uk": [["smtp.mail.yahoo.co.uk", 465], ["imap.mail.yahoo.co.uk", 993]],
        "yahoo-europe": [["smtp.mail.yahoo.com", 465], ["imap.mail.yahoo.com", 993]],
        "t-online": [["securesmtp.t-online.de", 587], ["secureimap.t-online.de", 993]],
        "verizon": [["outgoing.verizon.net", 587], ["incoming.verizon.net", 143]]
        # Find additional mail servers at https://www.systoolsgroup.com/imap/
    }
    def __init__(self, email, password):
        self.email = email
        self.password = password
        try:
            self.smtp_server, self.smtp_port = Login.mail_servers[email.split("@")[1].split(".")[0]][0]
            self.imap_server, self.imap_port = Login.mail_servers[email.split("@")[1].split(".")[0]][1]
        except KeyError:
            print("Invalid email address")
        
    def __str__(self):
        data = "\n"
        for key, value in self.__dict__.items():
            data += f"{key}: \t{value}\n"
        return data
    
    
if __name__ == "__main__":
    user = Login("some_mail@gmail.com", "some_password")
    print(user)
    
