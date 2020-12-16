import setuptools

setuptools.setup(
        name = 'en_erg_script',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        entry_points = {
            'console_scripts':[
                'en_erg_script = en_erg_script.script:main',
            ]},)
