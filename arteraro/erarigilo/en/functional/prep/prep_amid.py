from arteraro.erarigilo.util import *
from .generator import *

@register('prep_amid')
def _prep_amid(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_amid',
            word_set = {'amid'},
            choice_list = ['', 'in', 'on', 'at', 'about', 'between', 'among'])

@register('prep_amidst')
def _prep_amidst(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_amidst',
            word_set = {'amidst'},
            choice_list = ['', 'in', 'on', 'at', 'about', 'between', 'amongst'])

