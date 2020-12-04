from argparse import ArgumentParser
import numpy as np

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('src_inputs')
    parser.add_argument('trg_inputs')
    parser.add_argument('src_output')
    parser.add_argument('trg_output')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    src_inputs = args.src_inputs.split(':')
    trg_inputs = args.trg_inputs.split(':')

    np.save(args.src_output,
            np.concatenate([
                np.load(src_input)
                for src_input in src_inputs],
                axis = 0))

    np.save(args.trg_output,
            np.concatenate([
                np.load(trg_input)
                for trg_input in trg_inputs],
                axis = 0))

