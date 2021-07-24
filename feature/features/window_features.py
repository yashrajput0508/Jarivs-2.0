import os
import Speech

class window:
    def __init__(self):
        self.sp=Speech.speech()

    def shutdown(self):
        res=""
        self.sp.text_to_speech("Do you wish to shutdown your computer, sir ? (yes or no): ")
        res=self.sp.speech_to_text()
        while res=="":
            self.sp.text_to_speech("Sir, can i shutdown your computer ? (yes or no): ")
            res = self.sp.speech_to_text()
        if res=="yes":
            self.sp.text_to_speech("Shutdown computer")
            os.system("shutdown /s /t 1")
        else:
            self.sp.text_to_speech("Shutdown process cancelled")
    def restart(self):
        res = ""
        self.sp.text_to_speech("Do you wish to restart your computer, sir ? (yes or no): ")
        res = self.sp.speech_to_text()
        while res == "":
            self.sp.text_to_speech("Sir, can i restart your computer ? (yes or no): ")
            res = self.sp.speech_to_text()
        if res=="yes":
            self.sp.text_to_speech("restart computer")
            os.system("shutdown /r /t 1")
        else:
            self.sp.text_to_speech("Restart proces cancelled")