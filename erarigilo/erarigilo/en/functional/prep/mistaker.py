from erarigilo.util import *

class MistakerInConditioned(MistakerWordConditionable):
    def cond(self, token):
        return (self.word_cond(token)
                and not token.word().isupper()
                and token.tag == 'IN'
                and self.dep_cond(token.dep))


class MistakerPrepConditioned(MistakerInConditioned):
    def dep_cond(self, dep):
        # ROOT は "In ... ." のように前置詞句自体が一文をなしているもの．大体 in か on が導く．
        # conj はよくわからないがなんかいい感じがする．
        return dep in {'prep', 'ROOT', 'conj'}


class MistakerMarkConditioned(MistakerInConditioned):
    def dep_cond(self, dep):
        return dep == 'mark'


class MistakerAgentConditioned(MistakerInConditioned):
    def dep_cond(self, dep):
        return dep == 'agent'


class MistakerPcompConditioned(MistakerInConditioned):
    def dep_cond(self, dep):
        return dep == 'pcomp'


class MistakerDativeConditioned(MistakerInConditioned):
    def dep_cond(self, dep):
        return dep == 'dative'


class MistakerAdvmodConditioned(MistakerInConditioned):
    def dep_cond(self, dep):
        return dep == 'advmod'


class PrepWordConditionedChoiceSamplingCaseFittingTokenWiseMistaker(MistakerPrepConditioned, WordConditionedChoiceSamplingCaseFittingTokenWiseMistaker):
    pass


class PrepWordConditionedReplacingCaseFittingTokenWiseMistaker(MistakerPrepConditioned, WordConditionedReplacingCaseFittingTokenWiseMistaker):
    pass


class MarkWordConditionedChoiceSamplingCaseFittingTokenWiseMistaker(MistakerMarkConditioned, WordConditionedChoiceSamplingCaseFittingTokenWiseMistaker):
    pass


class MarkWordConditionedReplacingCaseFittingTokenWiseMistaker(MistakerMarkConditioned, WordConditionedReplacingCaseFittingTokenWiseMistaker):
    pass


class AgentWordConditionedChoiceSamplingCaseFittingTokenWiseMistaker(MistakerAgentConditioned, WordConditionedChoiceSamplingCaseFittingTokenWiseMistaker):
    pass


class AgentWordConditionedReplacingCaseFittingTokenWiseMistaker(MistakerAgentConditioned, WordConditionedReplacingCaseFittingTokenWiseMistaker):
    pass


class PcompWordConditionedChoiceSamplingCaseFittingTokenWiseMistaker(MistakerPcompConditioned, WordConditionedChoiceSamplingCaseFittingTokenWiseMistaker):
    pass


class PcompWordConditionedReplacingCaseFittingTokenWiseMistaker(MistakerPcompConditioned, WordConditionedReplacingCaseFittingTokenWiseMistaker):
    pass


class DativeWordConditionedChoiceSamplingCaseFittingTokenWiseMistaker(MistakerDativeConditioned, WordConditionedChoiceSamplingCaseFittingTokenWiseMistaker):
    pass


class DativeWordConditionedReplacingCaseFittingTokenWiseMistaker(MistakerDativeConditioned, WordConditionedReplacingCaseFittingTokenWiseMistaker):
    pass


class AdvmodWordConditionedChoiceSamplingCaseFittingTokenWiseMistaker(MistakerAdvmodConditioned, WordConditionedChoiceSamplingCaseFittingTokenWiseMistaker):
    pass


class AdvmodWordConditionedReplacingCaseFittingTokenWiseMistaker(MistakerAdvmodConditioned, WordConditionedReplacingCaseFittingTokenWiseMistaker):
    pass

