import Speech
import datetime
from feature.features import dates,weathers

class wish_me:
    def __init__(self):
        self.sp=Speech.speech()
        self.time=dates.dates()
        self.weather=weathers.weather()
    def wish(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.sp.text_to_speech("Good Morning Sir !")

        elif hour >= 12 and hour < 18:
            self.sp.text_to_speech("Good Afternoon Sir !")

        else:
            self.sp.text_to_speech("Good Evening Sir !")
        try:
            self.time.time()
            self.weather.report()
        except Exception:
            pass

    def introduction(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.sp.text_to_speech("Good Morning Sir !")

        elif hour >= 12 and hour < 18:
            self.sp.text_to_speech("Good Afternoon Sir !")

        else:
            self.sp.text_to_speech("Good Evening Sir !")
        self.sp.text_to_speech("I'm Jarvis, an Artificial Intelligent virtual assistant and I'm here to assist you, sir")
        self.sp.text_to_speech("can you tell me your name, sir")
        name=self.sp.speech_to_text()
        if name=="":
            self.sp.text_to_speech("sorry sir i cannot listen your name")
            self.sp.text_to_speech("nice to meet you sir")
        else:
            self.sp.text_to_speech("nice to meet you"+name)
            self.sp.text_to_speech("how can i help you, sir")