from pathlib import Path

class Script(list):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.header()
        self.make()

    def make(self):
        raise NotImplementedError

    def header(self):
        pass

    def __str__(self):
        return '\n'.join(self)


class RunScript(Script):
    def header(self):
        self.append('set -ex')
        if self.config.get('mode', None) == 'abci':
            self.append('. /etc/profile.d/modules.sh')
        self.append('') # 空行
        cwd = Path.cwd().resolve()
        self.append(f'cd {cwd}')
        if 'source_path' in self.config:
            env = self.config['source_path']
            self.append(f'. {env}')
        self.append('') # 空行


class SubScript(Script):
    def add(self, command, group, h_rt, node = 'rt_C.large', num_node = 1, var_dict = None):

        qsub_command = 'qsub'
        if group is not None:
            qsub_command += f' -g {group}'
        qsub_command += f' -l {node}={num_node}'
        qsub_command += f' -l h_rt={h_rt}'
        if var_dict is not None:
            v = ','.join([f'{key}={value}' for key, value in var_dict.items()])
            qsub_command += f' {v}'
        qsub_command += f' {command}'

        self.append(qsub_command)

