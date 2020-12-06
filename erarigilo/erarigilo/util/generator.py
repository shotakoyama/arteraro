import os
from erarigilo.util.manager import *

registory = {}

def register(name):
    def register_generator(generator_function):
        assert name not in registory
        registory[name] = generator_function
        return generator_function
    return register_generator


def replace_environment_variable(path):
    path = path.replace('${SGE_LOCALDIR}', os.environ['SGE_LOCALDIR'])
    return path


class Generator:
    def __init__(self, mistaker_class):
        self.mistaker_class = mistaker_class


class TokenWiseGenerator(Generator):
    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        buffer_size = dct.get('buffer_size', None)
        mistaker = self.mistaker_class()
        manager = TokenWiseBetaManager(mean, std, mistaker)
        return manager


class IndexWiseGenerator(Generator):
    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        buffer_size = dct.get('buffer_size', None)
        mistaker = self.mistaker_class()
        manager = IndexWiseBetaManager(mean, std, mistaker)
        return manager


class SpanWiseGenerator(Generator):
    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        buffer_size = dct.get('buffer_size', None)
        mistaker = self.mistaker_class()
        manager = SpanWiseBetaManager(mean, std, mistaker)
        return manager


class ChoiceSamplingTokenWiseGenerator(Generator):
    def __call__(self, dct, name, word_cond, choice_list, p = None):
        mean = dct['mean']
        std = dct['std']
        buffer_size = dct.get('buffer_size', None)
        mistaker = self.mistaker_class(name, choice_list, word_cond = word_cond, p = p, buffer_size = buffer_size)
        manager = TokenWiseBetaManager(mean, std, mistaker)
        return manager


class ChoiceSamplingWordSetConditionedTokenWiseGenerator(Generator):
    def __call__(self, dct, name, word_set, choice_list, p = None):
        mean = dct['mean']
        std = dct['std']
        buffer_size = dct.get('buffer_size', None)
        word_cond = lambda token : token.word().lower() in word_set
        mistaker = self.mistaker_class(name, choice_list, word_cond = word_cond, p = p, buffer_size = buffer_size)
        manager = TokenWiseBetaManager(mean, std, mistaker)
        return manager


class ReplacingTokenWiseGenerator(Generator):
    def __call__(self, dct, name, source_set, target):
        mean = dct['mean']
        std = dct['std']
        word_cond = lambda token : token.word().lower() in source_set
        mistaker = self.mistaker_class(name, target, word_cond)
        manager = TokenWiseBetaManager(mean, std, mistaker)
        return manager

