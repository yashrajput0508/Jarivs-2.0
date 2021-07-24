import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings("ignore",category=FutureWarning)



class train_data:
    def __init__(self):
        self.training_sentences = []
        self.training_labels = []
        self.labels = []
        self.responses = []
        self.data=""
        self.load_json()

    def initate(self):
        self.training()

    def load_json(self):
        with open(r'models\model\response.json') as file:
            self.data = json.load(file)
        for intent in self.data['intents']:
            for pattern in intent['patterns']:
                self.training_sentences.append(pattern.lower())
                self.training_labels.append(intent['tag'])
            self.responses.append(intent['responses'])

            if intent['tag'] not in self.labels:
                self.labels.append(intent['tag'])

    def training(self):

        num_classes = len(self.labels)

        lbl_encoder = LabelEncoder()
        lbl_encoder.fit(self.training_labels)
        training_labels = lbl_encoder.transform(self.training_labels)

        vocab_size = 1000
        embedding_dim = 16
        max_len = 20
        oov_token = "<OOV>"

        tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
        tokenizer.fit_on_texts(self.training_sentences)
        word_index = tokenizer.word_index
        sequences = tokenizer.texts_to_sequences(self.training_sentences)
        padded_sequences = pad_sequences(sequences, truncating='post', maxlen=max_len)

        print(self.training_labels)
        print(sequences)
        model = Sequential()
        model.add(Embedding(vocab_size, embedding_dim, input_length=max_len))
        model.add(GlobalAveragePooling1D())
        model.add(Dense(16, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(num_classes, activation='softmax'))

        model.compile(loss='sparse_categorical_crossentropy',
                      optimizer='adam', metrics=['accuracy'])

        model.summary()


        epochs = 500
        history = model.fit(padded_sequences, np.array(training_labels), epochs=epochs)

        # to save the trained model
        model.save(r"models\model\chat_model")

        import pickle

        # to save the fitted tokenizer
        with open(r'models\model\tokenizer.pickle', 'wb') as handle:
            pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

        # to save the fitted label encoder
        with open(r'models\model\label_encoder.pickle', 'wb') as ecn_file:
            pickle.dump(lbl_encoder, ecn_file, protocol=pickle.HIGHEST_PROTOCOL)

"""
['None', 'jarvis', 'greet', 'greeting', 'greeting', 'greeting', 'greeting', 'greeting', 'greeting', 'goodbye', 'goodbye', 'goodbye', 'fine', 'thanks', 'thanks', 'thanks', 'thanks', 'about', 'about', 'about', 'name', 'name', 'name', 'help', 'help', 'help', 'help', 'help', 'help', 'help2', 'time', 'time', 'time', 'time', 'time', 'time', 'covid', 'covid', 'reading', 'reading', 'screenshot', 'screenshot', 'send_email', 'joke', 'joke', 'wikipedia', 'google', 'open', 'update', 'close', 'shutdown', 'shutdown', 'shutdown', 'restart', 'restart', 'restart', 'introduction', 'introduction']
[[37], [15], [38, 39], [40], [41], [5, 42, 43], [16], [44], [16, 15], [45], [46, 2, 47], [48], [49, 9, 2], [17], [50, 2], [51, 52], [17, 18, 4, 10], [19, 9, 2], [3, 9, 2], [19, 2, 9], [3, 5, 20, 21], [3, 53, 11, 54, 2], [55, 20, 21], [56, 2, 10, 7], [57, 7, 8, 58, 22], [23, 2, 10], [11, 24, 8, 25], [11, 24, 8, 10], [25, 7, 22], [3, 23, 2, 59, 18, 7], [6], [26, 6], [3, 5, 4, 6], [3, 5, 4, 26, 6], [3, 5, 4, 60, 6], [3, 5, 4, 6], [27, 28, 12], [3, 5, 4, 27, 28, 12], [29, 4, 30], [29, 4, 61, 30], [62, 8, 31], [31], [63, 64], [32], [65, 7, 8, 32], [33, 34, 66], [33, 34, 67], [68], [12, 69], [70], [13], [13, 35], [13, 36], [14], [14, 35], [14, 36], [71], [72, 73]]
"""