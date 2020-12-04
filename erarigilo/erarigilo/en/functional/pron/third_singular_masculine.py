from erarigilo.util import *
from .generator import *

@register('3sng_masc_subj')
def _3sng_masc_subj(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_masc_subj',
            word_cond = lambda token : token.norm == 'he' and token.dep in {'nsubj', 'nsubjpass', 'conj', 'appos', 'nmod', 'compound', 'attr'},
            choice_list = ['she', 'his', 'him', 'they', 'them', 'their'])

@register('3sng_masc_pobj')
def _3sng_masc_pobj(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_masc_pobj',
            word_cond = lambda token : token.norm == 'him' and token.dep == 'pobj',
            choice_list = ['her', 'he', 'his', 'their', 'them', 'himself'])

@register('3sng_masc_dobj')
def _3sng_masc_dobj(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_masc_dobj',
            word_cond = lambda token : token.norm == 'him' and token.dep == 'dobj',
            choice_list = ['', 'her', 'he', 'for him', 'to him', 'on him', 'in him', 'at him', 'of him'],
            p = [0.1, 0.05, 0.05, 0.3, 0.3, 0.05, 0.05, 0.05, 0.05])

@register('3sng_masc_nsubj_obj')
def _3sng_masc_nsubj_obj(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_masc_nsubj_obj',
            word_cond = lambda token : token.norm == 'him' and token.dep in {'nsubj', 'nsubjpass', 'conj', 'appos', 'nmod', 'compound', 'attr'},
            choice_list = ['', 'her', 'he', 'his'])

@register('3sng_masc_dative')
def _3sng_masc_dative(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_masc_dative',
            word_cond = lambda token : token.norm == 'him' and token.dep == 'dative',
            choice_list = ['', 'her', 'he', 'for him', 'to him', 'on him', 'in him', 'at him'],
            p = [0.1, 0.05, 0.05, 0.3, 0.35, 0.05, 0.05, 0.05])

@register('3sng_masc_poss')
def _3sng_masc_poss(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_masc_poss',
            word_cond = lambda token : token.norm == 'his',
            choice_list = ['', 'he', 'him', 'her', 'a', 'an', 'the', 'its', 'theirs'])

@register('3sng_masc_reflexive')
def _3sng_masc_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_masc_reflexive',
            word_cond = lambda token : token.norm == 'himself' and token.dep in {'dobj', 'conj', 'nsubj', 'nsubjpass', 'npadvmod', 'dative', 'attr'},
            choice_list = ['',
                'to himself', 'of himself', 'for himself', 'by himself', 'with himself',
                'himselves', 'to himselves', 'of himselves', 'for himselves', 'by himselves', 'with himselves',
                'themself', 'to themself', 'of themself', 'for themself', 'by themself', 'with themself',
                'he', 'his', 'him', 'herself'],
            p = [0.2, 0.1, 0.1, 0.1, 0.1, 0.1,
                0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                0.045, 0.045, 0.045, 0.045])

@register('3sng_masc_appos_reflexive')
def _3sng_masc_appos_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_masc_appos_reflexive',
            word_cond = lambda token : token.norm == 'himself' and token.dep == 'appos',
            choice_list = ['', 'him', 'themself', 'him self', 'for himself', 'by himself', 'herself'])

@register('3sng_masc_pobj_reflexive')
def _3sng_masc_pobj_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_masc_pobj_reflexive',
            word_cond = lambda token : token.norm == 'himself' and token.dep == 'pobj',
            choice_list = ['him', 'him self', 'themself', 'he', 'herself'])

