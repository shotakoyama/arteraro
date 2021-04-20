from pathlib import Path
from arteraro.auxt.script import JobScript

class DataJobScript(JobScript):
    localdir = True

    def __init__(self, index):
        self.index = index
        super().__init__()

    def get_bpe_model_path(self):
        return Path(self.config['prepare']['bpe_model']).resolve()

    def get_source_language(self):
        return self.config.get('source_lang', 'src')

    def get_target_language(self):
        return self.config.get('target_lang', 'trg')

    def get_language_pair(self):
        source_lang = self.get_source_language()
        target_lang = self.get_target_language()
        return source_lang, target_lang

    def get_threads(self):
        return self.config['threads']

    def get_lines(self):
        return self.config['lines']

