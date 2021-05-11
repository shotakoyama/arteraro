from pathlib import Path
from arteraro.auxt.util.load import load_config
from arteraro.auxt.util.command import spm_command, parallel_command
from arteraro.auxt.util.run import generate_run
from .job import PrepareJobScript
from .run import PrepareRunScript
from .sub import PrepareSubScript

class BEA19PrepareJobScript(PrepareJobScript):
    def make(self):
        model = self.get_bpe_model_path()
        self.append('MODELPATH={}'.format(model))
        self.append('')

        train_source_input = Path(self.config['dataset']['train_source']).resolve()
        train_target_input = Path(self.config['dataset']['train_target']).resolve()
        source_spm, target_spm = self.make_spm_commands(parallel = False)

        train_source_output = Path('{}/train.src.gz'.format(self.index)).resolve()
        train_target_output = Path('{}/train.trg.gz'.format(self.index)).resolve()

        self.append('cat {} \\'.format(train_source_input))
        self.append('   | {} \\'.format(source_spm))
        self.append('   | progress \\')
        self.append('   > ${SGE_LOCALDIR}/train.src')
        self.append('')
        self.append('cat {} \\'.format(train_target_input))
        self.append('   | {} \\'.format(target_spm))
        self.append('   | progress \\')
        self.append('   > ${SGE_LOCALDIR}/train.trg')
        self.append('')

        self.append('paste ${SGE_LOCALDIR}/train.src ${SGE_LOCALDIR}/train.trg \\')
        self.append('   | tondi --max-len {} \\'.format(self.config['prepare']['max_length']))
        self.append('   > ${SGE_LOCALDIR}/train.tsv')
        self.append('')

        self.append('cut -f 1 ${SGE_LOCALDIR}/train.tsv \\')
        self.append('   | pigz -c > {} &'.format(train_source_output))
        self.append('cut -f 2 ${SGE_LOCALDIR}/train.tsv \\')
        self.append('   | pigz -c > {} &'.format(train_target_output))
        self.append('wait')

class BEA19PrepareSubScript(PrepareSubScript):
    def make_node(self):
        return 'rt_C.small'

def bea19_prepare():
    config = load_config()
    num_iter = config['iter']

    script_list = [BEA19PrepareJobScript(n) for n in range(num_iter)]
    generate_run(script_list,
            PrepareRunScript,
            BEA19PrepareSubScript)

