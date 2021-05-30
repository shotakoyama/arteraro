from pathlib import Path
from arteraro.auxt.data.job import DataJobScript

class PreprocessJobScript(DataJobScript):
    def __init__(self, first_index, index):
        self.first_index = first_index
        super().__init__(index)

    def make_path(self):
        return '{}/preproc.sh'.format(self.index)

    def make_dict_path(self, side):
        if (self.first_index is not None) and (self.first_index != self.index):
            dict_path = '{}/data-bin/dict.{}.txt'.format(self.first_index, side)
        elif 'preprocess' in self.config:
            dict_path = self.config['preprocess'].get('{}_dict_path'.format(side), None)
        else:
            dict_path = self.config.get('{}_dict_path'.format(side), None)

        if dict_path is not None:
            dict_path = str(Path(dict_path).resolve())
        return dict_path

    def make_src_dict_path(self):
        return self.make_dict_path('src')

    def make_trg_dict_path(self):
        return self.make_dict_path('trg')

