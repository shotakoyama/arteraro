from erarigilo.util import *
from .mistaker import *

@register('demonstrative')
def _demonstrative(dct):
    generator = ChoiceSamplingTokenWiseGenerator(DeterminerChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct,
            name = 'demonstrative',
            word_cond = lambda token : token.lower in {'this', 'that', 'these', 'those'} and token.dep == 'det',
            choice_list = ['', 'this', 'that', 'these', 'those', 'a', 'an', 'the'])

@register('demonstrative_extra')
def _demonstrative_extra(dct):
    generator = ChoiceSamplingTokenWiseGenerator(DeterminerChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct,
            name = 'demonstrative_extra',
            word_cond = lambda token : (token.lower in {'this', 'that', 'these', 'those'}
                and token.dep in {'nsubj', 'nsubjpass', 'pobj', 'dobj', 'conj', 'appos', 'attr', 'advmod', 'ROOT', 'quantmod', 'npadvmod'}
                and token.tag != 'WDT'),
            choice_list = ['', 'this', 'that', 'these', 'those'])

