from models.model import modeling, replyes
import Speech

class models:
    def __init__(self):
        self.sp=Speech.speech()
        self.training= modeling.train_data()
        self.reply= replyes.replyes()

    def train_model(self):
        self.sp.text_to_speech("updating the model, sir")
        self.training.initate()
        self.reply = replyes.replyes()
        self.sp.text_to_speech("model updated, sir")

    def model_reply(self,input):
        return self.reply.initiate(input)
