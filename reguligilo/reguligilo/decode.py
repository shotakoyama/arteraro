import sys
from .util import load_reverse

def decode():
    rule = load_reverse()
    for line in sys.stdin:
        line = line.strip()
        for src, trg in rule:
            line = line.replace(src, trg)
        print(line)

