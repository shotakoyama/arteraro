from argparse import ArgumentParser
from .encode import encode
from .decode import decode

def encode_main():
    parser = ArgumentParser()
    parser.add_argument('-a', '--all', action = 'store_true')
    parser.add_argument('-r', '--rev', action = 'store_true')
    parser.add_argument('-l', '--limit', action = 'store_true')
    parser.add_argument('-z', '--rm-zero', action = 'store_true')
    args = parser.parse_args()

    encode(limit=args.limit, rev=args.rev, full=args.all, rm_zero=args.rm_zero)

def decode_main():
    decode()

