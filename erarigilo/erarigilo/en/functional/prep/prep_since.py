from erarigilo.util import *
from .generator import *

# prepのsinceのほとんどは時間の起源を表すので，単にfromに変えればいい
@register('prep_since')
def _prep_since(dct):
    return generate_replacing_prep_generator(dct,
            name = 'prep_since',
            source_set = {'since'},
            target = 'from')

