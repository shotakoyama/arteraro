from arteraro.erarigilo.util import *
from .generator import *

@register('prep_beyond')
def _prep_beyond(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_beyond',
            word_set = {'beyond'},
            choice_list = ['on', 'over', 'above', 'out of', 'far from'])

