from .gec import make_gec_dataset_arguments, add_gec_dataset_arguments
from arteraro.auxt.expt.wmt import wmt_valid_score, wmt_test_score
from arteraro.auxt.expt.score.gec import gec_valid_score

def wmt_valid_score_command(args):
    wmt_valid_score()


def wmt_test_score_command(args):
    wmt_test_score()


def gec_valid_score_command(args):
    gec_valid_score(*make_gec_dataset_arguments(args))


def set_wmt_score(main_sub_parsers):
    parser = main_sub_parsers.add_parser('wmt')
    sub_parsers = parser.add_subparsers()

    valid = sub_parsers.add_parser('valid')
    valid.set_defaults(handler = wmt_valid_score_command)

    test = sub_parsers.add_parser('test')
    test.set_defaults(handler = wmt_test_score_command)


def set_gec_score(main_sub_parsers):
    parser = main_sub_parsers.add_parser('gec')
    sub_parsers = parser.add_subparsers()

    valid = sub_parsers.add_parser('valid')
    add_gec_dataset_arguments(valid)
    valid.set_defaults(handler = gec_valid_score_command)

    # test = sub_parsers.add_parser('test')
    # test.set_defaults(handler = gec_test_score_command)

    # ensemble = sub_parsers.add_parser('ensemble')
    # ensemble.set_defaults(handler = gec_ensemble_score_command)


def set_score(main_sub_parsers):
    parser = main_sub_parsers.add_parser('score')
    sub_parsers = parser.add_subparsers()

    set_wmt_score(sub_parsers)
    set_gec_score(sub_parsers)

