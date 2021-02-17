import pickle
import random as rd

class OrtoBruilo:
    def __init__(self, ort_dict_path, penalty):
        self.penalty = penalty
        with open(ort_dict_path, 'rb') as f:
            self.orto_dict = pickle.load(f)

    def __call__(self, word):
        if rd.random() < self.penalty:
            if word in self.orto_dict:
                cand = rd.choice(self.orto_dict[word])
            else:
                cand = word
        else:
            if len(word) > 1:
                pos = rd.randrange(1, len(word))
                cand = word[:pos] + ' ' + word[pos:]
            else:
                cand = word
        return cand

