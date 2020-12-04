from erarigilo.util import *
from .generator import *

@register('prep_than')
def _prep_than(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_than',
            word_set = {'than'},
            choice_list = ['', 'to', 'from', 'over', 'beyond'],
            p = [0.2, 0.4, 0.2, 0.1, 0.1])

