from arteraro.auxt.expt.result.gec import (
        bea19_result,
        conll_result,
        fce_result,
        jfleg_result)

def bea19_result_command(args):
    bea19_result()

def conll_result_command(args):
    conll_result()

def fce_result_command(args):
    fce_result()

def jfleg_result_command(args):
    jfleg_result()

def set_result(main_sub_parsers):
    parser = main_sub_parsers.add_parser('result')
    sub_parsers = parser.add_subparsers()

    bea19 = sub_parsers.add_parser('bea19') 
    bea19.set_defaults(handler = bea19_result_command)

    conll = sub_parsers.add_parser('conll')
    conll.set_defaults(handler = conll_result_command)

    fce = sub_parsers.add_parser('fce')
    fce.set_defaults(handler = fce_result_command)

    jfleg = sub_parsers.add_parser('jfleg')
    jfleg.set_defaults(handler = jfleg_result_command)

