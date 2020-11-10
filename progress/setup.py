import setuptools

setuptools.setup(
        name = 'progress',
        author = 'nymwa',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        install_requires = ['tqdm'],
        entry_points = {
            'console_scripts':[
                'progress = progress.main:main',
                ]},
            )

