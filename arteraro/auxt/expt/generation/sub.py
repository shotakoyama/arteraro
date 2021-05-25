from arteraro.auxt.expt.sub import ExptSubScript

class GenerationSubScript(ExptSubScript):
    def make_h_rt(self):
        return self.sub_config['generate']['h_rt']

    def make_node(self):
        return self.sub_config['generate'].get('node', 'rt_G.small')

    def make_num_node(self):
        return self.sub_config['generate'].get('num_node', 1)

# ValidGenerationSubScript and TestGenerationSubScript is used
# for wmt experiment. So do not remove them.
# method "make_path" should be implemented using PathInterface,
# but it is not repaired. This is TODO.
class ValidGenerationSubScript(GenerationSubScript):
    def make_path(self):
        return 'generate_valid.sh'

class TestGenerationSubScript(GenerationSubScript):
    def make_path(self):
        return 'generate_test.sh'

# EnsembleGenerationSubScript is used
# for GEC experiment. Be careful that it is not used for wmt.
class EnsembleGenerationSubScript(GenerationSubScript):
    def make_h_rt(self):
        return self.sub_config['generate'].get(
                'ensemble_h_rt',
                self.sub_config['generate']['h_rt'])

    def make_node(self):
        return self.sub_config['generate'].get('node', 'rt_AG.small')

