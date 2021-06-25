from arteraro.auxt.erg.main import erg
from arteraro.auxt.erg.fix_prepare import fix_prepare
from arteraro.auxt.erg.fix_preproc import fix_preproc

def erg_command(args):
    erg()

def fixerg_prepare_command(args):
    fix_prepare()

def fixerg_preproc_command(args):
    fix_preproc()

def set_erg(main_sub_parsers):
    parser = main_sub_parsers.add_parser('erg')
    parser.set_defaults(handler = erg_command)

def set_fixerg(main_sub_parsers):
    parser = main_sub_parsers.add_parser('fixerg')
    sub_parsers = parser.add_subparsers()

    prepare = sub_parsers.add_parser('prepare')
    prepare.set_defaults(handler = fixerg_prepare_command)

    preproc = sub_parsers.add_parser('preproc')
    preproc.set_defaults(handler = fixerg_preproc_command)

