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
        self.raw_data = []
        self.cv = CountVectorizer(
                stop_words=stop_words,
                max_features=max_features, 
                max_df=max_df, 
                min_df=min_df
            )
    
    def fit(self):
        self.load_data()
        self.features = self.cv.fit_transform(self.raw_data)

    def load_data(self):
        emails = []
        spam_file_path = f'{self.path}/spam/'
        for filename in glob.glob(os.path.join(spam_file_path, '*.txt')):
            sleep(DELAY)
            emails.append(get_contents_from_file(filename))
            print(f"...loading {filename}...")

        ham_file_path = f'{self.path}/ham/'
        for filename in glob.glob(os.path.join(ham_file_path, '*.txt')):
            sleep(DELAY)
            emails.append(get_contents_from_file(filename))
            print(f"...loading {filename}...")

        emails_cleaned = []
        for email in emails:
            sleep(DELAY)
            print(f"...cleaning...")
            emails_cleaned.append(clean_text(email))

        print(f"...DONE...")
        self.raw_data = emails_cleaned
        self.labels = np.load("labels.npy")
    
    def get_feature_array(self):
        return self.features.toarray()

    def get_feature_names(self):
        return self.cv.get_feature_names()
