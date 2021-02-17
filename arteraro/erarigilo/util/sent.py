from json import JSONEncoder, JSONDecoder

class Sent(list):
    def __init__(self, token_list, history = None):
        super().__init__(token_list)
        if history is None:
            self.history = []
        else:
            self.history = history

    def encode(self):
        dct = {'doc' : [token.encode() for token in self], 'history' : self.history}
        return dct

    @classmethod
    def decode(cls, dct, token_class):
        doc = [token_class.decode(token) for token in dct['doc']]
        sent = cls(doc, history = dct['history'])
        return sent

