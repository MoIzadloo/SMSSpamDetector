import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
import pickle
import re
import time

class SMSSpamDetection(MRJob):
    OUTPUT_PROTOCOL = JSONValueProtocol
    def preprocess_message(self, message):
        message = message.lower()
        message = re.sub(r'[^\w\s]', '', message)
        message = re.sub(r'\s+', ' ', message)
        return message

    def mapper_init(self):
        data = pd.read_csv('spam.csv', encoding = "ISO-8859-1")
        with open('model.pkl', 'rb') as f:
            self.model = pickle.load(f)
        messages = data['v2']
        preprocessed_messages = [self.preprocess_message(message) for message in messages]
        self.vectorizer = CountVectorizer()
        self.vectorizer.fit_transform(preprocessed_messages)

    def mapper(self, _, message):
        current_time = time.time()
        preprocessed_message = self.preprocess_message(message)
        features = self.vectorizer.transform([preprocessed_message])
        proba = self.model.predict_proba(features).tolist()
        yield "messages", [list(proba[0]), current_time, message]

    def reducer(self, key, values):
        output = []
        for value in values: 
            record = value
            current_time = time.time()
            label = "spam"
            proba = record[0]
            mapTime = record[1]
            if proba[0] < proba[1]:
                label = "spam"
            else:
                label = "ham"
            output.append({
                "message": record[2],
                "label": label,
                "time": "{0:.2f}s".format(current_time - mapTime)
            })
        yield key, output
        
        

if __name__ == '__main__':
    SMSSpamDetection.run()