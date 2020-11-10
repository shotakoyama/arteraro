import setuptools

setuptools.setup(
        name = 'm2_to_text',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        entry_points = {
            'console_scripts':[
                'm2_to_src = m2_to_text.main:m2_to_src',
                'm2_to_trg = m2_to_text.main:m2_to_trg',
                'remove_identical = m2_to_text.main:remove_identical',
                ]},
            )

