import sys
from argparse import ArgumentParser

def normal(n, inverse):
    for line in sys.stdin:
        line = line.strip()
        length = len(line.split())
        if (length <= n) ^ inverse:
            print(line)

def reflect(n, inverse, src, trg):
    with open(src) as f, open(trg, 'w') as g:
        for line, orig in zip(sys.stdin, f):
            line = line.strip()
            orig = orig.strip()
            length = len(line.split())
            if (length <= n) ^ inverse:
                print(line)
                print(orig, file=g)

def main():
    parser = ArgumentParser()
    parser.add_argument('-n', type=int)
    parser.add_argument('-i', '--inverse', action='store_true')
    parser.add_argument('-r', '--reflect', action='store_true')
    parser.add_argument('-s', '--source')
    parser.add_argument('-t', '--target')
    args = parser.parse_args()

    if args.reflect:
        reflect(args.n, args.inverse, args.source, args.target)
    else:
        normal(args.n, args.inverse)


