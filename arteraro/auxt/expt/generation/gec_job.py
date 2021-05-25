import yaml
from pathlib import Path
from .job import GenerationJobScript
from arteraro.auxt.expt.job import ExptGECJobScriptInterface
from arteraro.auxt.util.tokenize import tokenize_command

class GECGenerationJobScript(ExptGECJobScriptInterface, GenerationJobScript):
    def make_path(self):
        return self.outdir.make_path('generate.sh')

    def get_beam_attributes(self):
        beam = self.config['generate'].get('beam', 12)
        nbest = self.config['generate'].get('nbest', beam)
        return beam, nbest

    def get_generation_attributes(self):
        beam, nbest = self.get_beam_attributes()
        buffer_size, batch_size = self.get_batch_size_attributes()
        lenpen = self.config['generate'].get('lenpen', 0.6)
        return beam, nbest, buffer_size, batch_size, lenpen

    def make(self):
        command = self.make_interactive_command()
        input_path = self.get_input_path()
        self.append('{} \\'.format(command))
        self.append('   < {} \\'.format(input_path))
        self.append('   | 2yaml \\')
        self.append('   | tee {} \\'.format(self.outdir.make_path('output.yaml')))
        self.append('   | select-best \\')
        self.append('   > {}'.format(self.outdir.make_path('best.txt')))


class GECSingleGenerationJobScript(GECGenerationJobScript):
    def get_batch_size_attributes(self):
        buffer_size = self.config['generate'].get('buffer_size', 1024)
        batch_size = self.config['generate'].get('batch_size', 32)
        return buffer_size, batch_size


class GECEnsembleGenerationJobScript(GECGenerationJobScript):
    def get_batch_size_attributes(self):
        buffer_size = self.config['generate'].get('buffer_size', 1024)
        batch_size = self.config['generate'].get('ensemble_batch_size',
                self.config['generate'].get('batch_size', 32))
        return buffer_size, batch_size

