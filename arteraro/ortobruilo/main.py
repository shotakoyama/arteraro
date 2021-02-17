import sys
import pickle
from argparse import ArgumentParser
from tqdm import tqdm
from .ortobruilo import OrtoBruilo 

def split_word(vocab, word):
    candidates = []
    for i in range(1, len(word)):
        left, right = word[:i], word[i:]
        if left in vocab and right in vocab:
            candidates.append(left + ' ' + right)
    return candidates

def prepare():
    parser = ArgumentParser()
    parser.add_argument('vocab', help = 'path to vocabulary')
    parser.add_argument('model', help = 'path to model')
    parser.add_argument('--min-freq', type = int, default = 1000)
    args = parser.parse_args()

    vocab = []
    with open(args.vocab, 'r') as f:
        for x in f:
            word, freq = x.strip().split('\t')
            freq = int(freq)
            if freq >= args.min_freq:
                vocab.append(word)
    vocab = set(vocab)

    orts = {}
    for word in tqdm(vocab, bar_format = '{l_bar}{r_bar}'):
        candidates = split_word(vocab, word)
        if len(candidates) > 0:
            orts[word] = candidates

    with open(args.model, 'wb') as f:
        pickle.dump(orts, f)

def sample():
    parser = ArgumentParser()
    parser.add_argument('path', help = 'path to dict')
    parser.add_argument('--penalty', type = float, default = 0.8)
    args = parser.parse_args()
    noiser = OrtoBruilo(args.path, args.penalty)
    while x := input():
        print(noiser(x)) 

def main():
    parser = ArgumentParser()
    parser.add_argument('model', help = 'path to model')
    parser.add_argument('--penalty', type = float, default = 0.8)
    args = parser.parse_args()
    noiser = OrtoBruilo(args.path, args.penalty)
    while x := input():
        if x in model:
            print(noiser.orto_dict[x])
        else:
            print('...')


