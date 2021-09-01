from pathlib import Path
from arteraro.auxt.script import JobScript

class TrainJobScript(JobScript):
    def __init__(self, index, num_node):
        self.index = index
        self.num_node = num_node
        super().__init__()

    def make_path(self):
        return '{}/job.sh'.format(self.index)

    def p_tmp_save(self):
        return self.config['train'].get('tmp_save_dir', False)

    def make_tmp_save_dir(self):
        return Path('${SGE_LOCALDIR}/checkpoints')

    def make(self):
        if self.p_tmp_save():
            self.append('mkdir {}'.format(self.make_tmp_save_dir()))

        if self.num_node == 1:
            line = 'sh worker.sh'
        else:
            line = 'mpirun --map-by ppr:1:node -np {} sh worker.sh $(hostname -f)'.format(self.num_node)
        self.append(line)

        if self.p_tmp_save():
            self.append('mkdir -p checkpoints')
            self.append('mv $(sh -c "ls {}") checkpoints/'.format(self.make_tmp_save_dir() / '*.pt'))

