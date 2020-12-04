import setuptools

setuptools.setup(
        name = 'afiksilo',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        entry_points = {
            'console_scripts':[
                'afiksilo = afiksilo.afiksilo:main',
                'afiksilo_prepare = afiksilo.prepare:main',
                'afiksilo_make_model = afiksilo.make:main',
            ]},)
