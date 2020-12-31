import setuptools

setuptools.setup(
        name = 'fa_script',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        entry_points = {
            'console_scripts':[
                'fa_data_pretrain = fa_script.data.pretrain:main',
                'fa_data_finetune = fa_script.data.finetune:main',
                'fa_train_pretrain = fa_script.train.pretrain:main',
                'fa_train_finetune = fa_script.train.finetune:main',
                'fa_convert_eval_config = fa_script.convert_eval_config:main',
                'fa_generate_valid = fa_script.generate.main:valid',
                'fa_generate_test = fa_script.generate.main:test',
                'fa_score_valid = fa_script.score.main:valid',
                'fa_score_test = fa_script.score.main:test',
                'fa_ensemble = fa_script.ensemble.main:main',
                'fa_rescore = fa_script.rescore.main:main',
                'fa_result_bea19 = fa_script.result.bea19:main',
                'fa_result_conll = fa_script.result.conll:main',
                'fa_result_fce = fa_script.result.fce:main',
                'fa_result_jfleg = fa_script.result.jfleg:main',
            ]},)
