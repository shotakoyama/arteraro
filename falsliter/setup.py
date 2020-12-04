import setuptools

setuptools.setup(
        name = 'falsliter',
        packages = setuptools.find_packages(),
        entry_points = {
            'console_scripts':[
                'falsliter-data-split = falsliter.data_split:main',
                'falsliter-preprocess = falsliter.preprocess:main',
                'falsliter-data-merge = falsliter.data_merge:main',
                'falsliter-train = falsliter.train:main',
                'falsliter-dump = falsliter.dump:main',
                'falsliter-merge-model = falsliter.merge_model:main',
                'falsliter-dist = falsliter.dist:main',
                'falsliter-sample = falsliter.sample:main',
                ]},
            )

