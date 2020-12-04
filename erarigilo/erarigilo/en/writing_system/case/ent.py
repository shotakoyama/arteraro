from erarigilo.util import *

def extract_ent_span(sent):
    i = 0
    span_list = []
    while i < len(sent):
        if sent[i].ent_iob == 'B':
            span = [i]
            i += 1
            while i < len(sent) and sent[i].ent_iob == 'I':
                span.append(i)
                i += 1
            span_list.append(span)
        else:
            i += 1
    return span_list


class NamedEntityCaseMistaker(SpanWiseMistaker):
    def __init__(self, ratio, threshold):
        super().__init__('ent')
        self.sampler = UniformSampler()
        self.ratio = ratio
        self.threshold = threshold

    def random_uncase(self, word):
        return ''.join([
            char.lower()
            if self.sampler() < self.threshold
            else char
            for char
            in word])

    def extract_span(self, doc):
        return extract_ent_span(doc)

    def mistake(self, sent, span):
        cond = self.sampler() < self.ratio
        for i in span:
            word = sent[i].word()
            if not word.islower() and not word.isdigit() and word.isalnum():
                if cond:
                    cand = self.random_uncase(word)
                else:
                    cand = word.lower()
                if word != cand:
                    sent[i].org = cand
        return sent


class NamedEntityCaseGenerator(Generator):
    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        ratio = dct['ratio']
        threshold = dct['threshold']
        mistaker = self.mistaker_class(ratio, threshold)
        manager = SpanWiseBetaManager(mean, std, mistaker)
        return manager


@register('ent')
def _ent(dct):
    generator = NamedEntityCaseGenerator(NamedEntityCaseMistaker)
    return generator(dct)

