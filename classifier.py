from processors import *
from model import Model

model = Model(path = "./dat/enron1/")
model.cache()

class Text(object):
    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.cleaned_text = clean_text(self.raw_text)
        self.words = tokenize(self.cleaned_text)
        self.f_if = text_to_feature_array(self.raw_text)

    def __repr__(self):
        return f"{self.words}"

    def get_spam_percentage(self):
        return 69.99
