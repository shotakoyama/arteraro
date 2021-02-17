import re 

class Vocabulary(list):
    def __init__(self):
        self.bos = '<b>'
        self.eos = '<e>'
        lst = [self.bos, self.eos]
        lst += [chr(x) for x in range(65, 91)]
        lst += [chr(x) for x in range(97, 123)]
        lst += [chr(x) for x in [0xdf, 0x142, 0x300, 0x301, 0x302, 0x303, 0x308, 0x327]]
        super().__init__(lst)
        self.index_dict = {token : index for index, token in enumerate(self)}

    def __contains__(self, x):
        return x in self.index_dict

    def index(self, x):
        return self.index_dict[x]

