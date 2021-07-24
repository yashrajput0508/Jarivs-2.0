import pyjokes
import Speech

class jokes:
    def __init__(self):
        self.sp=Speech.speech()
    def tell_jokes(self):
        self.sp.text_to_speech(pyjokes.get_joke())