import sys
from argparse import ArgumentParser

def allocate_indices():
    for i, line in enumerate(sys.stdin):
        line = line.strip()
        line = '{}\t{}'.format(i, line)
        print(line)

def convert_to_indices():
    for i, _ in enumerate(sys.stdin):
        print(i)

def main():
    parser = ArgumentParser()
    parser.add_argument('--only-indices', action='store_true')
    args = parser.parse_args()

    try:
        if args.only_indices:
            convert_to_indices()
        else:
            allocate_indices()
    except KeyboardInterrupt:
        pass
    except BrokenPipeError:
        pass

