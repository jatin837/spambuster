from helpers import *
import numpy as np
import glob
from processors import *

labels = np.load("labels.npy")

def eval_NB(text: str) -> float:
    return 59.00

indx_upto_spam = np.count_nonzero(labels)
indx_upto_total = labels.shape[0]
total_spam_features = [np.load(f"data/{str(i + 1)}.npy") for i in range(indx_upto_spam)]

N_spam = indx_upto_spam
N_nspam = indx_upto_total - indx_upto_spam

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
