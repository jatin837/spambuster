from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import numpy as np

from nltk.corpus import names
ALL_NAMES = set(names.words())

with open("feature_space.txt", 'r') as f:
    feature_space = f.readlines()
    for i in range(len(feature_space)):
        feature_space[i] = feature_space[i][:-1]

def word_stemmer(words):
    stemmer = PorterStemmer()
    stem_words = [stemmer.stem(o) for o in words]
    return stem_words

def word_lemmatizer(words):
    lemmatizer = WordNetLemmatizer()
    lemma_words = [lemmatizer.lemmatize(o) for o in words]
    return lemma_words

def words_from_text(text: str) -> list[str]:
    return text.split(" ")

def text_from_words(words: list[str]) -> str:
    return " ".join(words)

def tokenize(text: str) -> list[str]:
    return word_tokenize(text)

def is_letter_only(word: str) -> bool:
    for char in word:
        if not char.isalpha():
            return False
    return True

def clean_text(text: str) -> str:
    """
    input: text
           Eg text = 
                '''
                we could have had it all
                rolling in the deep
                you had my heart inside you hand
                but you played it to the beat
                '''

    output: Cleaned text(no names and only alphaneumeric)
    """
    text_cleaned = []
    words = tokenize(text)

    for word in words:
        if is_letter_only(word):
            text_cleaned.append(word)

    text_cleaned = text_from_words(text_cleaned)
    return text_cleaned

def text_to_feature_array(text: str) -> np.array:
    result = []
    cleaned_text = clean_text(text)
    tokens = tokenize(cleaned_text)
    for token in tokens:
        if token in feature_space:
            result.append(feature_space.index(token))
    if len(result) == 0:
        return np.array([-1])
    return np.array(result)

