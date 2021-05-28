from arteraro.auxt.util.prod import make_train_indices, make_epoch_indices
from .outdir import (
        SingleOutDir,
        EnsembleOutDir,
        EnsembleRerankingOutDir)

def get_single_valid_outdir_list(dataset):
    outdir_list = [
            SingleOutDir(index, dataset, 'valid', epoch)
            for index in make_train_indices()
            for epoch in make_epoch_indices()]
    return outdir_list

def get_best_valid_epoch_indices(valid_result_table):
    epoch_indices = [max(result_list).outdir.epoch
            for result_list in valid_result_table]
    return epoch_indices

def get_single_test_outdir_list(dataset, valid_result_table):
    epoch_indices = get_best_valid_epoch_indices(valid_result_table)

    train_indices = make_train_indices()
    if len(train_indices) != len(epoch_indices):
        raise RuntimeError

    outdir_list = [
            SingleOutDir(index, dataset, 'test', epoch)
            for index, epoch in zip(train_indices, epoch_indices)]

    return outdir_list

def get_ensemble_outdir(dataset, phase, valid_result_table = None):
    if valid_result_table is None:
        epoch_indices = None
    else:
        epoch_indices = get_best_valid_epoch_indices(valid_result_table)
    outdir = EnsembleOutDir(dataset, phase, epoch_indices)
    return outdir

def get_ensemble_reranking_outdir(dataset, phase, arch):
    arch_name_dict = {
            'bert_base_uncased': 'bert-base-uncased',
            'bert_large_uncased': 'bert-large-uncased',
            'bert_base_cased': 'bert-base-cased',
            'bert_large_cased': 'bert-large-cased',
            'roberta_base': 'roberta-base',
            'roberta_large': 'roberta-large',
            'distilroberta_base': 'distilroberta-base',
            'distilbert_base_uncased': 'distilbert-base-uncased',
            'distilbert_base_cased': 'distilbert-base-cased',
            'albert_base_v1': 'albert-base-v1',
            'albert_large_v1': 'albert-large-v1',
            'albert_xlarge_v1': 'albert-xlarge-v1',
            'albert_xxlarge_v1': 'albert-xxlarge-v1',
            'albert_base_v2': 'albert-base-v2',
            'albert_large_v2': 'albert-large-v2',
            'albert_xlarge_v2': 'albert-xlarge-v2',
            'albert_xxlarge_v2': 'albert-xxlarge-v2'}
    arch_name = arch_name_dict[arch]
    outdir = EnsembleRerankingOutDir(dataset, phase, arch_name)
    return outdir

