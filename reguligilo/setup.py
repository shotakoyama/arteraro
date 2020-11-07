import setuptools

setuptools.setup(
        name = 'reguligilo',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        entry_points = {
            'console_scripts':[
                'reguligilo = reguligilo.main:main',
            ]},)
