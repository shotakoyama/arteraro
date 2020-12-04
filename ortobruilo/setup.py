import setuptools

setuptools.setup(
        name = 'ortobruilo',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        entry_points = {
            'console_scripts':[
                'ortobruilo = ortobruilo.main:main',
                'ortobruilo-sample = ortobruilo.main:sample',
                'ortobruilo-prepare = ortobruilo.main:prepare',
            ]},)
