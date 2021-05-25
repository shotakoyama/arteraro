from .bea19 import (
        bea19_valid_generation,
        bea19_test_generation)
from .conll import (
        conll13_generation,
        conll14_generation)
from .fce import (
        fce_valid_generation,
        fce_test_generation)
from .jfleg import (
        jfleg_valid_generation,
        jfleg_test_generation)

def gec_valid_generation(bea19, conll, fce, jfleg):
    if bea19:
        bea19_valid_generation()
    if conll:
        conll13_generation()
    if fce:
        fce_valid_generation()
    if jfleg:
        jfleg_valid_generation()

def gec_test_generation(bea19, conll, fce, jfleg):
    if bea19:
        bea19_test_generation()
    if conll:
        conll14_generation()
    if fce:
        fce_test_generation()
    if jfleg:
        jfleg_test_generation()

