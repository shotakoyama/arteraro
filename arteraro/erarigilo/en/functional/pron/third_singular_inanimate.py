from arteraro.erarigilo.util import *
from .generator import *

@register('3sng_inan_subj')
def _3sng_inan_subj(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_inan_subj',
            word_cond = lambda token : token.norm == 'it' and token.dep in {'nsubj', 'nsubjpass', 'conj', 'appos', 'nmod', 'compound', 'attr'},
            choice_list = ['', 'its', 'they', 'he', 'she', 'this', 'that', 'which'])

@register('3sng_inan_pobj')
def _3sng_inan_pobj(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_inan_pobj',
            word_cond = lambda token : token.norm == 'it' and token.dep == 'pobj',
            choice_list = ['its', 'them', 'him', 'her', 'this', 'that', 'which'])

@register('3sng_inan_dobj')
def _3sng_inan_dobj(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_inan_dobj',
            word_cond = lambda token : token.norm == 'it' and token.dep == 'dobj',
            choice_list = ['', 'its', 'them', 'him', 'her', 'this', 'that', 'which', 'for it', 'to it', 'on it', 'in it', 'at it', 'of it'])

@register('3sng_inan_dative')
def _3sng_inan_dative(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_inan_dative',
            word_cond = lambda token : token.norm == 'it' and token.dep == 'dative',
            choice_list = ['', 'its', 'her', 'him', 'them', 'for it', 'to it', 'on it', 'in it', 'at it'])

@register('3sng_inan_poss')
def _3sng_inan_poss(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_inan_poss',
            word_cond = lambda token : token.norm == 'its',
            choice_list = ['', 'it', 'theirs', 'their', 'his', 'hers', 'whose', 'a', 'an', 'the'])

@register('3sng_inan_reflexive')
def _3sng_inan_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_inan_reflexive',
            word_cond = lambda token : token.norm == 'itself' and token.dep in {'dobj', 'conj', 'nsubj', 'nsubjpass', 'npadvmod', 'dative', 'attr'},
            choice_list = ['',
                'to itself', 'of itself', 'for itself', 'by itself', 'with itself',
                'themself', 'to themself', 'of themself', 'for themself', 'by themself', 'with themself',
                'themselves', 'to themselves', 'of themselves', 'for themselves', 'by themselves', 'with themselves',
                'itselves', 'to itselves', 'of itselves', 'for itselves', 'by itselves', 'with itselves',
                'himself', 'to himself', 'of himself', 'for himself', 'by himself', 'with himself',
                'herself', 'to herself', 'of herself', 'for herself', 'by herself', 'with herself',
                'she', 'her', 'hers',
                'he', 'him', 'his'],
            p = [0.2, 0.1, 0.1, 0.1, 0.1, 0.1,
                0.005, 0.005, 0.005, 0.005, 0.005, 0.005,
                0.005, 0.005, 0.005, 0.005, 0.005, 0.005,
                0.005, 0.005, 0.005, 0.005, 0.005, 0.005,
                0.005, 0.005, 0.005, 0.005, 0.005, 0.005,
                0.005, 0.005, 0.005, 0.005, 0.005, 0.005,
                0.025, 0.025, 0.025, 0.025, 0.025, 0.025])

@register('3sng_inan_appos_reflexive')
def _3sng_inan_appos_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_inan_appos_reflexive',
            word_cond = lambda token : token.norm == 'itself' and token.dep == 'appos',
            choice_list = ['', 'it', 'they', 'them', 'themselves', 'it self', 'for itself', 'by itself', 'themself', 'herself', 'himself'])

@register('3sng_inan_pobj_reflexive')
def _3sng_inan_pobj_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_inan_pobj_reflexive',
            word_cond = lambda token : token.norm == 'itself' and token.dep == 'pobj',
            choice_list = ['it', 'it self', 'herself', 'himself'])

