from arteraro.erarigilo.util import *

def extract_wh(sent):
    i = 0
    wh_list = []
    for i in range(len(sent)):
        if sent[i].word().lower() in {'how', 'what', 'who', 'which', 'whose', 'when', 'where', 'whither', 'whence', 'why', 'whether'}:
            wh_list.append(i)
    return wh_list


class WhWOMistaker(Mistaker):
    def __init__(self, loc, scale):
        super().__init__('wh_wo')
        self.sampler = NormalSampler(loc = loc, scale = scale)

    def mistake(self, sent, index):
        shift = round(self.sampler())
        if 0 <= index + shift < len(sent):
            sent[index].shift += shift
            for token in sent[index].addition:
                token.shift += shift
        return sent

    def __call__(self, sent, index):
        sent = self.mistake(sent, index)
        sent[index] = self.add_history(sent[index])
        return sent


class WhWOApplier:
    def apply(self, sent, lottery):
        wh_list = extract_wh(sent)
        for index in wh_list:
            if lottery():
                sent = self.mistaker(sent, index)
        return sent


class WhWOManager(WhWOApplier, BetaManager):
    pass


class WhWOGenerator(Generator):
    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        loc = dct['loc']
        scale = dct['scale']
        mistaker = self.mistaker_class(loc, scale)
        manager = WhWOManager(mean, std, mistaker)
        return manager


@register('wh_wo')
def _wh_wo(dct):
    generator = WhWOGenerator(WhWOMistaker)
    return generator(dct)

