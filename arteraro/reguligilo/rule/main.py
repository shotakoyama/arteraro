import unicodedata
from argparse import ArgumentParser
from util import (
        make_control_code_list,
        make_euro_ng_list,
        make_digraph_replace_dict,
        make_quote_replace_dict,
        make_space_replace_dict,
        make_punct_replace_dict,
        normalized_euro_char_iterator)

def make_replace_dict(quote):
    replace_dict = make_space_replace_dict()
    replace_dict.update(make_punct_replace_dict())
    replace_dict.update(make_digraph_replace_dict())
    if quote:
        replace_dict.update(make_quote_replace_dict())
    return replace_dict

def make_replace_char(replace_dict):
    def replace_char(char):
        if char in replace_dict:
            char = replace_dict[char]
        return char
    return replace_char

def make_char_list(quote):
    char_list = make_control_code_list()
    char_list += list(normalized_euro_char_iterator())
    char_list += list(make_replace_dict(quote))
    char_list = list(set(char_list))
    char_list.sort()
    return char_list

def make_rule_list(quote=False):
    control_code_set = set(make_control_code_list())
    ng_euro_set = set(make_euro_ng_list())
    replace_dict = make_replace_dict(quote)
    replace_char = make_replace_char(replace_dict)

    rule_list = []
    for src in make_char_list(quote):
        if src in ng_euro_set:
            continue
        if src in control_code_set:
            trg = ''
        elif src in replace_dict:
            trg = replace_dict[src]
        else:
            trg = unicodedata.normalize('NFKD', src)
        if len(trg) > 1 and chr(0x20) in trg:
            continue
        trg = ''.join([replace_char(char) for char in trg])
        rule_list.append((src, trg))
    return rule_list

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--quote', action='store_true')
    parser.add_argument('--fore-rule', default='fore.tsv')
    parser.add_argument('--back-rule', default='back.tsv')
    args = parser.parse_args()

    rule_list = make_rule_list(args.quote)
    with open(args.fore_rule, 'w') as f:
        for src, trg in rule_list:
            line = '{}\t{}'.format(src, trg)
            print(line, file=f)

    back_dict = {}
    for src, trg in rule_list:
        if any(0x300 <= ord(char) <= 0x36f for char in trg) and all(ord(char) != 0x20 for char in trg):
            if trg not in back_dict:
                back_dict[trg] = src
    with open(args.back_rule, 'w') as f:
        for trg, src in back_dict.items():
            line = '{}\t{}'.format(trg, src)
            print(line, file=f)

