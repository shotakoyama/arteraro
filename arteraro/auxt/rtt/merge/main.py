from pathlib import Path
from arteraro.auxt.script import JobScript, RunScript, SubScript
from arteraro.auxt.util.run import generate_run
from arteraro.auxt.rtt.util import get_rtt_indices

class RTTMergeJobScript(JobScript):
    localdir = True

    def __init__(self, index):
        self.index = index
        super().__init__()

    def make_path(self):
        return '{}/merge.sh'.format(self.index)

    def make(self):
        num_segments = self.config['segments']
        output_path = str(Path('{}/merged.gz'.format(self.index)).resolve())

        for segment in range(num_segments):
            joined_path = str(Path('{}/{}/joined.gz'.format(self.index, segment)).resolve())
            self.append('zcat {} >> ${{SGE_LOCALDIR}}/tmp.txt'.format(joined_path))
        self.append('pigz -c < ${{SGE_LOCALDIR}}/tmp.txt > {}'.format(output_path))

class RTTMergeRunScript(RunScript):
    def make_path(self):
        return 'merge.sh'

class RTTMergeSubScript(SubScript):
    def make_path(self):
        return 'merge.sh'

    def make_h_rt(self):
        return self.sub_config['merge']['h_rt']

    def make_node(self):
        return self.sub_config['merge'].get('node', 'rt_C.small')

def rtt_merge():
    script_list = [RTTMergeJobScript(index) for index in get_rtt_indices()]
    generate_run(script_list,
            RTTMergeRunScript,
            RTTMergeSubScript)

