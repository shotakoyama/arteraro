from erarigilo.util import *

def extract_pp(sent):
    i = 0
    pp_list = []
    while i < len(sent):
        if (sent[i].tag == 'IN'
                and sent[i].pos == 'ADP'
                and sent[i].dep == 'prep'
                and sent[i].lower != 'of'):
            lst = [i]
            i = i + 1
            while (i < len(sent)
                    and sent[i].pos in {'ADV', 'ADJ', 'DET', 'NUM', 'NOUN', 'PRON', 'PROPN'}
                    and sent[i].tag != 'WDT'):
                lst.append(i)
                i = i + 1
            if ((i >= len(sent) or sent[i].pos in {'PUNCT', 'VERB', 'AUX', 'SYM', 'X', 'SCONJ'})
                    and sent[i - 1].pos in {'PRON', 'PROPN', 'NOUN'}
                    and len(lst) >= 2):
                pp_list.append(lst)
        else:
            i = i + 1
    return pp_list


class PPWOMistaker(Mistaker):
    def __init__(self, scale):
        super().__init__('pp_wo')
        self.sampler = NormalSampler(loc = 0.0, scale = scale)

    def mistake(self, sent, pp):
        shift = round(self.sampler())
        if (0 <= min(pp) + shift) and (max(pp) + shift < len(sent)):
            if shift > 0:
                target = [x for x in range(max(pp) + 1, max(pp) + 1 + shift)]
                target_shift = - (max(pp) - min(pp) + 1)
            else:
                target = [x for x in range(min(pp) + shift, min(pp))]
                target_shift = max(pp) - min(pp) + 1
            for i in pp:
                sent[i].shift += shift
                for token in sent[i].addition:
                    token.shift += shift
            for i in target:
                sent[i].shift += target_shift
                for token in sent[i].addition:
                    token.shift += target_shift
        return sent

    def __call__(self, sent, pp):
        sent = self.mistake(sent, pp)
        for index in pp:
            sent[index] = self.add_history(sent[index])
        return sent


class PPWOApplier:
    def apply(self, sent, lottery):
        pp_list = extract_pp(sent)
        for pp in pp_list:
            if lottery():
                sent = self.mistaker(sent, pp)
        return sent


class PPWOManager(PPWOApplier, BetaManager):
    pass


class PPWOGenerator(Generator):
    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        scale = dct['scale']
        mistaker = self.mistaker_class(scale)
        manager = PPWOManager(mean, std, mistaker)
        return manager


@register('pp_wo')
def _pp_wo(dct):
    generator = PPWOGenerator(PPWOMistaker)
    return generator(dct)

