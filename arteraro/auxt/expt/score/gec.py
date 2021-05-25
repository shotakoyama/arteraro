from .errant import (
        bea19_valid_score,
        fce_valid_score,
        fce_test_score)
from .m2 import (
        conll13_score,
        conll14_score)
from .gleu import (
        jfleg_valid_score,
        jfleg_test_score)

def gec_valid_score(bea19, conll, fce, jfleg):
    if bea19:
        bea19_valid_score()
    if conll:
        conll13_score()
    if fce:
        fce_valid_score()
    if jfleg:
        jfleg_valid_score()

def gec_test_score(conll, fce, jfleg):
    if conll:
        conll14_score()
    if fce:
        fce_test_score()
    if jfleg:
        jfleg_test_score()

