from arteraro.erarigilo.util import *
from .mistaker import *

@register('det_no')
def _det_no(dct):
    generator = ChoiceSamplingTokenWiseGenerator(DeterminerChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct,
            name = 'det_no',
            word_cond = lambda token : token.lower == 'no',
            choice_list = ['not', 'non', 'any'])

@register('det_any')
def _det_any(dct):
    generator = ChoiceSamplingTokenWiseGenerator(DeterminerChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct,
            name = 'det_any',
            word_cond = lambda token : token.lower == 'any',
            choice_list = ['', 'some', 'every', 'a', 'an', 'all', 'anything'],
            p = [0.4, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])

@register('det_some')
def _det_some(dct):
    generator = ChoiceSamplingTokenWiseGenerator(DeterminerChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct,
            name = 'det_some',
            word_cond = lambda token : token.lower == 'some',
            choice_list = ['', 'a', 'an', 'the', 'those', 'these', 'few', 'little', 'something', 'somewhere', 'much', 'many', 'so'],
            p = [0.4, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])

@register('det_all')
def _det_all(dct):
    generator = ChoiceSamplingTokenWiseGenerator(DeterminerChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct,
            name = 'det_all',
            word_cond = lambda token : token.lower == 'all',
            choice_list = ['both', 'each', 'every'])

@register('det_both')
def _det_both(dct):
    generator = ChoiceSamplingTokenWiseGenerator(DeterminerChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct,
            name = 'det_both',
            word_cond = lambda token : token.lower == 'both',
            choice_list = ['', 'all', 'each', 'every'])

@register('det_each')
def _det_each(dct):
    generator = ChoiceSamplingTokenWiseGenerator(DeterminerChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct,
            name = 'det_each',
            word_cond = lambda token : token.lower == 'each',
            choice_list = ['', 'all', 'both', 'every'])

@register('det_every')
def _det_every(dct):
    generator = ChoiceSamplingTokenWiseGenerator(DeterminerChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct,
            name = 'det_every',
            word_cond = lambda token : token.lower == 'every',
            choice_list = ['', 'all', 'both', 'each'])

