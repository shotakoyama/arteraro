from arteraro.erarigilo.util import *
from .generator import *

@register('prep_below')
def _prep_below(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_below',
            word_set = {'below'},
            choice_list = ['in', 'on', 'by', 'with', 'under', 'through', 'within'])

