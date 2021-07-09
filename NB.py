from helpers import *
import glob
from processors import *

def eval_NB(text: str) -> float:
    return 59.00


emails, labels = [], []

# spam labeled with 1
spam_file_path = 'dat/enron1/spam/'
for filename in glob.glob(os.path.join(spam_file_path, '*.txt')):
    contents = get_contents_from_file(filename)
    emails.append(contents)
    labels.append(1)

breakpoint()
# ham labeled with 0
ham_file_path = 'dat/enron1/ham/'
for filename in glob.glob(os.path.join(ham_file_path, '*.txt')):
    contents = get_contents_from_file(filename)
    emails.append(contents)
    labels.append(0)

emails_cleaned = []
for email in emails:
    emails_cleaned.append(clean_text(email))

docs_cv = cv.fit_transform(emails_cleaned)

def get_prior():
    pass

def get_posterior():
    pass

def get_likelihood():
    pass

def get_evidence():
    pass
