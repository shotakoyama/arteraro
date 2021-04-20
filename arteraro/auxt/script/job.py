from pathlib import Path
from .script import Script
from .util import (
        add_environmental_script,
        add_workdir_script,
        add_localdir_script)

class JobScript(Script):
    localdir = False

    def make_environment_source_path(self):
        return self.config['source']

    def header(self):
        self.append('#!/bin/bash')
        self.append('')
        self.append('set -ex')
        self.append('')
        self = add_workdir_script(self)
        self = add_environmental_script(self, self.make_environment_source_path())
        if self.localdir:
            self = add_localdir_script(self)
        self.append('set -u')
        self.append('')


class NestJobScript(JobScript):
    def __init__(self, expt, dataset, phase, epoch, width):
        self.expt = expt
        self.dataset = dataset
        self.phase = phase
        self.epoch = epoch
        self.width = width
        super().__init__()

    def make_own_file_path(self, file_path):
        return '{}/{}/{}/{}/{}/{}'.format(
                self.expt,
                self.dataset,
                self.phase,
                self.epoch,
                self.width,
                file_path)

