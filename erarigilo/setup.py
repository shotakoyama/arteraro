import setuptools

setuptools.setup(
        name = 'erarigilo',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        entry_points = {
            'console_scripts':[
                'erg_paste = erarigilo.paste:main',
                'en_erg_form = erarigilo.en.form:main',
                'en_erg_tokenizer = erarigilo.en.preprocess:tokenization',
                'en_erg_preprocess = erarigilo.en.preprocess:main',
                'en_erg_noise = erarigilo.en.noise:main',
                'en_erg_pj = erarigilo.en.pj:main',
            ]},)
