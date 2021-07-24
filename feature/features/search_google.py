import wikipedia
import webbrowser as wb
import Speech

class searching:
    def __init__(self):
        self.text=""
        self.sp=Speech.speech()

    def find_wiki(self):
        while self.text=="":
            self.sp.text_to_speech("What should i search, sir")
            self.text=self.sp.speech_to_text()
        self.sp.text_to_speech("Searching on wikipedia, sir")
        self.sp.text_to_speech(self.search(self.text))

    def find_google(self):
        while self.text == "":
            self.sp.text_to_speech("What should i search, sir")
            self.text = self.sp.speech_to_text()
        self.sp.text_to_speech("Searching on google, sir")
        self.searchgoogle(self.text)
        self.sp.text_to_speech(self.search(self.text))

    def search(self,text):
        try:
            result = wikipedia.summary(text, sentences=2)
        except Exception as e:
            result = "Cannot search on wikipedia, sir"
        return result

    def searchgoogle(self,text):
        wb.open('https://www.google.com/search?q=' + text)