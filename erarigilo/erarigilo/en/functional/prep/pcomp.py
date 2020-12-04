from erarigilo.util import *
from .generator import *

@register('pcomp_of')
def _pcomp_of(dct):
    return generate_replacing_pcomp_generator(dct,
            name = 'pcomp_of',
            source_set = {'of'},
            target = '')

@register('pcomp_to')
def _pcomp_to(dct):
    return generate_replacing_pcomp_generator(dct,
            name = 'pcomp_to',
            source_set = {'to'},
            target = '')

@register('pcomp_on')
def _pcomp_on(dct):
    return generate_sampling_pcomp_generator(dct,
            name = 'pcomp_on',
            word_set = {'on'},
            choice_list = ['at', 'in', 'of'])

@register('pcomp_for')
def _pcomp_for(dct):
    return generate_sampling_pcomp_generator(dct,
            name = 'pcomp_for',
            word_set = {'for'},
            choice_list = ['to', 'at', 'in', 'on'],
            p = [0.4, 0.2, 0.2, 0.2])

@register('pcomp_at')
def _pcomp_at(dct):
    return generate_sampling_pcomp_generator(dct,
            name = 'pcomp_at',
            word_set = {'at'},
            choice_list = ['on', 'in', 'of'])

@register('pcomp_by')
def _pcomp_by(dct):
    return generate_sampling_pcomp_generator(dct,
            name = 'pcomp_by',
            word_set = {'by'},
            choice_list = ['at', 'in', 'on', 'of', 'from'])

