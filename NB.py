from helpers import *
import numpy as np
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
terms = cv.get_feature_names()

with open("feature_space.txt", 'w') as f:
    for term in terms:
        f.write(term)
        f.write('\n')

def get_feature_index(indx: int) -> list[int]:
    """
    param:  index from cleaned emails
    return: list representing feature index and number of occurence
    """
    try:
        email = docs_cv.toarray()[indx]
    except IndexError:
        print("index given is out of range")
        exit(1)
    feature_index = []
    for i in range(len(email)):
        if email[i] != 0:
            feature_index.append([i, email[i]])
    return np.array(feature_index)



N_spam = labels.count(1)
N_nspam = labels.count(0)

PRIOR: dict[str, float] = {
        "spam": (N_spam)/(N_spam + N_nspam), 
        "non-spam": (N_nspam)/(N_spam + N_nspam)
        }

def get_posterior():
    pass

def get_likelihood():
    pass

def get_evidence():
    pass
