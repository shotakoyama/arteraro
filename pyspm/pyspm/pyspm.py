import sentencepiece as spm
import sys
from argparse import ArgumentParser

# pyspm_encode
def encode():
    parser = ArgumentParser()
    parser.add_argument('--model_file')
    parser.add_argument('--let-unk', action = 'store_true')
    parser.add_argument('--dropout', type = float, default = None)
    args = parser.parse_args()
    sp = spm.SentencePieceProcessor(model_file = args.model_file)
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

# pyspm_decode
def decode():
    parser = ArgumentParser()
    parser.add_argument('--model_file')
    args = parser.parse_args()
    sp = spm.SentencePieceProcessor(model_file = args.model_file)
    for x in sys.stdin:
        x = x.strip()
        x = sp.decode(x.split(' '))
        print(x)

# pyspm_train
def train():
    parser = ArgumentParser()
    parser.add_argument('--input')
    parser.add_argument('--corpus_name')
    parser.add_argument('--vocab_size', type = int)
    parser.add_argument('--model_type', default = 'bpe')
    parser.add_argument('--character_coverage', type = float, default = 1.0)
    parser.add_argument('--user_defined_symbols', default = '')
    parser.add_argument('--normalization_rule_name', default = 'identity')
    parser.add_argument('--required_chars', default = '□▨')
    args = parser.parse_args()
    spm.SentencePieceTrainer.train(
            input = args.input,
            model_prefix = args.corpus_name + '.' + str(args.vocab_size),
            vocab_size = args.vocab_size,
            model_type = args.model_type,
            character_coverage = args.character_coverage,
            user_defined_symbols = args.user_defined_symbols,
            normalization_rule_name = args.normalization_rule_name,
            num_threads = 40,
            split_by_unicode_script = False,
            required_chars = args.required_chars,
            )

