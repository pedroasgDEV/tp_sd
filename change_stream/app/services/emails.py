import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.config import send_email as send
from app.config import recv_email as recv


class SendEmail:
    def __init__(self, recv_email):
        #Config Menssage
        self.__recv_email = recv_email
        self.__send_email = send["EMAIL"]
        self.__send_password = send["PASSWORD"]
        self.__email = MIMEMultipart()
        self.__email["From"] = self.__send_email 
        self.__email["To"] = self.__recv_email
        
        #Config server
        self.__server = smtplib.SMTP('smtp.gmail.com', 587)
    
    def send(self, change, change_type):
        self.__email["Subject"] = "MongoDB Change Notification: " + change_type
        body = "A change was detected in the MongoDB collection:\n\n" + change
        self.__email.attach(MIMEText(body, 'plain'))
        
        self.__server.starttls()
        self.__server.login(self.__send_email, self.__send_password)
        mail = self.__email.as_string()
        self.__server.sendmail(self.__send_email, self.__recv_email, mail)
        self.__server.quit()
        
email = SendEmail(recv["EMAIL"])
email.send("HELLO WOLRD", "TEST")
        
        
        
        
