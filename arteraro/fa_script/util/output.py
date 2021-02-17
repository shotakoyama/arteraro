from pathlib import Path
from arteraro.fa_script.util.qsub import qsub_command
from arteraro.fa_script.util.script import SubScript
from arteraro.fa_script.util.name import make_script_name
from arteraro.fa_script.util.prod import make_epoch_list, make_prod
from arteraro.fa_script.util.base import make_base_dir, make_ensemble_base_dir
from arteraro.fa_script.util.load import load_eval_config, load_config_and_eval_config

class OutputSubScript(SubScript):
    def __init__(self, phase, dataset, default_node, default_num_node):
        self.phase = phase
        self.dataset = dataset
        self.default_node = default_node
        self.default_num_node = default_num_node
        self.eval_config = load_eval_config()
        super().__init__()

    def get_run_script_name(self):
        return '{}.sh'.format(self.phase)

    def get_h_rt(self):
        return self.sub_config[self.phase]['h_rt']

    def append_command(self, base_dir, code_path = None):
        if code_path is None:
            code_path = base_dir / self.get_run_script_name()
        group = self.sub_config['group']
        h_rt = self.get_h_rt()
        node = self.sub_config[self.phase].get('node', self.default_node)
        num_node = self.sub_config[self.phase].get('num_node', self.default_num_node)
        p = self.sub_config[self.phase].get('p', None)
        var_dict = {'SGE_QSUB': 'yes'}
        command = qsub_command(code_path, group, h_rt, node, num_node, p=p, var_dict=var_dict)
        self.append(command)

class SingleOutputSubScript(OutputSubScript):
    def __init__(self, phase, dataset, stage, default_node, default_num_node):
        self.stage = stage
        super().__init__(phase, dataset, default_node, default_num_node)

    def get_sub_script_name(self):
        return '{}_{}_{}.sh'.format(self.phase, self.dataset, self.stage)

class EnsembleOutputSubScript(SingleOutputSubScript):
    def get_sub_script_name(self):
        return '{}_{}_{}_ensemble.sh'.format(self.phase, self.dataset, self.stage)

class EnsembleValidTestOutputSubScript(OutputSubScript):
    def get_sub_script_name(self):
        return '{}_{}_ensemble.sh'.format(self.phase, self.dataset)

class OutputSubScriptGenerator:
    def __init__(self, script_class):
        self.script_class = script_class

    def __call__(self):
        sub_script = self.script_class()
        with open(sub_script.get_sub_script_name(), 'w') as f:
            f.write(str(sub_script))

class OutputRunScriptGenerator:
    def __init__(self, dataset, script_class):
        self.dataset = dataset
        self.script_class = script_class
        self.config, self.eval_config = load_config_and_eval_config()

    def write_script(self, base_dir, script):
        with open(base_dir / script.get_script_name(), 'w') as f:
            f.write(str(script))

