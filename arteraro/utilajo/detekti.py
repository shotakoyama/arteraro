import sys
from argparse import ArgumentParser
from fasttext import load_model

def detect(model_path, k, rev=False):
    model = load_model(model_path)
    for line in sys.stdin:
        line = line.strip()
        lang = model.predict(line, k=k)[0]
        if ('__label__en' in lang) ^ rev:
            print(line)

def main():
    parser = ArgumentParser()
    parser.add_argument('model')
    parser.add_argument('-k', type=int, default=1)
    parser.add_argument('-r', '--reverse', dest='rev', action = 'store_true')
    args = parser.parse_args()

    detect(args.model_path, args.k, args.rev)

