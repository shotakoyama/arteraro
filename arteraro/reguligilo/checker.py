class Checker:
    def __init__(self):
        self.char_set = set()
        for r in [range(0x20, 0x7f), range(0xa0, 0x180), [0x1c0], range(0x300, 0x370), range(0x2010, 0x2028), range(0x2030, 0x205f), range(0x20a0, 0x20d0), [0x2581, 0x25a8]]:
            for n in r:
                self.char_set.add(chr(n))

    def __call__(self, line):
        return all(char in self.char_set for char in line)


class PreChecker:
    def __init__(self):
        self.char_set1 = set()
        self.char_set2 = set()
        for r in [range(0x20, 0x7f), [0xa0, 0xad], [0x1c0], [0x2581, 0x25a8]]:
            for n in r:
                self.char_set1.add(chr(n))
        for r in [range(0x20, 0x7f), [0xa0, 0xad], range(0xc0, 0x100), [0x1c0], [0x2581, 0x25a8]]:
            for n in r:
                self.char_set2.add(chr(n))
        for char in '¢£¥¦©ª«®°±²³·¹º»¼½¾':
            self.char_set1.add(char)
            self.char_set2.add(char)
        for char in 'ČčĚěĜĝĞğŁłŃńŒœŘřŠšŹźŻżŽž':
            self.char_set2.add(char)
        for char in '‐‑‒–—―‘’‚‛“”„‟•․‥…‧′″‴‼‽⁇⁈⁉€':
            self.char_set1.add(char)
            self.char_set2.add(char)

    def check_token(self, token):
        if token.istitle():
            return all(char in self.char_set2 for char in token)
        else:
            return all(char in self.char_set1 for char in token)

    def __call__(self, line):
        return all(self.check_token(token) for token in line.split())

