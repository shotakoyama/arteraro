from arteraro.auxt.expt.wmt import wmt_valid_score, wmt_test_score

def wmt_valid_score_command(args):
    wmt_valid_score()

def wmt_test_score_command(args):
    wmt_test_score()

def set_wmt_score(main_sub_parsers):
    parser = main_sub_parsers.add_parser('wmt')
    sub_parsers = parser.add_subparsers()

    valid = sub_parsers.add_parser('valid')
    valid.set_defaults(handler = wmt_valid_score_command)

    test = sub_parsers.add_parser('test')
    test.set_defaults(handler = wmt_test_score_command)

def set_score(main_sub_parsers):
    parser = main_sub_parsers.add_parser('score')
    sub_parsers = parser.add_subparsers()

    set_wmt_score(sub_parsers)

