import sys
from pathlib import Path
from argparse import ArgumentParser

def load_rule():
    rule = {}
    with open(Path(__file__).parent / 'rule.tsv') as f:
        for line in f:
            src = line[0]
            trg = line[2:-1]
            rule[src] = trg
    return rule

def load_reverse():
    rule = []
    with open(Path(__file__).parent / 'reverse.tsv') as f:
        for line in f:
            src = line[0:-3]
            trg = line[-2:-1]
            rule.append([src, trg])
    rule.sort(key = lambda x : - len(x[0]))
    return rule


class Checker:
    def __init__(self):
        self.char_set = set()
        for r in [range(0x20, 0x7f), range(0xa0, 0x180), [0x1c0], range(0x300, 0x370), range(0x2010, 0x2028), range(0x2030, 0x205f), range(0x20a0, 0x20d0), [0x2581, 0x25a8]]:
            for n in r:
                self.char_set.add(chr(n))

    def __call__(self, line):
        return all(char in self.char_set for char in line)


class PreChecker:
    def __init__(self):
        self.char_set1 = set()
        self.char_set2 = set()
        for r in [range(0x20, 0x7f), [0xa0, 0xad], [0x1c0], [0x2581, 0x25a8]]:
            for n in r:
                self.char_set1.add(chr(n))
        for r in [range(0x20, 0x7f), [0xa0, 0xad], range(0xc0, 0x100), [0x1c0], [0x2581, 0x25a8]]:
            for n in r:
                self.char_set2.add(chr(n))
        for char in '¢£¥¦©ª«®°±²³·¹º»¼½¾':
            self.char_set1.add(char)
            self.char_set2.add(char)
        for char in 'ČčĚěĜĝĞğŁłŃńŒœŘřŠšŹźŻżŽž':
            self.char_set2.add(char)
        for char in '‐‑‒–—―‘’‚‛“”„‟•․‥…‧′″‴‼‽⁇⁈⁉€':
            self.char_set1.add(char)
            self.char_set2.add(char)

    def check_token(self, token):
        if token.istitle():
            return all(char in self.char_set2 for char in token)
        else:
            return all(char in self.char_set1 for char in token)

    def __call__(self, line):
        return all(self.check_token(token) for token in line.split())


def encode(args):
    if args.limit:
        prechecker = PreChecker()
    checker = Checker()

    rule = load_rule()
    for line in sys.stdin:
        line = line.strip()
        if (not args.limit) or prechecker(line):
            line = ''.join([rule[x] if x in rule else x for x in line])
            if (checker(line) ^ args.rev) or args.all:
                line = ' '.join(line.split())
                if (not args.rm_zero) or len(line) > 0:
                    print(line)

def decode(args):
    rule = load_reverse()
    for line in sys.stdin:
        line = line.strip()
        for src, trg in rule:
            line = line.replace(src, trg)
        print(line)

def main():
    parser = ArgumentParser()
    parser.add_argument('-a', '--all', action = 'store_true')
    parser.add_argument('-r', '--rev', action = 'store_true')
    parser.add_argument('-d', '--decode', action = 'store_true')
    parser.add_argument('-l', '--limit', action = 'store_true')
    parser.add_argument('-z', '--rm-zero', action = 'store_true')
    args = parser.parse_args()

    if args.decode:
        decode(args)
    else:
        encode(args)

