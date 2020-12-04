from argparse import ArgumentParser
from falsliter.noiser import FalsLiterNoiser
from tabulate import tabulate

def infer(noiser):
    line = input('input > ')
    if len(line) != 2 * noiser.n + 1:
        return None

    src = line[:noiser.n] + line[-noiser.n:]
    if line[noiser.n] in noiser.vocab:
        trg = line[noiser.n]
    else:
        trg = None
    dist = noiser.get_dist(src, trg)

    print('output:')
    xs1 = noiser.vocab[2:28]
    xs2 = noiser.vocab[28:54]
    xs3 = noiser.vocab[54:62] + ['' for _ in range(26-8)]
    ys1 = dist[2:28]
    ys2 = dist[28:54]
    ys3 = list(dist[54:62]) + [0.0 for _ in range(26-8)]
    tab = [
            [
                x1, y1,
                x2, y2,
                x3, y3,
                ]
            for x1, y1, x2, y2, x3, y3
            in zip(xs1, ys1, xs2, ys2, xs3, ys3)]
    return tabulate(tab)

def main():
    parser = ArgumentParser()
    parser.add_argument('n', type=int)
    parser.add_argument('score_path')
    parser.add_argument('--T', type=float, default=1.0)
    args = parser.parse_args()

    noiser = FalsLiterNoiser(args.n, args.score_path, args.T)
    while x := infer(noiser):
        print(x)

