import pickle
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('model', help = 'path to model')
    args = parser.parse_args()

    with open(args.model, 'rb') as f:
        model = pickle.load(f)

    while x := input():
        if x in model and len(model[x]) > 0:
            print(' '.join(model[x]))
        else:
            print('...')

