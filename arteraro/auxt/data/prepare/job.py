from pathlib import Path
from arteraro.auxt.util.command import spm_command, parallel_command
from arteraro.auxt.data.job import DataJobScript

class PrepareJobScript(DataJobScript):
    def make_path(self):
        return '{}/prepare.sh'.format(self.index)

    def get_source_data_path(self):
        return str(Path(self.config['prepare']['source']).resolve())

    def get_target_data_path(self):
        return str(Path(self.config['prepare']['target']).resolve())

    def get_data_path_pair(self):
        source = self.get_source_data_path()
        target = self.get_target_data_path()
        return source, target

    def get_source_dropout_probability(self):
        return self.config['prepare'].get('source_dropout', None)

    def get_target_dropout_probability(self):
        return self.config['prepare'].get('target_dropout', None)

    def get_dropout_probabilities(self):
        source_dropout = self.get_source_dropout_probability()
        target_dropout = self.get_target_dropout_probability()
        return source_dropout, target_dropout

    def make_spm_commands(self, parallel=True):
        src_dropout, trg_dropout = self.get_dropout_probabilities()

        src_spm = spm_command('${MODELPATH}', dropout = src_dropout)
        trg_spm = spm_command('${MODELPATH}', dropout = trg_dropout)

        if parallel and 'threads' in self.config:
            j = self.get_threads()
            L = self.get_lines()
            src_spm = parallel_command(j, L, '"{}"'.format(src_spm))
            trg_spm = parallel_command(j, L, '"{}"'.format(trg_spm))

        return src_spm, trg_spm



