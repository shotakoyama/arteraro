from arteraro.auxt.expt.util import (
        get_single_valid_outdir_list,
        get_single_test_outdir_list,
        get_ensemble_outdir,
        get_ensemble_reranking_outdir)
from arteraro.auxt.util.run import generate_run
from arteraro.auxt.expt.reranking.util import (
        get_arch_list,
        get_lambda_list)

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

def ensemble_score(dataset, phase,
        result_table_factory_class,
        score_job_script_class,
        score_run_script_class,
        score_sub_script_class):
    valid_result_table = result_table_factory_class().make(dataset, 'valid')
    outdir = get_ensemble_outdir(dataset, phase, valid_result_table)
    script_list = [score_job_script_class(outdir)]
    generate_run(script_list,
            score_run_script_class,
            score_sub_script_class)

def valid_ensemble_score(dataset,
        result_table_factory_class,
        score_job_script_class,
        score_run_script_class,
        score_sub_script_class):
    ensemble_score(dataset, 'valid',
            result_table_factory_class,
            score_job_script_class,
            score_run_script_class,
            score_sub_script_class)

def test_ensemble_score(dataset,
        result_table_factory_class,
        score_job_script_class,
        score_run_script_class,
        score_sub_script_class):
    ensemble_score(dataset, 'test',
            result_table_factory_class,
            score_job_script_class,
            score_run_script_class,
            score_sub_script_class)

def ensemble_reranked_score(dataset, phase,
        score_job_script_class,
        score_run_script_class,
        score_sub_script_class):
    arch_list = get_arch_list()
    outdir_list = [get_ensemble_reranking_outdir(dataset, phase, arch)
            for arch in arch_list]
    lambda_list = get_lambda_list()
    script_list = [score_job_script_class(outdir, l)
            for outdir in outdir_list
            for l in lambda_list]
    generate_run(script_list,
            score_run_script_class,
            score_sub_script_class)

