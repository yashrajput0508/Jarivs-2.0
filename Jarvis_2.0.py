import sys
import threading

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from gui.default import *
import requests,Speech,time
import Jarvis
import multiprocessing
import settings_gui


"""It is used for checking internet connection of your computer"""
class jarvis_copy:
    def __init__(self):
        pass

    def test_connection(self):
        try:
            requests.get('https://www.google.com/').status_code
            return "connected"
        except:
            return "not"

    def start(self):
        
        while True:
            ans = self.test_connection()
            if ans == "connected":
                break
            else:
                Speech.speech().text_to_speech("Internet is not connected, sir")
                time.sleep(5)

        self.jarvis = Jarvis.jarvis()
        self.jarvis.runjarvis()

"It is the main frame access all the frames"
class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.p=None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.play.hide()
        self.ui.pause.show()
        self.movie = QtGui.QMovie(r"gui/images/sound.gif")
        self.ui.listener.setMovie(self.movie)
        self.movie.start()
        self.ui.play.clicked.connect(self.pause)
        self.ui.pause.clicked.connect(self.play)
        self.ui.setting.clicked.connect(self.setting)
        self.ui.result.setText("...Jarvis...")
        self.jarvis_copy=jarvis_copy()

    # It play the jarvis
    def play(self):
        self.ui.pause.hide()
        self.ui.play.show()
        self.first=multiprocessing.Process(target=self.jarvis_copy.start)
        self.thread=True
        self.second=threading.Thread(target=self.edit_text)
        self.first.start()
        self.second.start()

    # IT show the response infromation such that jarvis listening or recognizing
    def edit_text(self):
        while self.thread:
            f = open(r'jarvis_update', 'r')
            text = f.readline()
            if text!=self.ui.result.text():
                self.ui.result.setText(text)
            f.close()
            time.sleep(1)

    # It stop the jarvis program when you stopped
    def pause(self):
        self.ui.result.setText("...Stopped...")
        self.ui.play.hide()
        self.ui.pause.show()
        self.first.kill()
        self.thread=False
        f = open(r'jarvis_update', 'w')
        f.write("...Conecting...")

    # It open the login model when you need
    def setting(self):
        if self.p==None:
            self.p = settings_gui.login(w)
            self.p.setWindowIcon(QIcon(r"gui/images/my.png"))
            self.p.show()
        elif self.p.isHidden()==True:
            self.p = settings_gui.login(w)
            self.p.setWindowIcon(QIcon(r"gui/images/my.png"))
            self.p.show()

    # It kills the jarvis process when close gui
    def closeEvent(self,event):
        if self.close():
            try:
                self.first.kill()
            except Exception:
                pass

if __name__=="__main__":
    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    w = MyForm()
    w.setWindowTitle("Jarvis_2.0")
    w.setWindowIcon(QIcon(r"gui/images/my.png"))
    w.show()
    sys.exit(app.exec_())
