from pathlib import Path
from .job import ScoreJobScript

class WMTScoreJobScript(ScoreJobScript):
    def __init__(self, outdir, dataset_name, src_lang, trg_lang):
        self.dataset_name = dataset_name
        self.src_lang = src_lang
        self.trg_lang = trg_lang
        super().__init__(outdir)

    def make(self):
        self.append('cat {} \\'.format(self.outdir.make_path('output.txt')))
        self.append('   | sacremoses -l {} detokenize \\'.format(self.trg_lang))
        self.append('   | sacrebleu -t {} -l {}-{} \\'.format(
            self.dataset_name, self.src_lang, self.trg_lang))
        self.append('   | tee result.txt')

