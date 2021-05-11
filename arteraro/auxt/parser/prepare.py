from arteraro.auxt.data.prepare.mt import mt_prepare
from arteraro.auxt.data.prepare.bea19 import bea19_prepare

def mt_prepare_command(args):
    mt_prepare()

def bea19_prepare_command(args):
    bea19_prepare()

def set_prepare(main_sub_parsers):
    parser = main_sub_parsers.add_parser('prepare')
    sub_parsers = parser.add_subparsers()

    mt = sub_parsers.add_parser('mt')
    mt.set_defaults(handler = mt_prepare_command)

    bea19 = sub_parsers.add_parser('bea19')
    bea19.set_defaults(handler = bea19_prepare_command)


