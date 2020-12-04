from argparse import ArgumentParser
from falsliter.noiser import FalsLiterNoiser

def sample(noiser):
    line = input('input > ')
    if len(line) != 2 * noiser.n + 1:
        return None

    src = line[:noiser.n] + line[-noiser.n:]
    if line[noiser.n] in noiser.vocab:
        trg = line[noiser.n]
    else:
        trg = None
    cand = noiser(src, trg)
    return cand

def main():
    parser = ArgumentParser()
    parser.add_argument('n', type = int)
    parser.add_argument('score_path')
    parser.add_argument('--T', type = float, default = 1.0)
    args = parser.parse_args()

    noiser = FalsLiterNoiser(args.n, args.score_path, args.T)
    while x := sample(noiser):
        print(f'{x} ({noiser.vocab.index(x)})')

