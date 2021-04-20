from pathlib import Path
from arteraro.auxt.util.load import load_config, check_sub_config
from arteraro.auxt.util.command import spm_command, parallel_command
from .job import PrepareJobScript
from .run import PrepareRunScript
from .sub import PrepareSubScript

class MTPrepareJobScript(PrepareJobScript):
    def make(self):
        model = self.get_bpe_model_path()
        self.append('MODELPATH={}'.format(model))
        self.append('')

        source_lang, target_lang = self.get_language_pair()
        source, target = self.get_data_path_pair()
        src_spm, trg_spm = self.make_spm_commands()

        source_output = Path('{}/train.{}.gz'.format(self.index, source_lang)).resolve()
        target_output = Path('{}/train.{}.gz'.format(self.index, target_lang)).resolve()

        self.append('zcat {} \\'.format(source))
        self.append('   | {} \\'.format(src_spm))
        self.append('   | progress \\')
        self.append('   > ${SGE_LOCALDIR}/train.src')
        self.append('')
        self.append('zcat {} \\'.format(target))
        self.append('   | {} \\'.format(trg_spm))
        self.append('   | progress \\')
        self.append('   > ${SGE_LOCALDIR}/train.trg')
        self.append('')

        self.append('paste ${SGE_LOCALDIR}/train.src ${SGE_LOCALDIR}/train.trg \\')
        self.append('   | tondi --max-len {} \\'.format(self.config['prepare']['max_length']))
        self.append('   > ${SGE_LOCALDIR}/train.tsv')
        self.append('')

        self.append('cut -f 1 ${SGE_LOCALDIR}/train.tsv \\')
        self.append('   | pigz -c > {} &'.format(source_output))
        self.append('cut -f 2 ${SGE_LOCALDIR}/train.tsv \\')
        self.append('   | pigz -c > {} &'.format(target_output))
        self.append('wait')

def mt_prepare():
    config = load_config()
    num_iter = config['iter']
    script_list = [MTPrepareJobScript(n) for n in range(num_iter)]
    if check_sub_config():
        sub = PrepareSubScript(script_list)
    else:
        run = PrepareRunScript(script_list)

