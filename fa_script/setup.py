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
                'fa_generate_bea19 = fa_script.generate.bea19:main',
                'fa_generate_conll = fa_script.generate.conll:main',
                'fa_generate_jfleg = fa_script.generate.jfleg:main',
                'fa_score_bea19 = fa_script.score.bea19:main',
                'fa_score_conll = fa_script.score.conll:main',
                'fa_score_jfleg = fa_script.score.jfleg:main',
                'fa_ensemble_bea19 = fa_script.ensemble.bea19:main',
                'fa_ensemble_conll = fa_script.ensemble.conll:main',
                'fa_ensemble_jfleg = fa_script.ensemble.jfleg:main',
                'fa_rescore_bea19 = fa_script.rescore.bea19:main',
                'fa_rescore_conll = fa_script.rescore.conll:main',
                'fa_rescore_jfleg = fa_script.rescore.jfleg:main',
            ]},)