from pathlib import Path
from .job import GenerationJobScript
from arteraro.auxt.util.tokenize import tokenize_command

class WMTGenerationJobScript(GenerationJobScript):
    def __init__(self, outdir, dataset_name, src_lang, trg_lang):
        self.dataset_name = dataset_name
        self.src_lang = src_lang
        self.trg_lang = trg_lang
        super().__init__(outdir)

    def get_bpe_model_path(self):
        bpe_model_path = self.config['generate']['bpe_model_path']
        return str(Path(bpe_model_path).resolve())

    def get_generation_attributes(self):
        beam = self.config['generate']['beam']
        nbest = self.config['generate'].get('nbest', beam)
        buffer_size = self.config['generate'].get('buffer_size', 1024)
        batch_size = self.config['generate'].get('batch_size', 128)
        lenpen = self.config['generate'].get('lenpen', 0.6)
        return beam, nbest, buffer_size, batch_size, lenpen

    def make(self):
        self.append('sacrebleu -t {} -l {}-{} --echo src \\'.format(
            self.dataset_name, self.src_lang, self.trg_lang))
        self.append('   | {} \\'.format(tokenize_command(self.src_lang)))
        self.append('   | reguligilo --all --quote \\')
        bpe_model_path = self.get_bpe_model_path()
        self.append('   | pyspm-encode --model-file {} \\'.format(bpe_model_path))
        self.append('   | {} \\'.format(self.make_interactive_command()))
        self.append('   | 2yaml \\')
        self.append('   | select-best \\')
        self.append('   > output.txt')

