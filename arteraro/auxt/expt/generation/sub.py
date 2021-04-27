from arteraro.auxt.expt.sub import ExptSubScript

class GenerationSubScript(ExptSubScript):
    def make_h_rt(self):
        return self.sub_config['generate']['h_rt']

    def make_node(self):
        return self.sub_config['generate'].get('node', 'rt_G.small')

    def make_num_node(self):
        return self.sub_config['generate'].get('num_node', 1)

class ValidGenerationSubScript(GenerationSubScript):
    def make_path(self):
        return 'generate_valid.sh'

class TestGenerationSubScript(GenerationSubScript):
    def make_path(self):
        return 'generate_test.sh'

class EnsembleGenerationSubScript(GenerationSubScript):
    def make_path(self):
        return 'generate_ensemble.sh'

