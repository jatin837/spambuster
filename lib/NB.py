from .helpers import *
import numpy as np
import glob
from .processors import *
from .model import Model

model = Model(path = "./dat/enron1")
model.cache()

A = [model.get_total_ham_features_count(), model.get_total_spam_features_count()]
B = model.get_unique_features_count()

def percentage_spam(word_indeces: list[int]) -> float:
    """
                           (p1 * p2 * p3 * p4 * ... * pN) * PRIOR["spam"]
    res =   -----------------------------------------------------------------------------------
            (p1 * p2 * p3 * p4 * ... * pN) + ( (1 - p1) * (1 - p2) * (1 - p3) * ... * (1 - pN))
    """
    a = get_likelihood(word_indeces, 1)
    b = get_likelihood(word_indeces, 0)
    Pa = get_prior(1)
    Pb = get_prior(0)
    res = (a*Pa) / (a*Pa + b*Pb)
    return res*100

def get_prior(T: int):
    """
    ======
    param:
    ======
        class  => integer representing which class
            - "spam" => 1
            - "ham"  => 0

    ==============
    evaluate prior
    ==============
                n_spam
        p = -----------------
            n_spam + n_ham
    """
    label_index = model.get_label_index()
    prior = {label: len(index) for label, index in label_index.items()}
    total_count = sum(prior.values())
    for label in prior:
        prior[label] /= float(total_count)
    return prior[T]


def get_likelihood(word_indeces: list[int], T: int) -> float:
    """
    ======
    param:
    ======
        list of words   => list of strings
        type            => string of either kind:
            - "spam"
            - "ham"

    For each word, evaluate p(word)
    `p1 => p(word 1)`
    `p2 => p(word 2)`
    `p3 => p(word 3)`
      . ..   ...
      . ..   ...
      . ..   ...
    `pN => p(word N)`

    =======
    return:
    =======
        likelihood = p1 * p2 * p3 * p4 * ... * pN

    """
    L = np.array([p(word_indx, T) for word_indx in word_indeces])
    res = np.prod(L)
    return res

def p(word_indx: int, T: int) -> float:
    return model.get_likelihood(T = T, indx = word_indx)
