import sys
import random as rd

def main():
    for line in sys.stdin:
        line = line.strip()
        lst = line.split('\t')
        trg = lst[0]
        srcs = lst[1:]
        src = rd.choice(srcs)
        print(src + '\t' + trg)

