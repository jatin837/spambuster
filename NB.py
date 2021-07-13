from helpers import *
import numpy as np
import glob
from processors import *

LABELS :np.array = np.load("labels.npy")

def eval_NB(p: list[float]) -> float:
    """
                           (p1 * p2 * p3 * p4 * ... * pN) * PRIOR["spam"]
    res =   -----------------------------------------------------------------------------------
            (p1 * p2 * p3 * p4 * ... * pN) + ( (1 - p1) * (1 - p2) * (1 - p3) * ... * (1 - pN))
    """
    pass

INDX_UPTO_SPAM: int = np.count_nonzero(LABELS)
INDX_UPTO_TOTAL: int = LABELS.shape[0]
TOTAL_SPAM_FEATURES: int = [np.load(f"data/{str(i + 1)}.npy") for i in range(INDX_UPTO_SPAM)]

N_SPAM: int = INDX_UPTO_SPAM
N_HAM: int = INDX_UPTO_TOTAL - INDX_UPTO_SPAM

PRIOR: dict[str, float] = {
        "spam": (N_SPAM)/(N_SPAM + N_HAM), 
        "non-spam": (N_HAM)/(N_SPAM + N_HAM)
        }

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

