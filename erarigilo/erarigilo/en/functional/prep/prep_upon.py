from erarigilo.util import *
from .generator import *

@register('prep_upon')
def _prep_upon(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_upon',
            word_set = {'upon'},
            choice_list = ['on', 'up', 'up on', 'over', 'after', 'to'])

