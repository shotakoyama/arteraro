import sentencepiece as spm
from argparse import ArgumentParser

def train(args):
    model_prefix = '{}.{}'.format(args.corpus_name, args.vocab_size)
    spm.SentencePieceTrainer.train(
            input = args.input,
            model_prefix = model_prefix,
            vocab_size = args.vocab_size,
            model_type = args.model_type,
            character_coverage = args.character_coverage,
            user_defined_symbols = args.user_defined_symbols,
            normalization_rule_name = args.normalization_rule_name,
            num_threads = args.num_threads,
            split_by_unicode_script = False,
            required_chars = args.required_chars)

def main():
    parser = ArgumentParser()
    parser.add_argument('--input')
    parser.add_argument('--corpus-name')
    parser.add_argument('--vocab-size', type = int)
    parser.add_argument('--model-type', default = 'bpe')
    parser.add_argument('--character-coverage', type = float, default = 1.0)
    parser.add_argument('--user-defined-symbols', default = '')
    parser.add_argument('--normalization-rule-name', default = 'identity')
    parser.add_argument('--num-threads', type = int, default = 40)
    parser.add_argument('--required-chars', default = '□▨')
    args = parser.parse_args()

    train(args)

