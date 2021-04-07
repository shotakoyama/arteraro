import unicodedata

def make_control_code_list():
    lst = [range(0x00, 0x20), [0x7f], range(0x80, 0xa0)]
    return [chr(char) for char_list in lst for char in char_list]

def make_euro_ng_list():
    lst = [0xaa, 0xb2, 0xb3, 0xb9, 0xba]
    lst += [0x132, 0x133, 0x1c7, 0x1c8, 0x1c9, 0x1ca, 0x1cb, 0x1cc, 0x1f1, 0x1f2, 0x1f3]
    lst += [0x2024, 0x2025, 0x2026]
    return [chr(char) for char in lst]

def make_euro_char_list():
    lst = [
        range(0x0000, 0x0500),
        range(0x1d00, 0x2000),
        range(0x2000, 0x2e00),
        range(0x3000, 0x3040),
        range(0x3250, 0x3260),
        range(0x32b1, 0x32c0),
        range(0x32cc, 0x32d0),
        range(0x3371, 0x337b),
        range(0x3380, 0x33e0),
        [0x33ff],
        range(0xfb00, 0xfb07),
        range(0xfe00, 0xfe70),
        range(0xff00, 0xff5f),
        range(0xffe0, 0x10000)]
    return [chr(char) for char_list in lst for char in char_list]

def make_digraph_replace_dict():
    return {
        chr(0x1c4): chr(0x1f1) + chr(0x30c),
        chr(0x1c5): chr(0x1f2) + chr(0x30c),
        chr(0x1c6): chr(0x1f3) + chr(0x30c)}

def make_quote_replace_dict():
    return {
        chr(0x2018): "'",
        chr(0x2019): "'",
        chr(0x201a): "'",
        chr(0x201b): "'",
        chr(0x201c): '"',
        chr(0x201d): '"',
        chr(0x201e): '"',
        chr(0x201f): '"'}

def make_space_replace_dict():
    return {
        chr(0x200b): '',
        chr(0x200c): '',
        chr(0x200d): '',
        chr(0x200e): '',
        chr(0x200f): '',
        chr(0x2028): '',
        chr(0x2029): '',
        chr(0x202a): '',
        chr(0x202b): '',
        chr(0x202c): '',
        chr(0x202d): '',
        chr(0x202e): '',
        chr(0x202f): ' ',
        chr(0x205f): ' ',
        chr(0x2060): '',
        chr(0x2061): '',
        chr(0x2062): '',
        chr(0x2063): '',
        chr(0x2064): '',
        chr(0x2066): '',
        chr(0x2067): '',
        chr(0x2068): '',
        chr(0x2069): '',
        chr(0x206a): '',
        chr(0x206b): '',
        chr(0x206c): '',
        chr(0x206d): '',
        chr(0x206e): '',
        chr(0x206f): ''}

def make_punct_replace_dict():
    return {
        chr(0x00a6): '|',
        chr(0x00ad): '-',
        chr(0x01c0): '|',
        chr(0x2010): '-',
        chr(0x2011): '-',
        chr(0x2012): '-',
        chr(0x2013): '-',
        chr(0x2014): '--',
        chr(0x2015): '--',
        chr(0x2043): '-',
        chr(0x2044): '/',
        chr(0x2055): '*',
        chr(0x2212): '-',
        chr(0x2215): '/',
        chr(0x2223): '|',
        chr(0x223c): '~',
        chr(0x223d): '~',
        chr(0x223e): '~',
        chr(0x223f): '~',
        chr(0x2500): '-',
        chr(0x2502): '|'}

def normalized_euro_char_iterator():
    for src in make_euro_char_list():
        trg = unicodedata.normalize('NFKD', src)
        if src != trg:
            yield src

