from .sampler import *

class Mistaker:
    def __init__(self, name):
        self.name = name

    def add_history(self, token):
        token.history.append(self.name)
        for additional_token in token.addition:
            additional_token.history.append(self.name)
        return token


class TokenWiseMistaker(Mistaker):
    def check(self, token, cand):
        return token.word() != cand

    def preprocess(self, token, cand):
        return cand

    def __call__(self, token):
        cand = self.mistake(token)
        if cand is not None and self.check(token, cand):
            cand = self.preprocess(token, cand)
            token.org = cand
            token = self.add_history(token)
        return token


class TokenWiseMistakerCaseFitted:
    def check(self, token, cand):
        return token.word().lower() != cand.lower()

    def preprocess(self, token, cand):
        if token.word().istitle():
            cand = cand.title()
        return cand


class IndexWiseMistaker(Mistaker):
    def __call__(self, sent, index):
        sent = self.mistake(sent, index)
        sent[index] = self.add_history(sent[index])
        return sent


class SpanWiseMistaker(Mistaker):
    def __call__(self, sent, span):
        sent = self.mistake(sent, span)
        for index in span:
            sent[index] = self.add_history(sent[index])
        return sent


class MistakeSamplable:
    def mistake(self, token):
        return self.sampler()


class MistakerWordConditionable:
    def word_cond(self, token):
        raise NotImplementedError


class MistakerChoiceSamplable(MistakeSamplable):
    def __init__(self, name, choice_list, p = None, buffer_size = None):
        super().__init__(name)
        self.sampler = ChoiceSampler(choice_list, p = p, buffer_size = buffer_size)


class MistakerWordConditionedChoiceSamplable(MistakerWordConditionable, MistakerChoiceSamplable):
    def __init__(self, name, choice_list, word_cond, p = None, buffer_size = None):
        super().__init__(name, choice_list, p = p, buffer_size = buffer_size)
        self.word_cond = word_cond


class MistakerReplacable:
    def __init__(self, name, target):
        super().__init__(name)
        self.target = target

    def mistake(self, token):
        return self.target


class MistakerWordConditionedReplacable(MistakerReplacable):
    def __init__(self, name, target, word_cond):
        super().__init__(name, target)
        self.word_cond = word_cond


class CaseFittingTokenWiseMistaker(TokenWiseMistakerCaseFitted, TokenWiseMistaker):
    pass


class ChoiceSamplingTokenWiseMistaker(MistakerChoiceSamplable, TokenWiseMistaker):
    pass


class ChoiceSamplingCaseFittingTokenWiseMistaker(MistakerChoiceSamplable, CaseFittingTokenWiseMistaker):
    pass


class WordConditionedChoiceSamplingTokenWiseMistaker(MistakerWordConditionedChoiceSamplable, TokenWiseMistaker):
    pass


class WordConditionedChoiceSamplingCaseFittingTokenWiseMistaker(MistakerWordConditionedChoiceSamplable, CaseFittingTokenWiseMistaker):
    pass


class ChoiceSamplingIndexWiseMistaker(MistakerChoiceSamplable, IndexWiseMistaker):
    pass


class WordConditionedChoiceSamplingIndexWiseMistaker(MistakerWordConditionedChoiceSamplable, IndexWiseMistaker):
    pass


class ReplacingTokenWiseMistaker(MistakerReplacable, TokenWiseMistaker):
    pass


class ReplacingCaseFittingTokenWiseMistaker(TokenWiseMistakerCaseFitted, ReplacingTokenWiseMistaker):
    pass


class WordConditionedReplacingTokenWiseMistaker(MistakerWordConditionedReplacable, TokenWiseMistaker):
    pass


class WordConditionedReplacingCaseFittingTokenWiseMistaker(TokenWiseMistakerCaseFitted, WordConditionedReplacingTokenWiseMistaker):
    pass

