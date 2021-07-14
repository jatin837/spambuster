from processors import *

class Text(object):
    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.cleaned_text = clean_text(raw_text)
        self.words = tokenize(cleaned_text)

    def __str__(self):
        return f"{self.words}"
