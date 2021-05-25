from pathlib import Path
from arteraro.auxt.util.prod import make_epoch_indices

class OutDir:
    def __init__(self, dataset):
        self.dataset = dataset

    def make_path(self, file_name):
        path = self.make_outdir_path() / file_name
        return str(Path(path).resolve())


class PhaseOutDir(OutDir):
    def __init__(self, dataset, phase):
        self.phase = phase
        super().__init__(dataset)


class SingleOutDir(PhaseOutDir):
    def __init__(self, index, dataset, phase, epoch):
        self.index = index
        self.epoch = epoch
        super().__init__(dataset, phase)

    def get_checkpoint_path(self):
        checkpoint_path = '{}/checkpoints/checkpoint{}.pt'.format(
                self.index, self.epoch)
        return str(Path(checkpoint_path).resolve())

    def make_outdir_path(self):
        path = '{}/{}/{}/{}'.format(self.index, self.dataset,
                self.phase, self.epoch)
        return Path(path)


class EnsembleOutDir(PhaseOutDir):
    def __init__(self, dataset, phase, epoch_list):
        self.epoch_list = epoch_list
        super().__init__(dataset, phase)

    def get_checkpoint_path(self):
        checkpoint_path_list = [
                '{}/checkpoints/checkpoint{}.pt'.format(index, epoch)
                for index, epoch in enumerate(self.epoch_list)]
        checkpoint_path_list = [
                str(Path(checkpoint_path).resolve())
                for checkpoint_path in checkpoint_path_list]
        return ':'.join(checkpoint_path_list)

    def make_outdir_path(self):
        path = 'ensemble/{}/{}/{}'.format(self.dataset,
                self.phase, self.epoch)
        return Path(path)


class SinglePhaseDir(PhaseOutDir):
    def __init__(self, index, dataset, phase):
        self.index = index
        self.epoch_indices = list(make_epoch_indices())
        super().__init__(dataset, phase)

    def make_outdir(self, epoch):
        return SingleOutDir(self.index, self.dataset, self.phase, epoch)

