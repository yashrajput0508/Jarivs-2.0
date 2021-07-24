"""It is the backend model of jarvis"""

import Speech
import warnings
from feature import _features_controller
from models import _model_controller
import requests
import time
import multiprocessing
warnings.filterwarnings("ignore",category=FutureWarning)
import speech_recognition as sr
import Database

# Jarvis class
class jarvis:
    def __init__(self):
        self.sp = Speech.speech()
        self.features= _features_controller
        self.model= _model_controller.models()
        self.exits=False
        self.active=True
        self.features.features("@wish","@wish")
        self.database=Database
    def runjarvis(self):
        """here we run the jarvis"""
        # convert speech to text and text to speech
        while True:
            if self.exits==True:
                break
            input=self.sp.speech_to_text()
            try:
                self.setreply(input)
            except Exception:
                continue

    def setreply(self,input):
        # It replay the answer of your qutestion
        reply,pred=self.model.model_reply(input)
        self.database.updatedatabase(input,reply)
        if self.active==True:
            try:
                input=input.split(" ")
                input.remove("jarvis")
                input=" ".join(input)
            except Exception:
                pass
            if "#sleep" in reply:
                self.active=False
                self.sp.text_to_speech("Sleep mode active, sir")
            elif "$" in reply:
                self.update_model()
            elif "@" in reply:
                self.features.features(input,reply)
            else:
                self.sp.text_to_speech(reply)

        elif self.active==False and "wake up" in input:
            self.active=True
            self.sp.text_to_speech(reply)

    def update_model(self):
        #"It update your jarvis model"
        self.model.train_model()

    def quit(self): # quit the program
        self.exits=True


