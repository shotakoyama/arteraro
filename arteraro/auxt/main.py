from argparse import ArgumentParser
from .data.prepare.mt import mt_prepare
from .data.preproc.mt import mt_preproc

def mt_prepare_command(args):
    mt_prepare()

def mt_preproc_command(args):
    mt_preproc()

def prepare(main_sub_parsers):
    parser = main_sub_parsers.add_parser('prepare')
    sub_parsers = parser.add_subparsers()

    mt = sub_parsers.add_parser('mt')
    mt.set_defaults(handler = mt_prepare_command)

def preproc(main_sub_parsers):
    parser = main_sub_parsers.add_parser('preproc')
    sub_parsers = parser.add_subparsers()

    mt = sub_parsers.add_parser('mt')
    mt.set_defaults(handler = mt_preproc_command)

def main():
    parser = ArgumentParser()
    sub_parsers = parser.add_subparsers()

    prepare(sub_parsers)
    preproc(sub_parsers)

    args = parser.parse_args()

    if hasattr(args, 'handler'):
        args.handler(args)

