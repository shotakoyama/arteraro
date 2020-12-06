import sys
import yaml
from argparse import ArgumentParser
from erarigilo.util import *
from erarigilo.en import *

def main():
    parser = ArgumentParser()
    parser.add_argument('-c', '--config', dest = 'config', default = 'config.yaml')
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.safe_load(f)

    generator_list = []
    for dct in config:
        for key, value in dct.items():
            generator_list.append((registory[key], value))
    noiser = EnNoiser(*generator_list)

    batch = sys.stdin.readlines()
    batch = noiser(batch)
    for sent in batch:
        print(sent)

