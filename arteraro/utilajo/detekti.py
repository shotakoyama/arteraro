import sys
from argparse import ArgumentParser
from fasttext import load_model

def detect(model_path, k=1, lang='en', rev=False):
    target_label = '__label__{}'.format(lang)
    model = load_model(model_path)
    for line in sys.stdin:
        line = line.strip()
        lang_labels = model.predict(line, k=k)[0]
        if (target_label in lang_labels) ^ rev:
            print(line)

def main():
    parser = ArgumentParser()
    parser.add_argument('model')
    parser.add_argument('-l', '--lang', default='en')
    parser.add_argument('-k', type=int, default=1)
    parser.add_argument('-r', '--reverse', dest='rev', action = 'store_true')
    args = parser.parse_args()

    detect(args.model, args.k, args.lang, args.rev)

