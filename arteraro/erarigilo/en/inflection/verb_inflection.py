from arteraro.erarigilo.util import *
from arteraro.erarigilo.en.util.token import EnToken
import random as rd
from lemminflect import getInflection, getAllInflections, getAllInflectionsOOV

def sample_verb(tag_list, source_tag, source):
    tag_list = [tag for tag in tag_list if tag != source_tag]
    tag = rd.choice(tag_list)
    cand_list = getInflection(source, tag)
    if cand_list == []:
        cand_list = getAllInflectionsOOV(source, upos = 'VERB').values()
    if len(cand_list) > 0:
        cand = rd.choice(cand_list)
    else:
        cand = None
    return cand


class VerbInflectionMistaker(Mistaker):
    def __init__(self, aux_ratio):
        super().__init__('verb_infl')
        self.tag_list = {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}
        self.aux_ratio = aux_ratio
        self.sampler = UniformSampler()
        contr_haves = [q + x for x in ['ve', 's', 'd'] for q in ["'", chr(0x2019)]]
        self.vbg_sampler = ChoiceSampler(contr_haves + [
            'have', 'has', 'had',  'have been', 'have be', 'have being', 'has been', 'has be', 'has being', 'had been', 'had be', 'had being', 'be', 'am', 'is', 'are', 'was', 'were'])
        self.vbn_sampler = ChoiceSampler(contr_haves + [
            'have been', 'have be', 'have being', 'has been', 'has be', 'has being', 'had been', 'had be', 'had being', 'be', 'am', 'is', 'are', 'was', 'were'])

    def cond(self, sent, index):
        return sent[index].tag in self.tag_list

    def __call__(self, sent, index):
        # get word
        if sent[index].org is not None:
            word = sent[index].org
        else:
            word = sent[index].lemma

        # get cand
        cand = None
        source = word.lower()
        if source != '':
            source_tag = sent[index].tag
            tag_list = [tag for tag in self.tag_list if tag != source_tag]
            tag = rd.choice(tag_list)
            cand_list = getInflection(source, tag)
            if cand_list == []:
                cand_list = getAllInflectionsOOV(source, upos = 'VERB').values()
            if len(cand_list) > 0:
                cand = rd.choice(cand_list)

        # replace to cand
        if cand is not None:
            if word.istitle():
                cand = cand.title()
            sent[index].org = cand
            if ((index >= 1 and sent[index - 1].pos != 'AUX')
                and (index >= 2 and sent[index - 2].pos != 'AUX')
                and self.sampler() < self.aux_ratio): # 直前にAUXがなくVBG, VBNなら"have (been)"の変化を直前に挿入する
                if tag == 'VBG':
                    sent[index].addition.append(EnToken(index = sent[index].index - 0.25, org = self.vbg_sampler()))
                elif tag == 'VBN':
                    sent[index].addition.append(EnToken(index = sent[index].index - 0.25, org = self.vbn_sampler()))
            sent[index] = self.add_history(sent[index])
        return sent


class VerbInflectionGenerator(Generator):
    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        aux_ratio = dct['aux_ratio']
        mistaker = self.mistaker_class(aux_ratio)
        manager = IndexWiseBetaManager(mean, std, mistaker)
        return manager


@register('verb_infl')
def _verb_infl(dct):
    generator = VerbInflectionGenerator(VerbInflectionMistaker)
    return generator(dct)

