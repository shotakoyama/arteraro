from pathlib import Path
from arteraro.auxt.expt.job import ExptJobScript

def mlm_scoring_command(arch, detokenize, max_tokens):
    command = ['mlm-scoring']
    command.append('--arch {}'.format(arch))
    if detokenize:
        command.append('--detokenize')
    command.append('--max-tokens {}'.format(max_tokens))
    command = ' '.join(command)
    return command

class RerankingJobScript(ExptJobScript):
    def make_path(self):
        return self.outdir.make_path('rerank.sh')

    def make(self):
        arch = self.outdir.arch
        detokenize = self.config['rerank'].get('detokenize', True)
        max_tokens = self.config['rerank'].get('max_tokens', 10000)
        command = mlm_scoring_command(arch, detokenize, max_tokens)
        input_path = (self.outdir.make_outdir_path().parent / 'output.yaml').resolve()
        output_path = self.outdir.make_path('output.yaml')
        self.append('{} \\'.format(command))
        self.append('   < {} \\'.format(input_path))
        self.append('   > {}'.format(output_path))

        for l in self.config['rerank']['lambda']:
            lmil = int(l * 1000)
            self.append('mlm-reranking -l {} < {} | select_best > {} &'.format(
                l, output_path,
                self.outdir.make_path('best.{}.txt'.format(lmil))))
        self.append('wait')

