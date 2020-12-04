from erarigilo.util import *
from .generator import *

@register('prep_among')
def _prep_among(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_among',
            word_set = {'among'},
            choice_list = ['', 'in', 'on', 'at', 'about', 'between', 'amid'])

@register('prep_amongst')
def _prep_amongst(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_amongst',
            word_set = {'amongst'},
            choice_list = ['', 'in', 'on', 'at', 'about', 'between', 'amidst'])

