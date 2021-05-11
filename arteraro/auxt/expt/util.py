from arteraro.auxt.util.prod import make_train_indices, make_epoch_indices
from .outdir import SingleOutDir

def get_single_valid_outdir_list(dataset, phase):
    outdir_list = [
            SingleOutDir(index, dataset, phase, epoch)
            for index in make_train_indices()
            for epoch in make_epoch_indices()]
    return outdir_list

