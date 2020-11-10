import sys
from .util import load_rule
from .checker import Checker, PreChecker

class Encoder:
    def __init__(self):
        self.rule = load_rule()

    def __call__(self, xs):
        return ''.join([self.rule[x] if x in self.rule else x for x in xs])

def encode(limit=False, rev=False, full=False, rm_zero=False):
    if limit:
        prechecker = PreChecker()
    checker = Checker()

    encoder = Encoder()
    for line in sys.stdin:
        line = line.strip()
        if (not limit) or prechecker(line):
            line = encoder(line)
            if (checker(line) ^ rev) or full:
                line = ' '.join(line.split())
                if (not rm_zero) or len(line) > 0:
                    print(line)

