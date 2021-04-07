import sys
from argparse import ArgumentParser
from .encoder import Encoder
from .decoder import Decoder

def encode():
    parser = ArgumentParser()
    parser.add_argument('-n', '--name', default = 'base')
    parser.add_argument('-q', '--quote', action = 'store_true')
    parser.add_argument('-a', '--all', action = 'store_true')
    parser.add_argument('-r', '--rev', action = 'store_true')
    parser.add_argument('-z', '--rm-zero', action = 'store_true')
    args = parser.parse_args()

    encoder = Encoder(
            name = args.name,
            quote = args.quote,
            rev = args.rev,
            full = args.all,
            rm_zero = args.rm_zero)

    for line in sys.stdin:
        line = encoder(line)
        if line is not None:
            print(line)

def decode():
    decoder = Decoder()
    for line in sys.stdin:
        line = decoder(line)
        print(line)

