from .job import RTTForeJobScript, RTTBackJobScript
from arteraro.auxt.script import RunScript, SubScript
from arteraro.auxt.util.load import load_config
from arteraro.auxt.util.run import generate_run
from arteraro.auxt.rtt.util import (
        get_num_indices,
        get_num_segments,
        get_bridge_language_list)

class RTTForeInterface:
    def make_path(self):
        return 'fore.sh'

class RTTBackInterface:
    def make_path(self):
        return 'back.sh'

class RTTTranslationSubScript(SubScript):
    def make_h_rt(self):
        return self.sub_config['translate']['h_rt']

    def make_node(self):
        return self.sub_config['translate'].get('node', 'rt_G.small')

class RTTForeRunScript(RunScript, RTTForeInterface):
    pass

class RTTBackRunScript(RunScript, RTTBackInterface):
    pass

class RTTForeSubScript(RTTTranslationSubScript, RTTForeInterface):
    pass

class RTTBackSubScript(RTTTranslationSubScript, RTTBackInterface):
    pass

def make_script_list(job_script_class):
    return [job_script_class(lang, index, segment)
            for lang in get_bridge_language_list()
            for index in get_num_indices()
            for segment in get_num_segments()]

def rtt_fore():
    script_list = make_script_list(RTTForeJobScript)
    generate_run(script_list,
            RTTForeRunScript,
            RTTForeSubScript)

def rtt_back():
    script_list = make_script_list(RTTBackJobScript)
    generate_run(script_list,
            RTTBackRunScript,
            RTTBackSubScript)

