def make_base_checker():
    lst = [x for x in range(0x20, 0x7f)] # basic latin
    lst += [x for x in range(0xa0, 0x180)] # latin 1 supplement and latin extended-A
    lst += [0x1c0] # dental click (not vertical line(0x7c))
    lst += [x for x in range(0x300, 0x370)] # combining diacritical marks
    lst += [x for x in range(0x2010, 0x2028)] # general punctuation
    lst += [x for x in range(0x2030, 0x205f)] # general punctuation
    lst += [x for x in range(0x20a0, 0x20d0)] # currency symbol
    lst += [0x2581] # word boundary of sentencepiece
    lst += [0x25a1, 0x25a8] # char mask and word mask
    return lst

def make_limit_checker():
    lst = [x for x in range(0x20, 0x7f)] # basic latin
    lst += [0xa2, 0xa3, 0xa4, 0xa5, 0xa9, 0xaa, 0xab, 0xae] # latin 1 supplement
    lst += [0xb0, 0xb1, 0xb2, 0xb3, 0xb7, 0xb9, 0xba, 0xbb]
    lst += [x for x in range(0xc0, 0x100)]
    lst += [0x141, 0x142, 0x152, 0x153] # latin extended A
    lst += [0x1c0] # dental click (not vertical line(0x7c))
    lst += [x for x in range(0x300, 0x334)] # combining diacritical marks
    lst += [x for x in range(0x2018, 0x2020)] # general punctuation
    lst += [0x2022, 0x2024, 0x2025, 0x2026, 0x2027, 0x2039, 0x203a, 0x20ac]
    return lst

checker_list = {
        'base': make_base_checker,
        'limit': make_limit_checker,
    }

class Checker:
    def __init__(self, name):
        self.char_set = set()
        for n in checker_list[name]():
            self.char_set.add(chr(n))

    def __call__(self, line):
        return all(char in self.char_set for char in line)

