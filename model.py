from sklearn.feature_extraction.text import CountVectorizer
import glob
import os
import numpy as np
import scipy as sp
from helpers import get_contents_from_file
from processors import clean_text
from time import sleep

DELAY: float = 0.001

class Model(object):
    def __init__(self, path='./dat/enron1/', stop_words="english", max_features=1000, max_df=0.5, min_df=2):
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
        with open("data/feature_names.txt", 'w') as f:
            for name in self._get_feature_names():
                f.write(name + "\n")

        np.save("data/feature_matrix.npy", self._get_feature_matrix())
        np.save("data/labels.npy", self.labels)
        sp.sparse.save_npz("data/feature_sparse.npz", self.features)

    def get_likelihood(self, T, indx, smoothing=1):
        term_matrix = self.features
        label_index = self.get_label_index()
        likelihood = {}
        for label, index in label_index.items():
            likelihood[label] = term_matrix[index, :].sum(axis=0) + smoothing
            likelihood[label] = np.asarray(likelihood[label])[0]
            total_count = likelihood[label].sum()
            likelihood[label] = likelihood[label] / float(total_count)
        return likelihood[T][indx]

    def get_label_index(self):
        from collections import defaultdict
        label_index = defaultdict(list)
        for index, label in enumerate(self.labels):
            label_index[label].append(index)
        return label_index

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
        self.labels = np.load("data/labels.npy")
        self.feature_matrix = np.load("data/feature_matrix.npy")
        self.features = sp.sparse.load_npz("data/feature_sparse.npz")
        with open("data/feature_names.txt", 'r') as f:
            self.feature_names = f.read().split("\n")
    
    def _get_feature_matrix(self):
        self.feature_matrix = self.features.toarray()
        return self.feature_matrix

    def _get_feature_names(self):
        self.feature_names = self.cv.get_feature_names()
        return self.feature_names

    def get_total_spam_features_count(self):
        res = 0
        for i in range(np.count_nonzero(self.labels)):
            res += np.sum(self.feature_matrix[i])
        return res

    def get_total_ham_features_count(self):
        res = 0
        for i in range(np.count_nonzero(self.labels), self.labels.shape[0]):
            res += np.sum(self.feature_matrix[i])
        return res
    
    def get_indx(self, T):
        if T == 0:
            i = np.count_nonzero(self.labels)
            j = self.labels.shape[0]
        if T == 1:
            i = 0
            j = np.count_nonzero(self.labels)
        
        return i, j
    def get_unique_features_count(self):
        return self.feature_names.__len__()

    def count(self, indx, T):
        i, j = self.get_indx(T)
        res = np.sum(self.feature_matrix[i:j][indx])
        return res
