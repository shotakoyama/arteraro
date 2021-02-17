from arteraro.erarigilo.util import *
from .generator import *

@register('standard_mark')
def _standard_mark(dct):
    return generate_replacing_mark_generator(dct,
            name = 'standard_mark',
            source_set = {'as', 'if', 'because', 'so', 'whether', 'while', 'since', 'although', 'than', 'though', 'once', 'whereas', 'whilst', 'like', 'except'},
            target = '')

@register('mark_for')
def _mark_for(dct):
    return generate_sampling_mark_generator(dct,
            name = 'mark_for',
            word_set = {'for'},
            choice_list = ['', 'to', 'on', 'in'],
            p = [0.2, 0.6, 0.1, 0.1])

