class Token:
    def __init__(self, index, shift = 0, org = None, cor = None, addition = None, history = None):
        self.index = index
        self.shift = shift
        self.org = org
        self.cor = cor
        if addition is None:
            self.addition = []
        else:
            self.addition = addition
        if history is None:
            self.history = []
        else:
            self.history = history

    def word(self):
        if self.org is not None:
            word = self.org
        else:
            word = self.cor
        return word

    def encode(self):
        dct = {
                'i' : self.index,
                'shift' : self.shift,
                'org' : self.org,
                'cor' : self.cor,
                'addition' : [token.encode() for token in self.addition],
                'history' : self.history,
                }
        return dct

    @classmethod
    def decode(cls, dct):
        index = dct['i']
        shift = dct['shift']
        org = dct['org']
        cor = dct['cor']
        addition = [cls.decode(x) for x in dct['addition']]
        history = dct['history']
        token = cls(index, shift = shift, org = org, cor = cor, addition = addition, history = history)
        return token

