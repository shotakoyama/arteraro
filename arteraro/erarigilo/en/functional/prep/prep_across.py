from arteraro.erarigilo.util import *
from .generator import *

@register('prep_across')
def _prep_across(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_across',
            word_set = {'across'},
            choice_list = ['beyond', 'over', 'through', 'throughout', 'during'])

