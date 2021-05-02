from pathlib import Path
from arteraro.auxt.script import JobScript, RunScript, SubScript
from arteraro.auxt.util.load import load_config
from arteraro.auxt.util.run import generate_run
from arteraro.auxt.rtt.util import (
        get_num_indices,
        get_num_segments,
        get_bridge_language_list)

class RTTJoinJobScript(JobScript):
    localdir = True

    def __init__(self, index, segment):
        self.index = index
        self.segment = segment
        super().__init__()

    def make_path(self):
        return '{}/{}/join.sh'.format(self.index, self.segment)

    def get_source_file_path(self, lang):
        return str(Path('{}/{}/{}/source.gz'.format(self.index, self.segment, lang)).resolve())

    def get_target_file_path(self, lang):
        return str(Path('{}/{}/{}/target.gz'.format(self.index, self.segment, lang)).resolve())

    def make_extracted_files(self):
        for lang in get_bridge_language_list():
            source = self.get_source_file_path(lang)
            self.append('zcat {} | sacremoses -l en detokenize | nltk-detokenize > ${{SGE_LOCALDIR}}/source.{}'.format(source, lang))

        for lang in get_bridge_language_list():
            target = self.get_target_file_path(lang)
            self.append('zcat {} | cut -f 2 > ${{SGE_LOCALDIR}}/target.{}'.format(target, lang))

    def get_source_file_list(self):
        source_file_list = ['${{SGE_LOCALDIR}}/source.{}'.format(lang) for lang in get_bridge_language_list()]
        return ':'.join(source_file_list)

    def get_target_file_list(self):
        target_file_list = ['${{SGE_LOCALDIR}}/target.{}'.format(lang) for lang in get_bridge_language_list()]
        return ':'.join(target_file_list)

    def make(self):
        self.make_extracted_files()

        source_file_list = self.get_source_file_list()
        target_file_list = self.get_target_file_list()

        self.append('kunigi \\')
        self.append('   {} \\'.format(source_file_list))
        self.append('   {}'.format(target_file_list))


def rtt_join():
    script_list = [RTTJoinJobScript(index, segment)
            for index in get_num_indices()
            for segment in get_num_segments()]

