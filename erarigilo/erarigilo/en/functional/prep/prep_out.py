from erarigilo.util import *
from .generator import *

@register('prep_out')
def _prep_out(dct):
    return generate_replacing_prep_generator(dct,
            name = 'prep_out',
            source_set = {'out'},
            target = '')

