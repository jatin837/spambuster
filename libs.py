from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


def word_stemmer(words):
    stemmer = PorterStemmer()
    stem_words = [stemmer.stem(o) for o in words]
    return stem_words

def word_lemmatizer(words):
    lemmatizer = WordNetLemmatizer()
    lemma_words = [lemmatizer.lemmatize(o) for o in words]
    return lemma_words
