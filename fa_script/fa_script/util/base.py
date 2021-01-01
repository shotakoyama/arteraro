from pathlib import Path

def make_base_dir(index, dataset, stage, epoch):
    return Path(str(index)).resolve() / dataset / stage / str(epoch)

def make_ensemble_base_dir(dataset, stage):
    return Path('ensemble').resolve() / dataset / stage

