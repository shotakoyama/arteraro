from .job import RTTForeJobScript, RTTBackJobScript
from arteraro.auxt.script import RunScript, SubScript
from arteraro.auxt.util.load import load_config, check_sub_config
from arteraro.auxt.rtt.util import (
        get_rtt_indices,
        get_rtt_segments,
        get_bridge_language_list)

class RTTForeRunScript(RunScript):
    def make_path(self):
        return 'fore.sh'

class RTTBackRunScript(RunScript):
    def make_path(self):
        return 'back.sh'

class RTTTranslationSubScript(SubScript):
    def __init__(self, group, script_list):
        self.group = group
        super().__init__(script_list)

    def make_h_rt(self):
        return self.sub_config['translate']['h_rt']

    def make_node(self):
        return self.sub_config['translate'].get('node', 'rt_G.small')

class RTTForeSubScript(RTTTranslationSubScript):
    def make_path(self):
        return 'fore.{}.sh'.format(self.group)

class RTTBackSubScript(RTTTranslationSubScript):
    def make_path(self):
        return 'back.{}.sh'.format(self.group)

def make_script_list(job_script_class):
    return [job_script_class(lang, index, segment)
            for index in get_rtt_indices()
            for segment in get_rtt_segments()
            for lang in get_bridge_language_list()]

def get_num_translation_groups():
    config = load_config()
    return config['translation_groups']

def rtt_sub_translation(sub_script_class, script_list):
    num_groups = get_num_translation_groups()
    width = (len(script_list) - 1) // num_groups + 1
    for group in range(num_groups):
        script_sub_list = script_list[group * width : (group + 1) * width]
        sub_script = sub_script_class(group, script_sub_list)

def rtt_fore():
    script_list = make_script_list(RTTForeJobScript)
    if check_sub_config():
        rtt_sub_translation(RTTForeSubScript, script_list)
    else:
        run_script = RTTForeRunScript(script_list)

def rtt_back():
    script_list = make_script_list(RTTBackJobScript)
    if check_sub_config():
        rtt_sub_translation(RTTBackSubScript, script_list)
    else:
        run_script = RTTBackRunScript(script_list)

