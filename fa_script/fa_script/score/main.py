from fa_script.score.bea19 import score_bea19_valid_single
from fa_script.score.conll import score_conll_valid_single, score_conll_test_single
from fa_script.score.fce import score_fce_valid_single, score_fce_test_single
from fa_script.score.jfleg import score_jfleg_valid_single, score_jfleg_test_single
from argparse import ArgumentParser

def valid():
    score_bea19_valid_single()
    score_conll_valid_single()
    score_fce_valid_single()
    score_jfleg_valid_single()

def test():
    parser = ArgumentParser()
    parser.add_argument('-c', '--conll', action='store_true')
    parser.add_argument('-f', '--fce', action='store_true')
    args = parser.parse_args()

    if not args.fce:
        score_conll_test_single()

    if not args.conll:
        score_fce_test_single()

    if not (args.conll or args.fce):
        score_jfleg_test_single()

