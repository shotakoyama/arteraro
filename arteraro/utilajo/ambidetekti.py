import gzip
from tqdm import tqdm
from argparse import ArgumentParser
from fasttext import load_model

def xopen(filepath, m, z):
    if z:
        f = gzip.open(filepath, '{}t'.format(m))
    else:
        f = open(filepath, m)
    return f

def main():
    parser = ArgumentParser()
    parser.add_argument('model')
    parser.add_argument('src_lang')
    parser.add_argument('trg_lang')
    parser.add_argument('src_input')
    parser.add_argument('trg_input')
    parser.add_argument('src_output')
    parser.add_argument('trg_output')
    parser.add_argument('-k', type=int, default=1)
    parser.add_argument('-r', '--reverse', dest='rev', action = 'store_true')
    parser.add_argument('-z', action='store_true')
    args = parser.parse_args()

    model = load_model(args.model)
    src_label = '__label__{}'.format(args.src_lang)
    trg_label = '__label__{}'.format(args.trg_lang)
    with    xopen(args.src_input, 'r', args.z) as si, \
            xopen(args.trg_input, 'r', args.z) as ti, \
            xopen(args.src_output, 'w', args.z) as so, \
            xopen(args.trg_output, 'w', args.z) as to:
        for src, trg in tqdm(zip(si, ti)):
            src = src.strip()
            trg = trg.strip()
            src_lang = model.predict(src, k=args.k)[0]
            trg_lang = model.predict(trg, k=args.k)[0]
            if ((src_label in src_lang) and (trg_label in trg_lang)) ^ args.rev:
                print(src, file = so)
                print(trg, file = to)

