from arteraro.auxt.erg.main import erg

def erg_command(args):
    erg()

def set_erg(main_sub_parsers):
    parser = main_sub_parsers.add_parser('erg')
    parser.set_defaults(handler = erg_command)

