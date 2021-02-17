import sys
import numpy as np
from argparse import ArgumentParser
from .vocabulary import Vocabulary

def check(vocab, word):
    return all(char in vocab.index_dict for char in word)

def word_to_tuple(n, vocab, word):
    word = ['<b>'] * n + list(word) + ['<e>'] * n
    word = [vocab.index(char) for char in word]
    for tup in zip(*[word[i:] for i in range(2 * n + 1)]):
        src = list(tup[:n]) + list(tup[-n:])
        trg = tup[n]
        yield src, trg

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('n', type=int)
    parser.add_argument('src_output_path')
    parser.add_argument('trg_output_path')
    return parser.parse_args()

def main():
    args = parse_args() 

    vocab = Vocabulary()
    src = []
    trg = []
    for sent in sys.stdin:
        for word in sent.strip().split():
            if check(vocab, word):
                for s, t in word_to_tuple(args.n, vocab, word):
                    src.append(s)
                    trg.append(t)

    src = np.array(src, dtype = np.int64)
    trg = np.array(trg, dtype = np.int64)
    np.save(args.src_output_path, src)
    np.save(args.trg_output_path, trg)

