import sys
from argparse import ArgumentParser

def get_length(line):
    return len(line.strip().split())

def cond(args, src, trg):
    src_length = get_length(src)
    if not (args.min_len <= src_length <= args.max_len):
        return False

    trg_length = get_length(trg)
    if not (args.min_len <= trg_length <= args.max_len):
        return False

    return True

def main():
    parser = ArgumentParser()
    parser.add_argument('--min-len', type=int, default = 1)
    parser.add_argument('--max-len', type=int, default = 400)
    args = parser.parse_args()

    try:
        for line in sys.stdin:
            line = line.rstrip('\n')
            src, trg = line.split('\t')
            if cond(args, src, trg):
                line = '{}\t{}'.format(src, trg)
                print(line)
    except KeyboardInterrupt:
        pass
    except BrokenPipeError:
        pass

