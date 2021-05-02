import sys
from argparse import ArgumentParser

def normal(n, m, inverse):
    for line in sys.stdin:
        line = line.strip()
        length = len(line.split())
        if (m <= length <= n) ^ inverse:
            print(line)

def reflect(n, m, inverse, src, trg):
    with open(src) as f, open(trg, 'w') as g:
        for line, orig in zip(sys.stdin, f):
            line = line.strip()
            orig = orig.strip()
            length = len(line.split())
            if (m <= length <= n) ^ inverse:
                print(line)
                print(orig, file=g)

def main():
    parser = ArgumentParser()
    parser.add_argument('-n', type=int)
    parser.add_argument('-m', type=int, default=1)
    parser.add_argument('-i', '--inverse', action='store_true')
    parser.add_argument('-r', '--reflect', action='store_true')
    parser.add_argument('-s', '--source')
    parser.add_argument('-t', '--target')
    args = parser.parse_args()

    if args.reflect:
        reflect(args.n, args.m, args.inverse, args.source, args.target)
    else:
        normal(args.n, args.m, args.inverse)


