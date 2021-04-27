from pathlib import Path
from arteraro.auxt.util.load import load_config
from arteraro.auxt.util.prod import make_train_indices, make_epoch_indices
from arteraro.auxt.util.run import generate_run
from .outdir import SingleOutDir
from .generation.wmt import WMTGenerationJobScript
from .generation.run import ValidGenerationRunScript, TestGenerationRunScript
from .generation.sub import ValidGenerationSubScript, TestGenerationSubScript
from .score.wmt import WMTScoreJobScript
from .score.run import ValidScoreRunScript, TestScoreRunScript
from .score.sub import ValidScoreSubScript, TestScoreSubScript

def get_attributes(phase):
    config = load_config()
    src_lang = config['generate']['source_lang']
    trg_lang = config['generate']['target_lang']
    dataset = config['generate']['dataset']
    dataset_name = config['generate']['{}_dataset'.format(phase)]
    return src_lang, trg_lang, dataset, dataset_name

def get_outdir_list(dataset, phase):
    outdir_list = [
            SingleOutDir(index, dataset, phase, epoch)
            for index in make_train_indices()
            for epoch in make_epoch_indices()]
    return outdir_list

def wmt_valid_generation():
    src_lang, trg_lang, dataset, valid_dataset = get_attributes('valid')
    script_list = [WMTGenerationJobScript(outdir, valid_dataset, src_lang, trg_lang)
            for outdir in get_outdir_list(dataset, 'valid')]
    generate_run(script_list, ValidGenerationRunScript, ValidGenerationSubScript)

def wmt_test_generation():
    src_lang, trg_lang, dataset, test_dataset = get_attributes('test')
    script_list = [WMTGenerationJobScript(outdir, test_dataset, src_lang, trg_lang)
            for outdir in get_outdir_list(dataset, 'test')]
    generate_run(script_list, TestGenerationRunScript, TestGenerationSubScript)

def wmt_valid_score():
    src_lang, trg_lang, dataset, valid_dataset = get_attributes('valid')
    script_list = [WMTScoreJobScript(outdir, valid_dataset, src_lang, trg_lang)
            for outdir in get_outdir_list(dataset, 'valid')]
    generate_run(script_list, ValidScoreRunScript, ValidScoreSubScript)

def wmt_test_score():
    src_lang, trg_lang, dataset, test_dataset = get_attributes('test')
    script_list = [WMTScoreJobScript(outdir, test_dataset, src_lang, trg_lang)
            for outdir in get_outdir_list(dataset, 'test')]
    generate_run(script_list, TestScoreRunScript, TestScoreSubScript)

