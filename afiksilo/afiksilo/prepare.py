import sys
from collections import Counter
from tqdm import tqdm
from argparse import ArgumentParser
import pickle

def main():
    # to count and output word frequency
    cnt = Counter()
    for x in tqdm(sys.stdin):
        x = x.strip().split()
        cnt.update(x)
    for x, f in cnt.most_common():
        print(f'{x}\t{f}')

def preprocess_vocabulary():
    parser = ArgumentParser()
    parser.add_argument('output')
    args = parser.parse_args()

    # load word frequency
    vocab = {}
    for x in sys.stdin:
        word, freq = x.strip().split('\t')
        vocab[word] = int(freq)

    # save vocabulary
    with open(args.output, 'wb') as f:
        pickle.dump(vocab, f)
