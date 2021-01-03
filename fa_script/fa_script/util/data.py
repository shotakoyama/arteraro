from pathlib import Path
from fa_script.util.script import SubScript
from fa_script.util.qsub import qsub_command

class DataSubScript(SubScript):
    def __init__(self, indices):
        self.indices = indices
        super().__init__()

    def make(self):
        for n in self.indices:
            base_dir = Path(str(n)).resolve()
            code_path = base_dir / 'data.sh'
            group = self.sub_config['group']
            h_rt = self.sub_config['h_rt']
            node = self.sub_config.get('node', 'rt_C.large')
            num_node = self.sub_config.get('num_node', 1)
            var_dict = {'SGE_QSUB': 'yes'}
            command = qsub_command(code_path, group, h_rt, node, num_node, var_dict=var_dict)
            self.append(command)

