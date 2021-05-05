from arteraro.auxt.tokenize.main import tokenize

def tokenize_command(args):
    tokenize()

def set_tokenize(main_sub_parsers):
    parser = main_sub_parsers.add_parser('tokenize')
    parser.set_defaults(handler = tokenize_command)

