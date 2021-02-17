from arteraro.fa_script.rescore.bea19 import bea19_rescore_regenerate, bea19_rescore_valid_score
from arteraro.fa_script.rescore.conll import conll_rescore_regenerate, conll_rescore_valid_score, conll_rescore_test_score
from arteraro.fa_script.rescore.fce import fce_rescore_regenerate, fce_rescore_valid_score, fce_rescore_test_score
from arteraro.fa_script.rescore.jfleg import jfleg_rescore_regenerate, jfleg_rescore_valid_score, jfleg_rescore_test_score
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('-b', '--bea19', action='store_true')
    parser.add_argument('-c', '--conll', action='store_true')
    parser.add_argument('-f', '--fce', action='store_true')
    args = parser.parse_args()

    if not (args.conll or args.fce):
        bea19_rescore_regenerate()
        bea19_rescore_valid_score()

    if not (args.bea19 or args.fce):
        conll_rescore_regenerate()
        conll_rescore_valid_score()
        conll_rescore_test_score()

    if not (args.bea19 or args.conll):
        fce_rescore_regenerate()
        fce_rescore_valid_score()
        fce_rescore_test_score()

    if not (args.bea19 or args.conll or args.fce):
        jfleg_rescore_regenerate()
        jfleg_rescore_valid_score()
        jfleg_rescore_test_score()

