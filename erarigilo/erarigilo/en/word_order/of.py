import random as rd
from erarigilo.util import *

class OfObj:
    def __init__(self, left, center, right):
        self.left = left
        self.center = center
        self.right = right

    def check(self):
        return (self.left is not None) and (self.right is not None)

def extract_left(sent, i):
    i = i - 1
    lst = []
    if i < 0 or sent[i].pos != 'NOUN':
        return None
    while i >= 0 and sent[i].pos == 'NOUN':
        lst = [i] + lst
        i = i - 1
    while i >= 0 and sent[i].pos in {'ADJ', 'DET', 'NUM'}:
        lst = [i] + lst
        i = i - 1
    if i < 0 or (sent[i].pos in {'ADP', 'PUNCT', 'VERB'} and sent[i].lemma != 'of'):
        return lst
    return None

def extract_right(sent, i):
    i = i + 1
    lst = []
    if i >= len(sent) or sent[i].pos != 'NOUN':
        return None
    while i < len(sent) and sent[i].pos == 'NOUN':
        lst = [i] + lst
        i = i + 1
    while i < len(sent) and sent[i].pos in {'ADJ', 'DET', 'NUM'}:
        lst = [i] + lst
        i = i + 1
    if i >= len(sent) or (sent[i].pos in {'ADP', 'PUNCT', 'VERB'} and sent[i].lemma != 'of'):
        return lst
    return None

def extract_of(sent):
    i = 0
    of_list = []
    for i in range(len(sent)):
        if (sent[i].cor == 'of'
                and sent[i].tag == 'IN'
                and sent[i].pos == 'ADP'
                and sent[i].dep == 'prep'):
            of_list.append(i)
    of_obj_list = []
    for i in of_list:
        left = extract_left(sent, i)
        right = extract_right(sent, i)
        of_obj = OfObj(left, i, right)
        if of_obj.check():
            of_obj_list.append(of_obj)
    return of_obj_list


class OfWOMistaker(Mistaker):
    def __init__(self):
        super().__init__('of_wo')

    def mistake(self, sent, left, center, right):
        shift_list = []
        for i in left:
            shift_list.append(len(right) + 1)
        shift_list.append(-len(left) + len(right))
        for i in right:
            shift_list.append(-len(left) - 1)
        for i, shift in zip(left + [center] + right, shift_list):
            sent[i].shift += shift
            for token in sent[i].addition:
                token.shift += shift
        return sent

    def __call__(self, sent, left, center, right):
        sent = self.mistake(sent, left, center, right)
        for index in left + [center] + right:
            sent[index] = self.add_history(sent[index])
        return sent


class OfWOApplier:
    def apply(self, sent, lottery):
        of_obj_list = extract_of(sent)
        for of_obj in of_obj_list:
            if lottery():
                sent = self.mistaker(sent, of_obj.left, of_obj.center, of_obj.right)
        return sent


class OfWOManager(OfWOApplier, BetaManager):
    pass


class OfWOGenerator(Generator):
    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        mistaker = self.mistaker_class()
        manager = OfWOManager(mean, std, mistaker)
        return manager


@register('of_wo')
def _of_wo(dct):
    generator = OfWOGenerator(OfWOMistaker)
    return generator(dct)

