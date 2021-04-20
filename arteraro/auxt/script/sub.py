from pathlib import Path
from .script import Script
from arteraro.auxt.util.load import load_sub_config

def qsub_command(code_path, group, h_rt, node, num_node, p=None, var_dict=None):
    line = 'qsub'
    if group is not None:
        line += ' -g {}'.format(group)
    if p is not None:
        line += ' -p {}'.format(p)
    line += ' -l {}={}'.format(node, num_node)
    line += ' -l h_rt={}'.format(h_rt)
    if var_dict is not None:
        var_list = ['{}={}'.format(key, value) for key, value in var_dict.items()]
        var_list = ','.join(var_list)
        line += ' -v ' + var_list
    line += ' {}'.format(code_path)
    return line

class SubScript(Script):
    def __init__(self, script_list):
        self.sub_config = load_sub_config()
        self.script_list = script_list
        super().__init__()

    def make_group(self):
        return self.sub_config['group']

    def make_h_rt(self):
        return self.sub_config['h_rt']

    def make_node(self):
        return self.sub_config['node']

    def make_num_node(self):
        return self.sub_config.get('num_node', 1)

    def make_p(self):
        return None

    def make_var_dict(self, script):
        workdir = str(Path(str(script.index)).resolve())
        return {'WORKDIR': workdir, 'IS_SGE': 'yes'}

    def add_qsub(self, script):
        path = Path(script.path).resolve()
        group = self.make_group()
        h_rt = self.make_h_rt()
        node = self.make_node()
        num_node = self.make_num_node()
        p = self.make_p()
        var_dict = self.make_var_dict(script)
        self.append(qsub_command(path, group, h_rt, node, num_node, p=p, var_dict=var_dict))

    def header(self):
        self.append('#!/bin/bash')
        self.append('')
        self.append('set -ex')
        self.append('')
        self.append('cd $(dirname $0)')
        self.append('BASEDIR=$(pwd)')
        self.append('')

    def make(self):
        for script in self.script_list:
            self.add_qsub(script)

