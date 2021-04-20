from arteraro.auxt.script import SubScript

class PrepareSubScript(SubScript):
    def make_path(self):
        return 'sub_prepare.sh'

    def make_node(self):
        return 'rt_C.large'

