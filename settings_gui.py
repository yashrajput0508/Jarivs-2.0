from PyQt5.QtGui import QStandardItemModel, QIcon

from gui.Login_form import *
from gui.settings import *
from PyQt5.QtWidgets import QDialog, QListWidgetItem, QListWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import sys
import pandas as pd
import sqlite3
receiver_names=[]
receiver_emails=[]
names=[]
numbers=[]

conn=sqlite3.connect(r"feature/features/gmail_list.db")
cur=conn.cursor()
cur.execute("Select * from gmail")

for i in cur.fetchall():
    receiver_names.append(i[1])
    receiver_emails.append(i[2])
conn.close()

conn=sqlite3.connect(r"feature/features/whatsapp_list.db")
cur=conn.cursor()
cur.execute("Select * from number")

for i in cur.fetchall():
    names.append(i[0])
    numbers.append(i[1])
conn.close()


class settings(QMainWindow):
    def __init__(self,parent):
        super(settings,self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.tc=QListWidget()
        self.ui.update.clicked.connect(self.update_email)
        self.ui.update_2.clicked.connect(self.update_time_table)
        self.ui.update_3.clicked.connect(self.update_whatsapp)
        self.ui.listWidget_2.addItems(receiver_names)
        self.ui.listWidget_3.addItems(receiver_emails)
        self.ui.listWidget_5.addItems(names)
        self.ui.listWidget_6.addItems(numbers)

    def update_email(self):
        name=self.ui.lineEdit.text()
        id=self.ui.lineEdit_2.text()
        self.ui.listWidget_2.addItem(name)
        self.ui.listWidget_3.addItem(id)
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")

        conn = sqlite3.connect(r"feature/features/gmail_list.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO gmail(name,id) VALUES(?,?);", (name, id))
        conn.commit()
        conn.close()

    def update_time_table(self):
        pass

    def update_whatsapp(self):
        name = self.ui.lineEdit_3.text()
        number = self.ui.lineEdit_4.text()
        self.ui.listWidget_5.addItem(name)
        self.ui.listWidget_6.addItem(number)
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")

        conn = sqlite3.connect(r"feature/features/whatsapp_list.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO number VALUES(?,?);", (name, number))
        conn.commit()
        conn.close()

class login(QDialog):
    def __init__(self,parent):
        super(login,self).__init__(parent)
        self.parent=parent
        self.w=None
        self.ui=Ui_Login()
        self.ui.setupUi(self)
        self.name="yash"
        self.password="9410243433"
        self.ui.button.clicked.connect(self.login)

    def login(self):
        if str(self.ui.id_name.text()).lower()==str(self.name) and str(self.ui.password_name.text())==str(self.password):

            if self.w is None :
                self.w = settings(self.parent)
                self.w.setWindowIcon(QIcon(r"gui/images/my.png"))
                self.w.show()
            else:
                self.w.close()  # Close window.
                self.w = None
            self.close()
        elif str(self.ui.id_name).lower()==str(self.name):
            self.ui.update.setText("Wrong Password")
        else:
            self.ui.update.setText("Wrong Id")


