from fa_script.generate.bea19 import generate_bea19_valid_single, generate_bea19_test_single
from fa_script.generate.conll import generate_conll_valid_single, generate_conll_test_single
from fa_script.generate.fce import generate_fce_valid_single, generate_fce_test_single
from fa_script.generate.jfleg import generate_jfleg_valid_single, generate_jfleg_test_single
from argparse import ArgumentParser

def valid():
    generate_bea19_valid_single()
    generate_conll_valid_single()
    generate_fce_valid_single()
    generate_jfleg_valid_single()

def test():
    parser = ArgumentParser()
    parser.add_argument('-b', '--bea19', action='store_true')
    parser.add_argument('-c', '--conll', action='store_true')
    parser.add_argument('-f', '--fce', action='store_true')
    args = parser.parse_args()

    if not (args.conll or args.fce):
        generate_bea19_test_single()

    if not (args.bea19 or args.fce):
        generate_conll_test_single()

    if not (args.bea19 or args.conll):
        generate_fce_test_single()

    if not (args.bea19 or args.conll or args.fce):
        generate_jfleg_test_single()

