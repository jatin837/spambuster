from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenizer

from nltk.corpus import names
ALL_NAMES = set(names.words())

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
    return word_tokenizer(text)

def is_letter_only(word: str) -> bool:
    for char in word:
        if not char.isalpha():
            return False
    return True

def clean_text(docs: list[str]) -> list[str]:
    """
    input: List of text
           Eg docs = [
                "we could have had it all",
                "rolling in the deep",
                "you had my heart inside you hand",
                "but you played it to the beat"
            ]

    output: Cleaned list(no names and only alphaneumeric)
    """
    docs_cleaned = []
    for doc in docs:
        doc = doc.lower()
        doc_cleaned = ' '.join(lemmatizer.lemmatize(word) for word in doc.split() if is_letter_only(word) and word not in ALL_NAMES)
        docs_cleaned.append(doc_cleaned)
    return docs_cleaned

