from argparse import ArgumentParser
from .parser.prepare import set_prepare
from .parser.preproc import set_preproc
from .parser.train import set_train
from .parser.generation import set_generation
from .parser.score import set_score

def main():
    parser = ArgumentParser()
    sub_parsers = parser.add_subparsers()

    set_prepare(sub_parsers)
    set_preproc(sub_parsers)
    set_train(sub_parsers)
    set_generation(sub_parsers)
    set_score(sub_parsers)

    args = parser.parse_args()

    if hasattr(args, 'handler'):
        args.handler(args)

