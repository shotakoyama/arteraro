from arteraro.auxt.script import RunScript

class PreprocessRunScript(RunScript):
    def __init__(self, script_list, first=False):
        self.first = first
        super().__init__(script_list)

    def make_path(self):
        return 'run_preprocess.sh'

    def make_node(self):
        return 'rt_C.large'

