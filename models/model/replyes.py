import json
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import Speech
import random
import pickle
import warnings
warnings.filterwarnings("ignore",category=FutureWarning)

class replyes:
    def __init__(self):

        with open(r"models\model\response.json") as file:
            self.data = json.load(file)
            # load trained model
            self.model = keras.models.load_model(r'models\model\chat_model')

            # load tokenizer object
            with open(r'models\model\tokenizer.pickle', 'rb') as handle:
                self.tokenizer = pickle.load(handle)

            # load label encoder object
            with open(r'models\model\label_encoder.pickle', 'rb') as enc:
                self.lbl_encoder = pickle.load(enc)

    def initiate(self,inp):
            # parameters

            max_len = 20

            if self.tokenizer.texts_to_sequences([inp])!=[[]]:
                result = self.model.predict(keras.preprocessing.sequence.pad_sequences(self.tokenizer.texts_to_sequences([inp]),
                                                                                      truncating='post', maxlen=max_len))
                tag = self.lbl_encoder.inverse_transform([np.argmax(result)])

                for i in self.data['intents']:
                    if i['tag'] == tag:
                        return np.random.choice(i['responses']),max(result[0])*100
            else:
                return ""

