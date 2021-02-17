from arteraro.erarigilo.util import *

quot = chr(0x2019)

class ContrTokenWiseMistaker(Mistaker):
    def __init__(self, delete_ratio):
        super().__init__('contr')
        self.delete_ratio = delete_ratio
        self.sampler = UniformSampler()

    def cond(self, token):
        word = token.word()
        return token.pos != 'PUNCT' and ("'" in word or quot in word)

    def __call__(self, token):
        word = token.word()
        if (word not in {q + x for x in ['m', 's', 'd', 've', 're'] for q in ["'", quot]}
                or self.sampler() > self.delete_ratio):
            cand = word.replace("'", '').replace(quot, '')
        else:
            cand = ''
        token.org = cand
        token.left_space = False
        token = self.add_history(token)
        return token


class ContrTokenWiseGenerator(Generator):
    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        delete_ratio = dct['delete_ratio']
        mistaker = self.mistaker_class(delete_ratio)
        manager = TokenWiseBetaManager(mean, std, mistaker)
        return manager


@register('contr')
def _contr(dct):
    generator = ContrTokenWiseGenerator(ContrTokenWiseMistaker)
    return generator(dct)

