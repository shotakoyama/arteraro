import sys
import yaml
from arteraro.erarigilo.util import *
from . import *

def en_run(config):
    with open(config) as f:
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

