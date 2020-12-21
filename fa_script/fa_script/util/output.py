from pathlib import Path
from fa_script.util.qsub import qsub_command
from fa_script.util.script import SubScript
from fa_script.util.generate import make_prod, make_base_dir

class OutputSubScript(SubScript):
    def __init__(self, dataset, config, sub_config, eval_config):
        self.dataset = dataset
        self.eval_config = eval_config
        super().__init__(config, sub_config)

    def make(self):
        prod = make_prod(self.config)
        for index, epoch, beam, lenpen in prod:
            base_dir = make_base_dir(index, self.dataset, epoch, beam, lenpen)
            code_path = base_dir / '{}_{}.sh'.format(self.phase_abbrev, self.dataset)
            group = self.sub_config['group']
            h_rt = self.sub_config[self.phase]['h_rt']
            node = self.sub_config[self.phase].get('node', self.default_node)
            num_node = self.sub_config[self.phase].get('num_node', self.default_num_node)
            workdir = str(base_dir)
            p = self.sub_config[self.phase].get('p', None)
            var_dict = {'WORKDIR': workdir, 'SGE_QSUB': 'yes'}
            command = qsub_command(code_path, group, h_rt, node, num_node, p=p, var_dict=var_dict)
            self.append(command)

class GenerateSubScript(OutputSubScript):
    def __init__(self, dataset, config, sub_config, eval_config):
        self.phase = 'generate'
        self.phase_abbrev = 'gen'
        self.default_node = 'rt_G.small'
        self.default_num_node = 1
        super().__init__(dataset, config, sub_config, eval_config)

class ScoreSubScript(OutputSubScript):
    def __init__(self, dataset, config, sub_config, eval_config):
        self.phase = 'score'
        self.phase_abbrev = 'score'
        self.default_node = 'rt_C.small'
        self.default_num_node = 1
        super().__init__(dataset, config, sub_config, eval_config)

