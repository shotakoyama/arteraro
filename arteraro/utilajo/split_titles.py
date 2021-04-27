import sys
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('col', type=int)
    args = parser.parse_args()

    for line in sys.stdin:
        x = line.split('|||')
        x = x[args.col].strip()
        print(x)

