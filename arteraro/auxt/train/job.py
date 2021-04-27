from pathlib import Path
from arteraro.auxt.script import JobScript

class TrainJobScript(JobScript):
    def __init__(self, index, num_node):
        self.index = index
        self.num_node = num_node
        super().__init__()

    def make_path(self):
        return '{}/job.sh'.format(self.index)

    def make(self):
        if self.num_node == 1:
            line = 'sh worker.sh'
        else:
            line = 'mpirun --map-by ppr:1:node -np {} sh worker.sh $(hostname -f)'.format(self.num_node)
        self.append(line)

