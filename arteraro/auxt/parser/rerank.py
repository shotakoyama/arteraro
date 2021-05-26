from .gec import (
        make_gec_dataset_arguments,
        add_gec_dataset_arguments)
from arteraro.auxt.expt.reranking.gec import gec_ensemble_reranking

def gec_ensemble_reranking_command(args):
    gec_ensemble_reranking(*make_gec_dataset_arguments(args))


def set_gec_reranking(main_sub_parsers):
    parser = main_sub_parsers.add_parser('gec')
    sub_parsers = parser.add_subparsers()

    ensemble = sub_parsers.add_parser('ensemble')
    add_gec_dataset_arguments(ensemble)
    ensemble.set_defaults(handler = gec_ensemble_reranking_command)


def set_rerank(main_sub_parsers):
    parser = main_sub_parsers.add_parser('rerank')
    sub_parsers = parser.add_subparsers()

    set_gec_reranking(sub_parsers)

