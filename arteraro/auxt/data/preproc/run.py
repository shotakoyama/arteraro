from arteraro.auxt.script import RunScript

class PreprocessRunScript(RunScript):
    def __init__(self, script_list, first=False):
        self.first = first
        super().__init__(script_list)

    def make_path(self):
        if self.first:
            path = 'first_preprocess.sh'
        else:
            path = 'preprocess.sh'
        return path

    def make_node(self):
        return 'rt_C.large'

