from pathlib import Path
from arteraro.auxt.script import JobScript, RunScript, SubScript
from arteraro.auxt.util.load import check_sub_config

class SplitJobScript(JobScript):
    localdir = True

    def make_path(self):
        return 'job.sh'

    def make(self):
        input_path = str(Path(self.config['input_path']).resolve())
        self.append('zcat {} > ${{SGE_LOCALDIR}}/corpus.txt'.format(input_path))
        self.append('')

        num_iter = self.config['iter']
        self.append('split -d -nl/{} ${{SGE_LOCALDIR}}/corpus.txt ${{SGE_LOCALDIR}}/split.'.format(num_iter))
        self.append('')

        for i in range(num_iter):
            suffix_length = max(2, len(str(num_iter - 1)))
            i_filled = str(i).zfill(suffix_length)
            self.append('gzip -c < ${{SGE_LOCALDIR}}/split.{} > split.{}.gz &'.format(i_filled, i))
        self.append('wait')
        self.append('')

class SplitRunScript(RunScript):
    def make_path(self):
        return 'split.sh'

class SplitSubScript(SubScript):
    def make_workdir(self, script):
        return str(Path().resolve())

    def make_path(self):
        return 'split.sh'

    def make_node(self):
        return self.sub_config.get('node', 'rt_C.large')

def split():
    job_script = SplitJobScript()
    if check_sub_config():
        sub_script = SplitSubScript([job_script])
    else:
        run_script = SplitRunScript([job_script])

