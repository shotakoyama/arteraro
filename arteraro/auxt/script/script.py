from pathlib import Path
from arteraro.auxt.util.load import load_config

class Script(list):
    def __init__(self):
        super().__init__()
        self.config = load_config()
        self.path = self.make_path()
        self.prepare()
        self.header()
        self.make()
        self.footer()
        self.make_dir()
        self.save()

    def prepare(self):
        pass

    def header(self):
        self.append('#!/bin/bash')
        self.append('')
        self.append('set -ex')
        self.append('')

    def footer(self):
        self.append('')

    def make_dir(self):
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)

    def save(self):
        with open (Path(self.path), 'w') as f:
            print(str(self), file=f)

    def __str__(self):
        return '\n'.join(self)


