import setuptools

setuptools.setup(
        name = 'arteraro',
        version = '1.0.0',
        packages = setuptools.find_packages(),
        entry_points = {
            'console_scripts':[
                # afiksilo
                'afiksilo = arteraro.afiksilo.afiksilo:main',
                'afiksilo_prepare = arteraro.afiksilo.prepare:main',
                'afiksilo_make_model = arteraro.afiksilo.make:main',
                # en_erg_script
                'en_erg_script = arteraro.en_erg_script.script:main',
                # erarigilo
                'erg_paste = arteraro.erarigilo.paste:main',
                'en_erg_form = arteraro.erarigilo.en.form:main',
                'en_erg_tokenizer = arteraro.erarigilo.en.preprocess:tokenization',
                'en_erg_preprocess = arteraro.erarigilo.en.preprocess:main',
                'en_erg_noise = arteraro.erarigilo.en.noise:main',
                'en_erg_pj = arteraro.erarigilo.en.pj:main',
                # fa_script
                'fa_data_pretrain = arteraro.fa_script.data.pretrain:main',
                'fa_data_finetune = arteraro.fa_script.data.finetune:main',
                'fa_train_pretrain = arteraro.fa_script.train.pretrain:main',
                'fa_train_finetune = arteraro.fa_script.train.finetune:main',
                'fa_convert_eval_config = arteraro.fa_script.convert_eval_config:main',
                'fa_generate_valid = arteraro.fa_script.generate.main:valid',
                'fa_generate_test = arteraro.fa_script.generate.main:test',
                'fa_score_valid = arteraro.fa_script.score.main:valid',
                'fa_score_test = arteraro.fa_script.score.main:test',
                'fa_ensemble = arteraro.fa_script.ensemble.main:main',
                'fa_rescore = arteraro.fa_script.rescore.main:main',
                'fa_result_bea19 = arteraro.fa_script.result.bea19:main',
                'fa_result_conll = arteraro.fa_script.result.conll:main',
                'fa_result_fce = arteraro.fa_script.result.fce:main',
                'fa_result_jfleg = arteraro.fa_script.result.jfleg:main',
                'fa_errant_cat2 = arteraro.fa_script.errant.cat2:main',
                # fa_select
                'fairseq_to_yaml = artetaro.fa_select.to_yaml:main',
                'roberta_rescore = arteraro.fa_select.rescore:main',
                'select_best = arteraro.fa_select.select:main',
                'rescore_with_lambda = arteraro.fa_select.select:rescore',
                # falsliter
                'falsliter-data-split = arteraro.falsliter.data_split:main',
                'falsliter-preprocess = arteraro.falsliter.preprocess:main',
                'falsliter-data-merge = arteraro.falsliter.data_merge:main',
                'falsliter-train = arteraro.falsliter.train:main',
                'falsliter-dump = arteraro.falsliter.dump:main',
                'falsliter-merge-model = arteraro.falsliter.merge_model:main',
                'falsliter-dist = arteraro.falsliter.dist:main',
                'falsliter-sample = arteraro.falsliter.sample:main',
                # m2_to_text
                'm2_to_src = arteraro.m2_to_text.main:m2_to_src',
                'm2_to_trg = arteraro.m2_to_text.main:m2_to_trg',
                'remove_identical = arteraro.m2_to_text.main:remove_identical',
                # ortobruilo
                'ortobruilo = arteraro.ortobruilo.main:main',
                'ortobruilo-sample = arteraro.ortobruilo.main:sample',
                'ortobruilo-prepare = arteraro.ortobruilo.main:prepare',
                # progress
                'progress = arteraro.progress.main:main',
                # pyspm
                'pyspm_train = arteraro.pyspm.pyspm:train',
                'pyspm_encode = arteraro.pyspm.pyspm:encode',
                'pyspm_decode = arteraro.pyspm.pyspm:decode',
                # reguligilo
                'reguligilo = artetaro.reguligilo.main:encode_main',
                'malreguligilo = arteraro.reguligilo.main:decode_main',
                ]},)
