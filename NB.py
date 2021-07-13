from helpers import *
import numpy as np
import glob
from processors import *

labels = np.load("labels.npy")

def eval_NB(text: str) -> float:
    return 59.00


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
