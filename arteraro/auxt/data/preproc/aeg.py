from pathlib import Path
from arteraro.auxt.util.load import load_config, check_sub_config
from .job import PreprocessJobScript
from .run import PreprocessRunScript
from .sub import PreprocessSubScript
from .fairseq import fairseq_preprocess_command

class AEGPreprocessJobScript(PreprocessJobScript):
    def get_train_input_path(self):
        train_input_list = [Path(self.config['dataset']['base']) / str(self.index) / str(segment) / 'train.gz'
                for segment in range(self.config['segments'])]
        train_input_list = [str(x.resolve()) for x in train_input_list]
        return ' '.join(train_input_list)

    def make(self):
        train_input_path = self.get_train_input_path()

        self.append('zcat {} \\'.format(train_input_path))
        if 'sentences' in self.config:
            self.append('   | head -n {} \\'.format(self.config['sentences']))
        self.append('   | progress \\')
        self.append('   > ${SGE_LOCALDIR}/train.tsv ')
        self.append('')

        self.append('cut -f 1 < ${SGE_LOCALDIR}/train.tsv > ${SGE_LOCALDIR}/train.src &')
        self.append('cut -f 2 < ${SGE_LOCALDIR}/train.tsv > ${SGE_LOCALDIR}/train.trg &')
        self.append('wait')

        train_pref = '${SGE_LOCALDIR}/train'
        valid_pref = str(Path(self.config['dataset']['valid_pref']).resolve())
        dest_dir = Path('{}/data-bin'.format(self.index)).resolve()
        threads = self.config['threads']

        src_dict = self.make_dict_path('src')
        command = fairseq_preprocess_command(
                'src',
                'trg',
                train_pref,
                valid_pref,
                dest_dir,
                threads,
                src_dict = src_dict,
                trg_dict = None,
                joined_dict = True)
        self.append(command)

def aeg_preproc():
    config = load_config()
    num_iter = config['iter']

    if 'preprocess' in config:
        first_index = config['preprocess'].get('first_index', 0)
    else:
        first_index = 0

    first_script = AEGPreprocessJobScript(first_index, first_index)
    script_list = [AEGPreprocessJobScript(first_index, n)
            for n in range(num_iter)
            if n != first_index]

    if check_sub_config():
        first_sub = PreprocessSubScript([first_script], first=True)
        rest_sub = PreprocessSubScript(script_list)
    else:
        first_run = PreprocessRunScript([first_script], first=True)
        rest_run = PReprocessRunScript(script_list)

