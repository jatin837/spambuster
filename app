#!./env/bin/python

from lib.processors import *
from lib.helpers import *
from lib.classifier import Text

def main() -> ():
    ipath = get_args()

    raw_contents = get_contents_from_file(ipath)
    text = Text(raw_contents)

    cleaned_contents = text.cleaned_text
    words = text.words

    spam_percentage: float = text.get_spam_percentage()
    print("--"*10)
    print(spam_percentage)

if __name__ == "__main__":
    main()
