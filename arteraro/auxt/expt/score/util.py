from arteraro.auxt.expt.util import (
        get_single_valid_outdir_list,
        get_single_test_outdir_list,
        get_ensemble_outdir)
from arteraro.auxt.util.run import generate_run

def valid_single_score(dataset,
        score_job_script_class,
        score_run_script_class,
        score_sub_script_class):
    outdir_list = get_single_valid_outdir_list(dataset)
    script_list = [score_job_script_class(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            score_run_script_class,
            score_sub_script_class)

def test_single_score(dataset,
        result_table_factory_class,
        score_job_script_class,
        score_run_script_class,
        score_sub_script_class):
    valid_result_table = result_table_factory_class().make(dataset, 'valid')
    outdir_list = get_single_test_outdir_list(dataset, valid_result_table)
    script_list = [score_job_script_class(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            score_run_script_class,
            score_sub_script_class)

def valid_ensemble_score(dataset,
        result_table_factory_class,
        score_job_script_class,
        score_run_script_class,
        score_sub_script_class):
    valid_result_table = result_table_factory_class().make(dataset, 'valid')
    outdir = get_ensemble_outdir(dataset, 'valid', valid_result_table)
    script_list = [score_job_script_class(outdir)]
    generate_run(script_list,
            score_run_script_class,
            score_sub_script_class)

def test_ensemble_score(dataset,
        result_table_factory_class,
        score_job_script_class,
        score_run_script_class,
        score_sub_script_class):
    valid_result_table = result_table_factory_class().make(dataset, 'valid')
    outdir = get_ensemble_outdir(dataset, 'test', valid_result_table)
    script_list = [score_job_script_class(outdir)]
    generate_run(script_list,
            score_run_script_class,
            score_sub_script_class)

