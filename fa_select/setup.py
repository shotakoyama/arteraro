import setuptools

setuptools.setup(
        name = 'fa_select',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        entry_points = {
            'console_scripts':[
                'fairseq_to_yaml = fa_select.to_yaml:main',
                'roberta_rescore = fa_select.rescore:main',
                'select_best = fa_select.select:main',
                'select_with_lambda = fa_select.select:rescore',
            ]},)
