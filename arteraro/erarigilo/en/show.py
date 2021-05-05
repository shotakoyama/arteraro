import sys
import json
from tabulate import tabulate
from .form import form_src, form_trg
from .util.token import EnToken
from .util.sent import EnSent

def decode(sent):
    sent = sent.strip()
    sent = json.loads(sent)
    sent = EnSent.decode(sent, token_class = EnToken)
    return sent

def o_or_x(p):
    return 'o' if p else 'x'

def blank(x):
    return x if x is not None else '____'

def add_color(x):
    return '\033[31m' + x + '\033[0m'

class Conds:
    def __init__(self, color = None, cor = None, tag = None, pos = None, dep = None):
        self.color = color
        self.cor = cor
        self.tag = tag
        self.pos = pos
        self.dep = dep

    def is_free(self):
        return (self.cor is None) and (self.tag is None) and (self.pos is None) and (self.dep is None)

    def is_ok(self, token):
        return ((self.cor is None) or (self.cor == token.cor)) and ((self.tag is None) or (self.tag == token.tag)) and ((self.pos is None) or (self.pos == token.pos)) and ((self.dep is None) or (self.dep == token.dep))

    def check(self, sent):
        if self.is_free():
            return True
        return any(self.is_ok(token) for token in sent)

class Row:
    def __init__(self, cond, token):
        self.token = token
        self.left_space = o_or_x(token.left_space)
        self.right_space = o_or_x(token.right_space)
        self.org = blank(token.org)
        self.cor = blank(token.cor)
        self.tag = blank(token.tag)
        self.pos = blank(token.pos)
        self.dep = blank(token.dep)
        self.lem = blank(token.lemma)
        self.nrm = blank(token.norm)
        self.ent_type = blank(token.ent_type)
        self.ent_iob = blank(token.ent_iob)
        if len(token.history) > 0:
            self.history = ' '.join(token.history)
        else:
            self.history = '____'

        if cond.color:
            if (token.cor is not None) and (token.cor == cond.cor):
                self.cor = add_color(self.cor)
            if (token.tag is not None) and (token.tag == cond.tag):
                self.tag = add_color(self.tag)
            if (token.pos is not None) and (token.pos == cond.pos):
                self.pos = add_color(self.pos)
            if (token.dep is not None) and (token.dep == cond.dep):
                self.dep = add_color(self.dep)

        if (not cond.is_free()) and cond.is_ok(token):
            self.p = '*'
        else:
            self.p = ' '

    def __call__(self):
        return (str(self.token.index), str(self.token.shift), self.org, self.cor, self.p, self.left_space, self.right_space, self.tag, self.pos, self.dep, self.lem, self.nrm, self.ent_type, self.ent_iob, self.history)

class Table:
    def __init__(self, cond, sent):
        self.row_list = []
        for token in sent:
            self.row_list.append(Row(cond, token))
            self.row_list += [Row(cond, x) for x in token.addition]
        self.col_list = ['i', 'shift', 'org', 'cor', 'cond', 'l_space', 'r_space', 'tag', 'pos', 'dep', 'lemma', 'norm', 'ent_type', 'ent_iob', 'history']

    def __call__(self):
        return tabulate([x() for x in self.row_list], self.col_list, tablefmt = 'psql')

def en_show(
        hide_history = False,
        color = False,
        cor = None,
        tag = None,
        pos = None,
        dep = None):

    cond = Conds(color, cor, tag, pos, dep)

    for sent in sys.stdin:
        sent = decode(sent)
        if cond.check(sent):
            tab = Table(cond, sent)

            if sent.trg is None:
                print('src: ' + form_src(sent))
                print('trg: ' + form_trg(sent))
            else:
                print('src    : ' + form_src(sent))
                print('rtt({}): '.format(sent.trg['bridge']) + form_trg(sent))
                print('trg    : ' + sent.trg['text'])

            if not hide_history:
                history = []
                for record in sent.history:
                    if 'threshold' in record:
                        if 'char_threshold' in record:
                            desc = '{}({}, {})'.format(record['name'], record['threshold'], record['char_threshold'])
                        else:
                            desc = '{}({})'.format(record['name'], record['threshold'])
                    elif 'ratio' in record:
                        desc = '{}<{}>'.format(record['name'], record['ratio'])
                    else:
                        desc = '{}'.format(record['name'])
                    history.append(desc)
                history_len = len(history)
                print(f'history ({history_len}): ' + ' '.join(history))
            print(tab())

