from arteraro.auxt.data.preproc.mt import mt_preproc
from arteraro.auxt.data.preproc.aeg import aeg_preproc
from arteraro.auxt.data.preproc.bea19 import bea19_preproc

def mt_preproc_command(args):
    mt_preproc()

def aeg_preproc_command(args):
    aeg_preproc()

def bea19_preproc_command(args):
    bea19_preproc()

def set_preproc(main_sub_parsers):
    parser = main_sub_parsers.add_parser('preproc')
    sub_parsers = parser.add_subparsers()

    mt = sub_parsers.add_parser('mt')
    mt.set_defaults(handler = mt_preproc_command)

    aeg = sub_parsers.add_parser('aeg')
    aeg.set_defaults(handler = aeg_preproc_command)

    bea19 = sub_parsers.add_parser('bea19')
    bea19.set_defaults(handler = bea19_preproc_command)

