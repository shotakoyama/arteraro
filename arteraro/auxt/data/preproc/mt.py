from pathlib import Path
from arteraro.auxt.util.load import load_config, check_sub_config
from .job import PreprocessJobScript
from .run import PreprocessRunScript
from .sub import PreprocessSubScript
from .fairseq import fairseq_preprocess_command

class MTPreprocessJobScript(PreprocessJobScript):
    def make(self):
        source_lang = self.config['source_lang']
        target_lang = self.config['target_lang']

        self.append('zcat train.{}.gz > ${{SGE_LOCALDIR}}/train.src &'.format(source_lang))
        self.append('zcat train.{}.gz > ${{SGE_LOCALDIR}}/train.trg &'.format(target_lang))
        self.append('wait')
        self.append('')

        train_pref = '${SGE_LOCALDIR}/train'
        valid_pref = Path(self.config['preprocess']['valid']).resolve()
        dest_dir = Path('{}/data-bin'.format(self.index)).resolve()
        threads = self.config['threads']
        src_dict = self.make_src_dict_path()
        trg_dict = None
        joined_dict = self.config['preprocess'].get('joined_dict', True)

        command = fairseq_preprocess_command(
                source_lang,
                target_lang,
                train_pref,
                valid_pref,
                dest_dir,
                threads,
                src_dict = src_dict,
                trg_dict = trg_dict,
                joined_dict = joined_dict)
        self.append(command)


def mt_preproc():
    config = load_config()
    num_iter = config['iter']
    first_index = config['preprocess'].get('first_index', 0)

    first_script = MTPreprocessJobScript(first_index, first_index)
    script_list = [MTPreprocessJobScript(first_index, n)
            for n in range(num_iter)
            if n != first_index]

    if check_sub_config():
        first_sub = PreprocessSubScript([first_script], first=True)
        rest_sub = PreprocessSubScript(script_list)
    else:
        first_run = PreprocessRunScript([first_script], first=True)
        rest_run = PReprocessRunScript(script_list)

