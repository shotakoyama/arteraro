import setuptools

setuptools.setup(
        name = 'arteraro',
        version = '1.0.1',
        packages = setuptools.find_packages(),
        entry_points = {
            'console_scripts':[
                # afiksilo
                'afiksilo = arteraro.afiksilo.afiksilo:main',
                'afiksilo_prepare = arteraro.afiksilo.prepare:main',
                'afiksilo_make_model = arteraro.afiksilo.make:main',
                # auxt
                'auxt = arteraro.auxt.main:main',
                # erg
                'erg = arteraro.erarigilo.main:main',
                # fa_select
                'fairseq_to_yaml = arteraro.fa_select.to_yaml:main',
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
                # ortobruilo
                'ortobruilo = arteraro.ortobruilo.main:main',
                'ortobruilo-sample = arteraro.ortobruilo.main:sample',
                'ortobruilo-prepare = arteraro.ortobruilo.main:prepare',
                # pyspm
                'pyspm_train = arteraro.pyspm.train:main',
                'pyspm_encode = arteraro.pyspm.encode:main',
                'pyspm_decode = arteraro.pyspm.decode:main',
                # reguligilo
                'reguligilo = arteraro.reguligilo.main:encode',
                'malreguligilo = arteraro.reguligilo.main:decode',
                # utilajo
                'en-tokenize = arteraro.utilajo.tokenize:en',
                'de-tokenize = arteraro.utilajo.tokenize:de',
                'fr-tokenize = arteraro.utilajo.tokenize:fr',
                'glui = arteraro.utilajo.glui:main',
                'progress = arteraro.utilajo.progress:main',
                'm22src = arteraro.utilajo.m22src:m2_to_src',
                'm22trg = arteraro.utilajo.m22trg:m2_to_trg',
                'remove_identical = arteraro.utilajo.remove_identical:remove_identical',
                ]},)
