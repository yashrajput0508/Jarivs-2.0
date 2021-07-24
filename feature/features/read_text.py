import clipboard
import Speech
"""It read the copied text"""
class read:
    def __init__(self):
        self.sp=Speech.speech()
    def readtext(self):
        text=clipboard.paste()
        try:
            self.sp.text_to_speech(text)
        except Exception as e:
            self.sp.text_to_speech("Cannot read the text ,sir")