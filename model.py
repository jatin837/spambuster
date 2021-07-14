from sklearn.feature_extraction.text import CountVectorizer
import glob
import os
import numpy as np
from helpers import get_contents_from_file
from processors import clean_text
from time import sleep

DELAY: float = 0.001

class Model(object):
    def __init__(self, path, stop_words="english", max_features=1000, max_df=0.5, min_df=2):
        self.path = path
        self.cv = CountVectorizer(
                stop_words=stop_words,
                max_features=max_features, 
                max_df=max_df, 
                min_df=min_df
            )
    
    def fit(self):
        raw_data = self.load_data()
        self.features = self.cv.fit_transform(raw_data)
        self.store()
    
    def store(self):
        with open("feature_names.txt", 'w') as f:
            for name in self._get_feature_names():
                f.write(name + "\n")

        np.save("feature_matrix.npy", self._get_feature_matrix())
        np.save("labels.npy", self.labels)


    def load_data(self):
        emails = []
        labels = []
        spam_file_path = f'{self.path}/spam/'
        for filename in glob.glob(os.path.join(spam_file_path, '*.txt')):
            sleep(DELAY)
            emails.append(get_contents_from_file(filename))
            labels.append(1)
            print(f"...loading {filename}...")

        ham_file_path = f'{self.path}/ham/'
        for filename in glob.glob(os.path.join(ham_file_path, '*.txt')):
            sleep(DELAY)
            emails.append(get_contents_from_file(filename))
            labels.append(0)
            print(f"...loading {filename}...")

        emails_cleaned = []
        for email in emails:
            sleep(DELAY)
            print(f"...cleaning...")
            emails_cleaned.append(clean_text(email))

        print(f"...DONE...")

        self.labels = np.array(labels)
        return emails_cleaned

    def cache(self):
        self.labels = np.load("labels.npy")
        self.feature_matrix = np.load("feature_matrix.npy")
        with open("feature_names.txt", 'r') as f:
            self.feature_names = f.read().split("\n")
    
    def _get_feature_matrix(self):
        self.feature_matrix = self.features.toarray()
        return self.feature_matrix

    def _get_feature_names(self):
        self.feature_names = self.cv.get_feature_names()
        return self.feature_names

