#!./env/bin/python

from processors import *
from helpers import *
from classifier import Text

def main() -> ():
    ipath = get_args()

    raw_contents = get_contents_from_file(ipath)
    text = Text(raw_contents)

    cleaned_contents = text.cleaned_text
    words = text.words

    spam_percentage: float = 69.99
    print(spam_percentage)

if __name__ == "__main__":
    main()
