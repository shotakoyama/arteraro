from erarigilo.util import *
from .generator import *

@register('prep_between')
def _prep_between(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_between',
            word_set = {'between'},
            choice_list = ['', 'in', 'on', 'at', 'about', 'among', 'amongst', 'amid', 'amidst'])

