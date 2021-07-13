from helpers import *
import numpy as np
import glob
from processors import *
from model import Model

def eval_NB(p: list[float]) -> float:
    """
                           (p1 * p2 * p3 * p4 * ... * pN) * PRIOR["spam"]
    res =   -----------------------------------------------------------------------------------
            (p1 * p2 * p3 * p4 * ... * pN) + ( (1 - p1) * (1 - p2) * (1 - p3) * ... * (1 - pN))
    """
    pass

def get_prior(T: str) -> float:
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
    pass

def get_likelihood(words: list[str], T: str) -> float:
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
    pass


def p(word: str) -> float:
    try:
        """
        check if word exist in our feature space
        if yes, then evaluate using below expression

                            (total number of times 'word' occure in all spam messages)  +  1
             p(word|Spam) = -----------------------------------------------------------------
                            (total spam features)    +    (total unique features in our data)

        """
        pass
    except ValueError:
        """
        if word does not exist in feature_space, then
        evaluate                             
                                             1
                 p = ------------------------------------------------------
                    total spam features + total unique features in our data
        """
        pass

