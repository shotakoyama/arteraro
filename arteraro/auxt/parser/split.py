from arteraro.auxt.split.main import split

def split_command(args):
    split()

def set_split(main_sub_parsers):
    parser = main_sub_parsers.add_parser('split')
    parser.set_defaults(handler = split_command)

