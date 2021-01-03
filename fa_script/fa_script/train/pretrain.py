from pathlib import Path
from fa_script.util.load import load_config, check_sub_config, load_sub_config
from fa_script.util.prod import make_index_list
from fa_script.util.train import TrainRunScript, TrainSubScript

class PretrainRunScript(TrainRunScript):
    def __init__(self, expt_id, work_dir):
        self.sub_config = load_sub_config()
        super().__init__(expt_id, work_dir)

    def make(self):
        self.append('mpirun --map-by ppr:1:node -np {} sh worker.sh $(hostname -f)'.format(self.sub_config['train']['num_node']))

class WorkerRunScript(TrainRunScript):
    def __init__(self, expt_id, work_dir):
        self.sub_config = load_sub_config()
        super().__init__(expt_id, work_dir)

    def make(self):
        indices = self.make_indices()
        self.make_copy(indices)
        command = self.make_train_command(indices)
        command.distributed(self.sub_config['train']['num_node'])
        self.append(str(command))

def run():
    for n in make_index_list(load_config()):
        base_dir = Path(str(n)).resolve()
        base_dir.mkdir(exist_ok=True)
        main_script = PretrainRunScript(n, base_dir)
        worker_script = WorkerRunScript(n, base_dir)
        with open(base_dir / 'pretrain.sh', 'w') as f:
            f.write(str(main_script))
        with open(base_dir / 'worker.sh', 'w') as f:
            f.write(str(worker_script))

def sub():
    sub_script = TrainSubScript('pretrain')
    with open('pretrain.sh', 'w') as f:
        f.write(str(sub_script))

def main():
    run()
    if check_sub_config():
        sub()

