import sys
from argparse import ArgumentParser
from .encoder import Encoder
from .decoder import Decoder

def make_encoder():
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
    return encoder

def encode():
    encoder = make_encoder()
    for line in sys.stdin:
        line = encoder(line)
        if line is not None:
            print(line)

def ambiencode():
    encoder = make_encoder()
    for line in sys.stdin:
        line = line.rstrip('\n')
        src, trg = line.split('\t')
        src = encoder(src)
        if src is None:
            continue
        trg = encoder(trg)
        if trg is None:
            continue
        print('{}\t{}'.format(src, trg))

def decode():
    decoder = Decoder()
    for line in sys.stdin:
        line = decoder(line)
        print(line)

