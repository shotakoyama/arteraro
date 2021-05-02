from pathlib import Path
from arteraro.auxt.script import JobScript, RunScript, SubScript
from arteraro.auxt.util.load import load_config
from arteraro.auxt.util.run import generate_run

class RTTSplitJobScript(JobScript):
    localdir = True

    def __init__(self, index):
        self.index = index
        super().__init__()

    def make_path(self):
        return '{}/split.sh'.format(self.index)

    def make(self):
        input_data_path = str(Path(self.config['input_data'] + '.{}.gz'.format(self.index)).resolve())
        self.append('zcat {} > ${{SGE_LOCALDIR}}/corpus.txt'.format(input_data_path))
        self.append('')

        num_threads = self.config['threads']
        num_lines = self.config['lines']

        self.append('parallel --pipe -j {} -k --L {} "en-tokenize" \\'.format(num_threads, num_lines))
        self.append('   < ${SGE_LOCALDIR}/corpus.txt \\')
        self.append('   > ${SGE_LOCALDIR}/tokenized.txt')
        self.append('')

        num_segments = self.config['segments']
        self.append('split -d -nl/{} ${{SGE_LOCALDIR}}/tokenized.txt ${{SGE_LOCALDIR}}/split.'.format(num_segments))
        self.append('')

        for i in range(num_segments):
            suffix_length = max(2, len(str(num_segments - 1)))
            i_filled = str(i).zfill(suffix_length)
            output_dir_path = str(Path('{}/{}'.format(self.index, i)).resolve())
            output_file_path = str(Path('{}/{}/split.gz'.format(self.index, i)).resolve())
            self.append('mkdir -p {}'.format(output_dir_path))
            self.append('pigz -c < ${{SGE_LOCALDIR}}/split.{} > {} &'.format(i_filled, output_file_path))
        self.append('wait')

class RTTSplitRunScript(RunScript):
    def make_path(self):
        return 'split.sh'

class RTTSplitSubScript(SubScript):
    def make_path(self):
        return 'split.sh'

    def make_h_rt(self):
        return self.sub_config['split']['h_rt']

    def make_node(self):
        return self.sub_config['split'].get('node', 'rt_C.large')

def rtt_split():
    config = load_config()

    num_indices = config['indices']
    script_list = [RTTSplitJobScript(index) for index in range(num_indices)]
    generate_run(script_list,
            RTTSplitRunScript,
            RTTSplitSubScript)

