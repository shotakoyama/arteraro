import sys
from argparse import ArgumentParser

def glui(src, trg, min_len, max_len):

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

def main():
    parser = ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('target')
    parser.add_argument('--min-len', type=int, default = 1)
    parser.add_argument('--min-len', type=int, default = 500)

    glui(args.source, args.target, args.min_len, args.max_len)

