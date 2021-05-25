from arteraro.auxt.expt.sub import ExptSubScript

class RerankingSubScript(ExptSubScript):
    def make_h_rt(self):
        return self.sub_config['rerank']['h_rt']

    def make_node(self):
        return self.sub_config['rerank'].get('node', 'rt_AG.small')

    def make_num_node(self):
        return self.sub_config['rerank'].get('num_node', 1)

