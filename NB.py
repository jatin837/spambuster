from helpers import *
import numpy as np
import glob
from processors import *
from model import Model

model = Model(path = "./dat/enron1")
model.cache()

A = [model.get_total_ham_features_count(), model.get_total_spam_features_count()]
B = model.get_unique_features_count()

def percentage_spam(p: list[int]) -> float:
    """
                           (p1 * p2 * p3 * p4 * ... * pN) * PRIOR["spam"]
    res =   -----------------------------------------------------------------------------------
            (p1 * p2 * p3 * p4 * ... * pN) + ( (1 - p1) * (1 - p2) * (1 - p3) * ... * (1 - pN))
    """
    a = get_likelihood(word_indeces, 1)
    b = get_likelihood(word_indeces, 1)
    prior = get_prior(1)
    res = (a*prior) / (a + b)
    return res*100

def get_prior(T: int) -> float:
    """
    ======
    param:
    ======
        type  => String of either kind
            - "spam"
            - "ham"

    ==============
    evaluate prior
    ==============
                n_spam
        p = -----------------
            n_spam + n_ham
    """
    n_spam = np.count_nonzero(model.labels)
    n_ham = model.labels.shape[0] - n_spam
    
    p = (n_spam) / (n_spam + n_ham)
    
    if T == 0:
        return (1 - p)
    elif T == 1:
        return p

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

    res = 1
    for word_indx in word_indeces:
        res *= p(word_indx, T)
    return res

def p(word_indx: int, T: int) -> float:
    if word_indx == -1:
        p = 1/(A[T] + B)
        return p
    try:
        """
        check if word exist in our feature space
        if yes, then evaluate using below expression

                            (total number of times 'word' occure in all spam messages)  +  1
             p(word|Spam) = -----------------------------------------------------------------
                            (total spam features)    +    (total unique features in our data)

        """
        x = model.count(word_indx, T)
        p = (x + 1) / (A[T] + B)
        return p
    except ValueError:
        """
        if word does not exist in feature_space, then
        evaluate                             
                                             1
                 p = ------------------------------------------------------
                    total spam features + total unique features in our data
        """
        print("IMPOSSIBLE INDEX GIVEN")
        exit(1)

