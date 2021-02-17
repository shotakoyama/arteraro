from arteraro.erarigilo.util import *
import pickle
from arteraro.ortobruilo import OrtoBruilo

class DelOrthIndexWiseMistaker(Mistaker):
    def __init__(self):
        super().__init__('del_orth')

    def cond(self, sent, index):
        return True

    def __call__(self, sent, index):
        if index < len(sent) - 1:
            left = sent[index].word()
            right = sent[index + 1].word()
            if left.isalnum() and right.isalnum():
                sent[index].right_space = ''
                sent[index] = self.add_history(sent[index])
        return sent


class InsOrthTokenWiseMistaker(TokenWiseMistaker):
    def __init__(self, dict_path, penalty):
        super().__init__('ins_orth')
        self.noiser = OrtoBruilo(dict_path, penalty)

    def cond(self, token):
        return True

    def mistake(self, token):
        word = token.word()
        cand = self.noiser(word)
        if cand == word:
            cand = None
        return cand


class InsOrthTokenWiseGenerator(Generator):
    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        penalty = dct['penalty']
        dict_path = replace_environment_variable(dct['dict_path'])
        mistaker = self.mistaker_class(dict_path, penalty)
        manager = TokenWiseBetaManager(mean, std, mistaker)
        return manager


@register('del_orth')
def _del_orth(dct):
    generator = IndexWiseGenerator(DelOrthIndexWiseMistaker)
    return generator(dct)

@register('ins_orth')
def _ins_orth(dct):
    generator = InsOrthTokenWiseGenerator(InsOrthTokenWiseMistaker)
    return generator(dct)

