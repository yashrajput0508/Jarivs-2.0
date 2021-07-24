import speech_recognition as sr  # Convert speech to text
import pyttsx3 # convert text to speech
import numpy as np

class speech:
    def __init__(self):
        self.mode = False
        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()

    def speech_to_text(self): # This convert speech to text
        r = sr.Recognizer()

        with sr.Microphone() as source:

            print("Listening...")
            f = open(r'jarvis_update', 'w')
            f.write("Listening...")
            f.close()
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            f = open(r'jarvis_update', 'w')
            f.write("Recognizing...")
            f.close()
            query = r.recognize_google(audio, language='en-in')

        except:
            return ""

        return query.lower()


    def speak(self,voice): # This speak the words which i tell
        self.engine.say(voice)
        self.engine.runAndWait()

    def text_to_speech(self,text): # this convert text to speech
        try:
            self.engine.setProperty("rate",180)
            voice=self.engine.getProperty("voices")
            self.switchmode(voice)
            self.speak(text)
        except Exception:
            pass

    def switchmode(self,voice): #Convert the mode Jarvis to Alis
        if self.mode==False:
            self.engine.setProperty("voice", voice[2].id)
        else:
            self.engine.setProperty("voice",voice[1].id)
