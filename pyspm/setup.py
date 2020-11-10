import setuptools

setuptools.setup(
        name = 'pyspm',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        install_requires = ['sentencepiece'],
        entry_points = {
            'console_scripts':[
                'pyspm_train = pyspm.pyspm:train',
                'pyspm_encode = pyspm.pyspm:encode',
                'pyspm_decode = pyspm.pyspm:decode',
                ]},
            )

