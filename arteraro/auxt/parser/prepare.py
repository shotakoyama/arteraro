from arteraro.auxt.data.prepare.mt import mt_prepare

def mt_prepare_command(args):
    mt_prepare()

def set_prepare(main_sub_parsers):
    parser = main_sub_parsers.add_parser('prepare')
    sub_parsers = parser.add_subparsers()

    mt = sub_parsers.add_parser('mt')
    mt.set_defaults(handler = mt_prepare_command)

