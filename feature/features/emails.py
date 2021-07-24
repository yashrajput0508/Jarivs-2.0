import smtplib # Send the email
import pandas as pd
from email.message import EmailMessage
import Speech
import sqlite3


gmail=pd.read_json("feature/features/gmail.json")['gmail']
ID,Password=gmail['gmailID'],gmail['password']


receiver_names=[]
receiver_emails=[]

conn=sqlite3.connect(r"feature/features/gmail_list.db")
cur=conn.cursor()
cur.execute("Select * from gmail")
for i in cur.fetchall():
    receiver_names.append(i[1])
    receiver_emails.append(i[2])
cur.close()

class email:

    def __init__(self):
        self.sp=Speech.speech()
        self.receive=self.receiver()
        self.sender="yasharajput0508@gmail.com"
        self.sub=self.subject()
        self.content=self.text()
        self.send_email()

    def receiver(self):
        receiver_name = ""
        receiver_email = ""
        try:
            self.sp.text_to_speech("tell the receiver name, sir")
            receiver_name=self.sp.speech_to_text().lower()

            while receiver_name not in receiver_names:
                self.sp.text_to_speech("receiver name not found, sir tell me the reciever name")
                receiver_name=self.sp.speech_to_text()
            receiver_email=receiver_emails[receiver_names.index(receiver_name)]

        except Exception as e:
            self.sp.text_to_speech("An error occurs,sir please tell the details again, sir")
            self.receiver()
        self.sp.text_to_speech("Receiver email is ," + receiver_email)
        return receiver_email

    def subject(self):
        sub=""
        try:
            self.sp.text_to_speech("What is the subject, sir")
            sub=self.sp.speech_to_text()
            while sub=="":
                self.sp.text_to_speech("Sir, tell me the subject")
                sub = self.sp.speech_to_text()


        except Exception as e:
            self.sp.text_to_speech("An error occurs,sir please tell the details again, sir")
            self.subject()
        self.sp.text_to_speech("Subject is, "+sub)
        return sub

    def text(self):
        content=""

        try:
            self.sp.text_to_speech("What is the content , sir")
            content=self.sp.speech_to_text()
            while content=="":
                self.sp.text_to_speech("Sir, tell me the content")
                content = self.sp.speech_to_text()

        except Exception as e:
            self.sp.text_to_speech("An error occurs,sir please tell the details again, sir")
            self.subject()

        self.sp.text_to_speech("The content is done, sir")
        return content

    def send_email(self):
        try:
            self.sp.text_to_speech("email has been sending, sir")
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(ID, Password)
            email = EmailMessage()
            email['From'] = self.sender
            email['To'] = self.receive
            email['Subject'] = self.sub
            email.set_content(self.content)
            server.send_message(email)
            server.close()
            self.sp.text_to_speech("email has been send, sir")
        except Exception as e:
            result=""
            while result=="":
                self.sp.text_to_speech("Email not sended, problem occurs, sir")
                self.sp.text_to_speech("can i resend email or not, sir")
                result=self.sp.speech_to_text()
            if result in "resend":
                self.send_email()
            else:
                self.sp.text_to_speech("email has been cancelled, sir")