from argparse import ArgumentParser
from .en.ready import en_ready
from .en.run import en_run
from .en.form import en_form
from .en.show import en_show

def command_en_ready(args):
    quote = not args.no_quote_regularization
    en_ready(quote=quote)


def command_en_run(args):
    if args.languages is None:
        lang_list = None
    else:
        lang_list = args.languages.split(':')
    en_run(config=args.config, ratio=args.ratio, lang_list=lang_list)


def command_en_form(args):
    en_form()


def command_en_show(args):
    en_show(
        hide_history = args.hide_history,
        color = args.color,
        cor = args.cor,
        tag = args.tag,
        pos = args.pos,
        dep = args.dep)


def ready(main_sub_parsers):
    parser = main_sub_parsers.add_parser('ready')
    sub_parsers = parser.add_subparsers()

    en = sub_parsers.add_parser('en')
    en.add_argument('--no-quote-regularization', action = 'store_true')
    en.set_defaults(handler = command_en_ready)


def run(main_sub_parsers):
    parser = main_sub_parsers.add_parser('run')
    sub_parsers = parser.add_subparsers()

    en = sub_parsers.add_parser('en')
    en.add_argument('-c', '--config', default = 'config.yaml')
    en.add_argument('-r', '--ratio', type=float, default=0.0)
    en.add_argument('-l', '--languages', default=None)
    en.set_defaults(handler = command_en_run)


def form(main_sub_parsers):
    parser = main_sub_parsers.add_parser('form')
    sub_parsers = parser.add_subparsers()

    en = sub_parsers.add_parser('en')
    en.set_defaults(handler = command_en_form)


def show(sub_parsers):
    parser = sub_parsers.add_parser('show')
    sub_parsers = parser.add_subparsers()

    en = sub_parsers.add_parser('en')
    en.add_argument('--hide-history', action = 'store_true')
    en.add_argument('--color', action = 'store_true')
    en.add_argument('--cor', default = None)
    en.add_argument('--tag', default = None)
    en.add_argument('--pos', default = None)
    en.add_argument('--dep', default = None)
    en.set_defaults(handler = command_en_show)


def main():
    parser = ArgumentParser()
    sub_parsers = parser.add_subparsers()

    ready(sub_parsers)
    run(sub_parsers)
    form(sub_parsers)
    show(sub_parsers)

    args = parser.parse_args()

    if hasattr(args, 'handler'):
        args.handler(args)

