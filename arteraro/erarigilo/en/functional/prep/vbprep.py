from erarigilo.util import *
from erarigilo.en.util.token import EnToken

class VBPrepInsertingIndexWiseMistaker(IndexWiseMistaker):
    def __init__(self):
        super().__init__('post_vb_prep')
        self.sampler = ChoiceSampler(['to', 'in', 'on', 'at', 'by', 'for', 'with', 'of'])

    def cond(self, doc, index):
        return (index < len(doc) - 1
                and doc[index].tag in {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}
                and doc[index].dep in {'acl', 'advcl', 'xcomp', 'pcomp'}
                and (doc[index + 1].pos in {'NOUN', 'DET', 'ADJ', 'PROPN'}
                    or (doc[index + 1].pos == 'SCONJ'
                        and doc[index + 1].dep == 'mark')))

    def mistake(self, doc, index):
        doc[index].addition.append(
                EnToken(
                    index = doc[index].index + 0.5,
                    org = self.sampler()))
        return doc

@register('post_vb_prep')
def _post_vb_prep(dct):
    mean = dct['mean']
    std = dct['std']
    mistaker = VBPrepInsertingIndexWiseMistaker()
    manager = IndexWiseBetaManager(mean, std, mistaker)
    return manager

