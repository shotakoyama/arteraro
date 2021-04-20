from pathlib import Path
from .script import Script
from .util import add_await_script

class RunScript(Script):
    def __init__(self, script_list):
        self.script_list = script_list
        super().__init__()

    def add_job(self, path):
        path = Path(path).resolve()
        self.append('bash {}'.format(path))

    def make(self):
        for script in self.script_list:
            self.add_job(script.path)

    def footer(self):
        self.append('')

class AwaitRunScript(RunScript):
    def add_job(self, path):
        self.append('bash {} & await'.format(path))

    def get_job(self):
        return 1

    def header(self):
        self.append('#!/bin/bash')
        self.append('')
        self.append('set -ex')
        self.append('')
        self = add_await_script(self, self.get_job())


    def footer(self):
        self.append('wait')
        self.append('')

