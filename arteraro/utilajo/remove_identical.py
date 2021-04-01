import sys
from argparse import ArgumentParser

def remove_identical():
    parser = ArgumentParser()
    parser.add_argument('source_input_path')
    parser.add_argument('target_input_path')
    parser.add_argument('source_output_path')
    parser.add_argument('target_output_path')
    args = parser.parse_args()

    with open(args.source_input_path) as src_in, open(args.target_input_path) as trg_in, open(args.source_output_path, 'w') as src_out, open(args.target_output_path, 'w') as trg_out:
        for src, trg in zip(src_in, trg_in):
            if src != trg:
                print(src.strip(), file = src_out)
                print(trg.strip(), file = trg_out)

