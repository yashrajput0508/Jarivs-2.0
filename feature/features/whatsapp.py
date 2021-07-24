import webbrowser as web
import time
import keyboard
import pyautogui
import Speech
import sqlite3
names=[]
numbers=[]

conn=sqlite3.connect(r"feature/features/whatsapp_list.db")
cur=conn.cursor()
cur.execute("Select * from number")
for i in cur.fetchall():
    names.append(i[0])
    numbers.append(i[1])
cur.close()

class whatsapps:
    def __init__(self):
        self.sp=Speech.speech()
        self.name=""
        self.number=""
        self.message=""

    def send_message(self):
        self.sp.text_to_speech("Tell me receiver name, sir")
        self.name=self.sp.speech_to_text()
        while self.name=="":
            self.sp.text_to_speech("Sir please, Tell me receiver name")
            self.name = self.sp.speech_to_text()
        if self.name not in names:
            self.sp.text_to_speech("Reciever number not found in list, please add the number sir")
        else:
            self.sp.text_to_speech("Tell me message, sir")
            self.message = self.sp.speech_to_text()
            self.sp.text_to_speech("Sending message, sir")
            try:
                self.whatsapp(numbers[names.index(self.name)],self.message)
                self.sp.text_to_speech("Message has been send, sir")
            except Exception:
                self.sp.text_to_speech("Problem occurs, sir")

    def whatsapp(self,number,message):
        numb = '+91' + number
        open_chat = "https://web.whatsapp.com/send?photo=" + numb + "&text=" + message
        web.open(open_chat)
        time.sleep(15)
        keyboard.press('enter')

    def Whatspp_Grp(self,group_id , message):
        open_chat = "https://web.whatsapp.com/accept?code=" + group_id
        web.open(open_chat)
        time.sleep(15)
        pyautogui.click(x=754 , y =696)
        keyboard.write(message)
        time.sleep(1)
        keyboard.press('enter')

