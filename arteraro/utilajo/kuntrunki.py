import sys
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('-r', '--ratio', type=float, default=2.0)
    args = parser.parse_args()

    th = args.ratio
    for x in sys.stdin:
        x = x.strip()
        x = x.split('\t')
        org = x[0]
        len_org = len(org.split())
        srcs = []
        for src in x[1:]:
            len_src = len(src.split())
            if (len_src <= len_org * th) and (len_org <= len_src * th):
                srcs.append(src)
        x = '\t'.join([org] + srcs)
        print(x)

