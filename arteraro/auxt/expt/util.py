from arteraro.auxt.util.prod import make_train_indices, make_epoch_indices
from .outdir import SingleOutDir

def get_single_valid_outdir_list(dataset):
    outdir_list = [
            SingleOutDir(index, dataset, 'valid', epoch)
            for index in make_train_indices()
            for epoch in make_epoch_indices()]
    return outdir_list

def get_single_test_outdir_list(dataset, valid_result_table):
    train_indices = make_train_indices()
    epoch_indices = [max(result_list).outdir.epoch
            for result_list in valid_result_table]

    if len(train_indices) != len(epoch_indices):
        raise RuntimeError

    outdir_list = [
            SingleOutDir(index, dataset, 'test', epoch)
            for index, epoch in zip(train_indices, epoch_indices)]
    return outdir_list

