from arteraro.auxt.expt.wmt import wmt_valid_generation, wmt_test_generation

def wmt_valid_generation_command(args):
    wmt_valid_generation()

def wmt_test_generation_command(args):
    wmt_test_generation()

def set_wmt_generation(main_sub_parsers):
    parser = main_sub_parsers.add_parser('wmt')
    sub_parsers = parser.add_subparsers()

    valid = sub_parsers.add_parser('valid')
    valid.set_defaults(handler = wmt_valid_generation_command)

    test = sub_parsers.add_parser('test')
    test.set_defaults(handler = wmt_test_generation_command)

def set_gec_generation(main_sub_parsers):
    parser = main_sub_parsers.add_parser('gec')
    sub_parsers = parser.add_subparsers()

    valid = sub_parsers.add_parser('valid')
    valid.set_defaults(handler = gec_valid_generation_command)

    test = sub_parsers.add_parser('test')
    test.set_defaults(handler = gec_test_generation_command)

    ensemble = sub_parsers.add_parser('ensemble')
    ensemble.set_defaults(handler = gec_ensemble_generation_command)

def set_generation(main_sub_parsers):
    parser = main_sub_parsers.add_parser('generate')
    sub_parsers = parser.add_subparsers()

    set_wmt_generation(sub_parsers)
    # set_gec_generation(sub_parsers)

