from argparse import ArgumentParser
from .parser.prepare import set_prepare
from .parser.preproc import set_preproc
from .parser.train import set_train
from .parser.generation import set_generation
from .parser.score import set_score
from .parser.result import set_result
from .parser.split import set_split
from .parser.rtt import set_rtt
from .parser.tokenize import set_tokenize
from .parser.ready import set_ready
from .parser.erg import set_erg
from .parser.conv import set_conv

def main():
    parser = ArgumentParser()
    sub_parsers = parser.add_subparsers()

    set_prepare(sub_parsers)
    set_preproc(sub_parsers)
    set_train(sub_parsers)
    set_generation(sub_parsers)
    set_score(sub_parsers)
    set_result(sub_parsers)
    set_split(sub_parsers)
    set_rtt(sub_parsers)
    set_tokenize(sub_parsers)
    set_ready(sub_parsers)
    set_erg(sub_parsers)
    set_conv(sub_parsers)

    args = parser.parse_args()

    if hasattr(args, 'handler'):
        args.handler(args)

