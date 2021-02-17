from arteraro.erarigilo.util import *
from .generator import *

@register('1plu_subj')
def _1plu_subj(dct):
    return generate_sampling_pron_generator(dct,
            name = '1plu_subj',
            word_cond = lambda token : token.norm == 'we' and token.dep in {'nsubj', 'nsubjpass', 'conj', 'appos', 'nmod', 'compound', 'attr'},
            choice_list = ['I', 'us', 'our', 'me', 'they', 'you'])

@register('1plu_pobj')
def _1plu_pobj(dct):
    return generate_sampling_pron_generator(dct,
            name = '1plu_pobj',
            word_cond = lambda token : token.norm == 'us' and token.dep == 'pobj',
            choice_list = ['we', 'ours', 'our', 'ourselves'])

@register('1plu_dobj')
def _1plu_dobj(dct):
    return generate_sampling_pron_generator(dct,
            name = '1plu_dobj',
            word_cond = lambda token : token.norm == 'us' and token.dep == 'dobj',
            choice_list = ['', 'we', 'for us', 'to us', 'on us', 'in us', 'at us', 'of us'],
            p = [0.1, 0.1, 0.3, 0.3, 0.05, 0.05, 0.05, 0.05])

@register('1plu_nsubj_obj')
def _1plu_nsubj_obj(dct):
    return generate_sampling_pron_generator(dct,
            name = '1plu_nsubj_obj',
            word_cond = lambda token : token.norm == 'us' and token.dep in {'nsubj', 'nsubjpass', 'conj', 'appos', 'nmod', 'compound', 'attr'},
            choice_list = ['', 'we', 'our'])

@register('1plu_dative')
def _1plu_dative(dct):
    return generate_sampling_pron_generator(dct,
            name = '1plu_dative',
            word_cond = lambda token : token.norm == 'us' and token.dep == 'dative',
            choice_list = ['', 'we', 'for us', 'to us', 'on us', 'in us', 'at us'],
            p = [0.1, 0.1, 0.3, 0.35, 0.05, 0.05, 0.05])

@register('1plu_poss')
def _1plu_poss(dct):
    return generate_sampling_pron_generator(dct,
            name = '1plu_poss',
            word_cond = lambda token : token.norm == 'ours',
            choice_list = ['our', 'us', 'we', 'mine', 'theirs', 'yours'])

@register('1plu_poss_det')
def _1plu_poss_det(dct):
    return generate_sampling_pron_generator(dct,
            name = '1plu_poss_det',
            word_cond = lambda token : token.norm == 'our',
            choice_list = ['', 'we', 'us', 'ours', 'a', 'the', 'an', 'theirs', 'its', 'my'])

@register('1plu_reflexive')
def _1plu_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '1plu_reflexive',
            word_cond = lambda token : token.norm == 'ourselves' and token.dep in {'dobj', 'conj', 'nsubj', 'nsubjpass', 'npadvmod', 'dative', 'attr'},
            choice_list = ['',
                'to ourselves', 'of ourselves', 'for ourselves', 'by ourselves', 'with ourselves',
                'ourself', 'to ourself', 'of ourself', 'for ourself', 'by ourself', 'with ourself',
                'us', 'our', 'ours', 'yourselves', 'myself'],
            p = [0.2, 0.1, 0.1, 0.1, 0.1, 0.1,
                0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
                0.1, 0.02, 0.02, 0.02, 0.02])

@register('1plu_appos_reflexive')
def _1plu_appos_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '1plu_appos_reflexive',
            word_cond = lambda token : token.norm == 'ourselves' and token.dep == 'appos',
            choice_list = ['', 'us', 'ourself', 'our selves', 'for ourselves', 'by ourselves'])

@register('1plu_pobj_reflexive')
def _1plu_pobj_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '1plu_pobj_reflexive',
            word_cond = lambda token : token.norm == 'ourselvel' and token.dep == 'pobj',
            choice_list = ['', 'us', 'ourself', 'our selves', 'for ourselves', 'by ourselves'])

