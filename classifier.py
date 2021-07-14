from processors import *

class Text(object):
    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.cleaned_text = clean_text(self.raw_text)
        self.words = tokenize(self.cleaned_text)

    def __repr__(self):
        return f"{self.words}"
