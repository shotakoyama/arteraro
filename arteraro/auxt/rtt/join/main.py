from pathlib import Path
from arteraro.auxt.script import JobScript, RunScript, SubScript
from arteraro.auxt.util.load import load_config, check_sub_config
from arteraro.auxt.rtt.util import (
        get_rtt_indices,
        get_rtt_segments,
        get_bridge_language_list)

class RTTJoinJobScript(JobScript):
    localdir = True

    def __init__(self, index, segment):
        self.index = index
        self.segment = segment
        super().__init__()

    def make_path(self):
        return '{}/{}/join.sh'.format(self.index, self.segment)

    def make_extracted_files(self):
        for lang in get_bridge_language_list():
            source = str(Path('{}/{}/{}/source.gz'.format(self.index, self.segment, lang)).resolve())
            self.append('zcat {} | sacremoses -l en detokenize | nltk-detokenize | progress > ${{SGE_LOCALDIR}}/source.{} &'.format(source, lang))
        self.append('wait')
        self.append('')

        for lang in get_bridge_language_list():
            target = str(Path('{}/{}/{}/target.gz'.format(self.index, self.segment, lang)).resolve())
            self.append('zcat {} | progress > ${{SGE_LOCALDIR}}/target.{} &'.format(target, lang))
        self.append('wait')
        self.append('')

    def make(self):
        self.make_extracted_files()

        source_file_list = ':'.join(['${{SGE_LOCALDIR}}/source.{}'.format(lang) for lang in get_bridge_language_list()])
        target_file_list = ':'.join(['${{SGE_LOCALDIR}}/target.{}'.format(lang) for lang in get_bridge_language_list()])

        self.append('kunigi \\')
        self.append('   {} \\'.format(source_file_list))
        self.append('   {} \\'.format(target_file_list))
        self.append('   | progress \\')
        self.append('   > ${SGE_LOCALDIR}/joined.txt')
        self.append('')

        ratio = self.config.get('ratio', 2.0)
        self.append('kuntrunki --ratio {} < ${{SGE_LOCALDIR}}/joined.txt \\'.format(ratio))
        self.append('   | pigz -c > {}'.format(str(Path('{}/{}/joined.gz'.format(self.index, self.segment)).resolve())))

class RTTJoinRunScript(RunScript):
    def make_path(self):
        return 'join.sh'

class RTTJoinSubScript(SubScript):
    def __init__(self, group, script_list):
        self.group = group
        super().__init__(script_list)

    def make_path(self):
        return 'join.{}.sh'.format(self.group)

    def make_h_rt(self):
        return self.sub_config['join']['h_rt']

    def make_node(self):
        return self.sub_config['join'].get('node', 'rt_C.small')

def rtt_run_join(script_list):
    run_script = RTTJoinRunScript(script_list)

def get_num_join_groups():
    config = load_config()
    return config['join_groups']

def rtt_sub_join(script_list):
    num_groups = get_num_join_groups()
    width = (len(script_list) - 1) // num_groups + 1
    for group in range(num_groups):
        script_sub_list = script_list[group * width : (group + 1) * width]
        sub_script = RTTJoinSubScript(group, script_sub_list)

def rtt_join():
    script_list = [RTTJoinJobScript(index, segment)
            for index in get_rtt_indices()
            for segment in get_rtt_segments()]

    if check_sub_config():
        rtt_sub_join(script_list)
    else:
        rtt_run_join(script_list)

