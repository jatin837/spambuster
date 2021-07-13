from helpers import *
import numpy as np
import glob
from processors import *

emails = []

# spam labeled with 1
spam_file_path = 'dat/enron1/spam/'
for filename in glob.glob(os.path.join(spam_file_path, '*.txt')):
    contents = get_contents_from_file(filename)
    emails.append(contents)

# ham labeled with 0
ham_file_path = 'dat/enron1/ham/'
for filename in glob.glob(os.path.join(ham_file_path, '*.txt')):
    contents = get_contents_from_file(filename)
    emails.append(contents)

count = 1
for email in emails:
    print(count)
    cleaned_email = clean_text(email)
    feature_array = text_to_feature_array(cleaned_email)
    np.save(f"data/{str(count)}.npy", feature_array)
    count += 1
