import sys
import sentencepiece as spm
from pathlib import Path
from argparse import ArgumentParser

def encode(args):
    sp = spm.SentencePieceProcessor(model_file = str(Path(args.model_file).resolve()))

    for x in sys.stdin:
        x = x.strip()
        if args.let_unk:
            if args.dropout is None:
                x = sp.encode(x, out_type = str)
            else:
                x = sp.encode(x, out_type = str, enable_sampling = True, alpha = args.dropout)
            x = ' '.join(x)
        else:
            if args.dropout is None:
                x = sp.encode(x, out_type = int)
            else:
                x = sp.encode(x, out_type = int, enable_sampling = True, alpha = args.dropout)
            x = ' '.join([sp.IdToPiece(i) for i in x])
        print(x)

def main():
    parser = ArgumentParser()
    parser.add_argument('--model-file')
    parser.add_argument('--let-unk', action = 'store_true')
    parser.add_argument('--dropout', type = float, default = None)
    args = parser.parse_args()

    encode(args)

