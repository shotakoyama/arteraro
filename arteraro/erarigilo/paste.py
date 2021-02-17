import sys
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('src')
    parser.add_argument('trg')
    parser.add_argument('--min-len', type = int, default = 1)
    parser.add_argument('--max-len', type = int, default = 500)
    args = parser.parse_args()

    with open(args.src) as f, open(args.trg) as g:

        for src, trg in zip(f, g):

            # remove \n
            src = src.strip()
            trg = trg.strip()

            # string -> list
            src_len = len(src.split())
            trg_len = len(trg.split())

            # codition of sentence length
            src_cond = args.min_len <= src_len <= args.max_len
            trg_cond = args.min_len <= trg_len <= args.max_len

            # output pasted sentence pair
            if src_cond and trg_cond:
                out = src + '\t' + trg
                print(out)

