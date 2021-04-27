from pathlib import Path
from arteraro.auxt.expt.job import ExptJobScript
from .fairseq import fairseq_interactive_command

class GenerationJobScript(ExptJobScript):
    def make_path(self):
        return self.outdir.make_path('generate.sh')

    def get_data_bin(self):
        path = Path(self.config['data']) / '0' / 'data-bin'
        return str(Path(path).resolve())

    def make_interactive_command(self):
        data_bin = self.get_data_bin()
        beam, nbest, buffer_size, batch_size, lenpen = self.get_generation_attributes()

        command = fairseq_interactive_command(
                data_bin,
                self.outdir.get_checkpoint_path(),
                beam,
                nbest,
                buffer_size, 
                batch_size,
                lenpen)
        return command

