import numpy as np
from pathlib import Path
from fa_script.util.util import load_config
from fa_script.util.generate import make_prod_without_index, make_base_dir

class M2Result:
    def __init__(self, epoch, result_path):
        self.epoch = epoch
        with open(result_path) as f:
            x = f.readlines()
        tp, fp, fn, p, r, f = x[3].split('\t')
        self.tp = int(tp)
        self.fp = int(fp)
        self.fn = int(fn)
        self.p = float(p)
        self.r = float(r)
        self.f = float(f)

    def __lt__(self, other):
        return self.f < other.f

def main():
    config = load_config()

    indices = range(len(config['seed_list']))
    maximum_list = []
    for index in indices:
        result_list = []
        for epoch, beam, lenpen in make_prod_without_index(config):
            base_dir = make_base_dir(index, 'bea19', epoch, beam, lenpen)
            output = base_dir / 'bea19_valid.res'
            result = M2Result(epoch, output)
            result_list.append(result)
        minimum = min(result_list)
        maximum = max(result_list)
        maximum_list.append(maximum.f)
        print('index {}:\tmin {} ({}, {}, {}),\tmax {} ({}, {}, {})'.format(
            index,
            minimum.f, minimum.p, minimum.r, minimum.epoch,
            maximum.f, maximum.p, maximum.r, maximum.epoch))
    print('average: {}'.format(np.mean(maximum_list)))
