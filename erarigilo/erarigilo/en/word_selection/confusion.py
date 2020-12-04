from erarigilo.util import *
import pickle
import random

class ConfusionMistaker(Mistaker):
    def __init__(self, model_path):
        super().__init__('confusion')
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

    def cond(self, token):
        return token.tag in {'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}

    def __call__(self, token):
        word = token.word()
        if word in self.model and len(self.model[word]) > 0:
            cand = random.choice(self.model[word])
            if word.istitle():
                cand = cand.title()
            token.org = cand
            token = self.add_history(token)
        return token


class ConfusionGenerator(Generator):
    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        model_path = dct['model_path']
        mistaker = ConfusionMistaker(model_path)
        manager = TokenWiseBetaManager(mean, std, mistaker)
        return manager


@register('confusion')
def _confusion(dct):
    generator = ConfusionGenerator(ConfusionMistaker)
    return generator(dct)

