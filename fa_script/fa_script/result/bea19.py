import numpy as np
from pathlib import Path
from fa_script.util.util import load_config
from fa_script.util.generate import make_prod_without_index, make_base_dir, make_prod_without_index_and_epoch, make_ensemble_base_dir

class M2Result:
    def __init__(self, index, epoch, beam, lenpen, result_path):
        self.index = index
        self.epoch = epoch
        self.beam = beam
        self.lenpen = lenpen
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

class RescoredM2Result(M2Result):
    def __init__(self, index, epoch, l, beam, lenpen, result_path):
        self.l = l
        super().__init__(index, epoch, beam, lenpen, result_path)

def make_bea19_result_table(config):
    result_table = []
    indices = range(len(config['seed_list']))
    for index in indices:
        result_list = []
        for epoch, beam, lenpen in make_prod_without_index(config):
            base_dir = make_base_dir(index, 'bea19', epoch, beam, lenpen)
            output = base_dir / 'bea19_valid.res'
            result = M2Result(index, epoch, beam, lenpen, output)
            result_list.append(result)
        result_table.append(result_list)
    return result_table

def get_ensemble_bea19_result_list(config):
    result_list = []
    prod = make_prod_without_index_and_epoch(config)
    for beam, lenpen in prod:
        base_dir =  make_ensemble_base_dir('bea19', beam, lenpen)
        output = base_dir / 'bea19_valid.res'
        if output.exists():
            result = M2Result(None, None, beam, lenpen, output)
            result_list.append(result)
    return result_list

def get_rescore_bea19_result_list(config):
    result_list = []
    prod = make_prod_without_index_and_epoch(config)
    for beam, lenpen in prod:
        for l in config['rescore']['lambda']:
            base_dir = make_ensemble_base_dir('bea19', beam, lenpen)
            lmil = int(l * 1000)
            output = base_dir / 'bea19_valid_rescored.{}.res'.format(lmil)
            if output.exists():
                result = RescoredM2Result(None, None, l, beam, lenpen, output)
                result_list.append(result)
    return result_list

def main():
    config = load_config()

    result_table = make_bea19_result_table(config)
    indices = range(len(config['seed_list']))
    for index, result_list in enumerate(result_table):
        minimum = min(result_list)
        maximum = max(result_list)
        print('index {}:\tmin {} ({}, {}, {}),\tmax {} ({}, {}, {})'.format(
            index,
            minimum.f, minimum.p, minimum.r, minimum.epoch,
            maximum.f, maximum.p, maximum.r, maximum.epoch))

    ave_f = np.mean([max(result_list).f for result_list in result_table])
    ave_p = np.mean([max(result_list).p for result_list in result_table])
    ave_r = np.mean([max(result_list).r for result_list in result_table])
    print('average: {} ({}, {})'.format(ave_f, ave_p, ave_r))

    ensemble_result_list = get_ensemble_bea19_result_list(config)
    if len(ensemble_result_list) > 0:
        result = max(ensemble_result_list)
        print('ensemble: {} ({}, {})'.format(result.f, result.p, result.r))

    rescored_result_list = get_rescore_bea19_result_list(config)
    if len(rescored_result_list) > 0:
        rescored_result_list.sort(key = lambda x:x.l)
        print('rescore')
        for result in rescored_result_list:
            print('l {}: {} ({}, {})'.format(result.l, result.f, result.p, result.r))
        maximum = max(rescored_result_list)
        print('max l={}: {} ({}, {})'.format(maximum.l, maximum.f, maximum.p, maximum.r))

