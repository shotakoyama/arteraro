from arteraro.auxt.data.preproc.mt import mt_preproc

def mt_preproc_command(args):
    mt_preproc()

def set_preproc(main_sub_parsers):
    parser = main_sub_parsers.add_parser('preproc')
    sub_parsers = parser.add_subparsers()

    mt = sub_parsers.add_parser('mt')
    mt.set_defaults(handler = mt_preproc_command)

