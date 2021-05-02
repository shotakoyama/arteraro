from arteraro.auxt.rtt.split.main import rtt_split
from arteraro.auxt.rtt.translate.main import rtt_fore, rtt_back
from arteraro.auxt.rtt.join.main import rtt_join
from arteraro.auxt.rtt.merge.main import rtt_merge

def rtt_split_command(args):
    rtt_split()

def rtt_fore_command(args):
    rtt_fore()

def rtt_back_command(args):
    rtt_back()

def rtt_join_command(args):
    rtt_join()

def rtt_merge_command(args):
    rtt_merge()

def set_rtt(main_sub_parsers):
    parser = main_sub_parsers.add_parser('rtt')
    sub_parsers = parser.add_subparsers()

    split = sub_parsers.add_parser('split')
    split.set_defaults(handler = rtt_split_command)

    fore = sub_parsers.add_parser('fore')
    fore.set_defaults(handler = rtt_fore_command)

    back = sub_parsers.add_parser('back')
    back.set_defaults(handler = rtt_back_command)

    join = sub_parsers.add_parser('join')
    join.set_defaults(handler = rtt_join_command)

    merge = sub_parsers.add_parser('merge')
    merge.set_defaults(handler = rtt_merge_command)

