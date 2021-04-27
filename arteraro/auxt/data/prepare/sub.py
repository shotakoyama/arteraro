from arteraro.auxt.data.sub import DataSubScript

class PrepareSubScript(DataSubScript):
    def make_path(self):
        return 'prepare.sh'

    def make_node(self):
        return 'rt_C.large'

