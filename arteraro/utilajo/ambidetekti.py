import sys
from argparse import ArgumentParser
from fasttext import load_model

def detect(model_path, src_lang, trg_lang, k=1, rev=False):
    src_label = '__label__{}'.format(src_lang)
    trg_label = '__label__{}'.format(trg_lang)
    model = load_model(model_path)

    for line in sys.stdin:
        line = line.rstrip('\n')
        src, trg = line.split('\t')
        src_lang = model.predict(src, k=k)[0]
        trg_lang = model.predict(trg, k=k)[0]
        if ((src_label in src_lang) and (trg_label in trg_lang)) ^ rev:
            line = '{}\t{}'.format(src, trg)
            print(line)

def main():
    parser = ArgumentParser()
    parser.add_argument('model')
    parser.add_argument('src_lang')
    parser.add_argument('trg_lang')
    parser.add_argument('-k', type=int, default=1)
    parser.add_argument('-r', '--reverse', dest='rev', action = 'store_true')
    args = parser.parse_args()

    detect(args.model, args.src_lang, args.trg_lang, args.k, args.rev)

