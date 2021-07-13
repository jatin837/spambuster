from sklearn.feature_extraction.text import CountVectorizer

class Model(object):
    def __init__(self, path):
        self.path = path
        self.cv = CountVectorizer(stop_words="english", max_features=1000, max_df=0.5, min_df=2)
