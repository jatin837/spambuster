#!./env/bin/python

from processors import *
from helpers import *

from NB import eval_NB

def main() -> ():
    ## test phase

    ## get input file path
    ipath = get_args()
    logging.info(ipath)

    ## get raw text from input file path
    raw_contents = get_contents_from_file(ipath)
    logging.info(raw_contents)

    ## clean raw_contents(checkout defination of `clean` in processors.clean_text doc_string
    cleaned_contents = clean_text(raw_contents)
    
    ## get words from raw text using split function
    words = words_from_text(cleaned_contents)

    ## get words from raw text using nltk tokenize function
    words2 = tokenize(cleaned_contents)

    ## get stem words from words
    stem_words = word_stemmer(words)

    ## get stem text
    stem_text = text_from_words(stem_words)

    ## get lemma words from words
    lemma_words = word_lemmatizer(words)

    ## get lemma text
    lemma_text = text_from_words(lemma_words)

    logging.info(f"done\ncleaned_contents\n{cleaned_contents}")

    spam_percentage: float = eval_NB(cleaned_contents)
    print(spam_percentage)

if __name__ == "__main__":
    main()