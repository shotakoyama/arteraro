import sys
import json
from tabulate import tabulate
from argparse import ArgumentParser
from .form import form_src, form_trg
from .util.token import EnToken
from .util.sent import EnSent

def decode(sent):
    sent = sent.strip()
    sent = json.loads(sent)
    sent = EnSent.decode(sent, token_class = EnToken)
    return sent

def is_free(args):
    cor_cond = args.cor is None
    tag_cond = args.tag is None
    pos_cond = args.pos is None
    dep_cond = args.dep is None
    return cor_cond and tag_cond and pos_cond and dep_cond

def is_ok(args, token):
    cor_cond = (args.cor is None) or (args.cor == token.cor)
    tag_cond = (args.tag is None) or (args.tag == token.tag)
    pos_cond = (args.pos is None) or (args.pos == token.pos)
    dep_cond = (args.dep is None) or (args.dep == token.dep)
    return cor_cond and tag_cond and pos_cond and dep_cond

def check(args, sent):
    if is_free(args):
        return True

    for token in sent:
        if is_ok(args, token):
            return True
    return False

def make_row(args, token):
    left_space = 'o' if token.left_space else 'x'
    right_space = 'o' if token.right_space else 'x'
    org = token.org if token.org is not None else '____'
    cor = token.cor if token.cor is not None else '____'
    tag = token.tag if token.tag is not None else '____'
    pos = token.pos if token.pos is not None else '____'
    dep = token.dep if token.dep is not None else '____'
    lem = token.lemma if token.lemma is not None else '____'
    nrm = token.norm if token.norm is not None else '____'
    ent_type = token.ent_type if token.ent_type is not None else '____'
    ent_iob = token.ent_iob if token.ent_iob is not None else '____'
    if len(token.history) > 0:
        history = ' '.join(token.history)
    else:
        history = '____'

    if args.color and (args.cor == cor):
        cor = '\033[31m' + cor + '\033[0m'
    if args.color and (args.tag == tag):
        tag = '\033[31m' + tag + '\033[0m'
    if args.color and (args.pos == pos):
        pos = '\033[31m' + pos + '\033[0m'
    if args.color and (args.dep == dep):
        dep = '\033[31m' + dep + '\033[0m'
    cond = '*' if (not is_free(args)) and is_ok(args, token) else ' '
    return [str(token.index), str(token.shift), org, cor, cond, left_space, right_space, tag, pos, dep, lem, nrm, ent_type, ent_iob, history]

def make_table(args, sent):
    lst = []
    for token in sent:
        lst.append(token)
        lst += token.addition
    lst = [make_row(args, token) for token in lst]
    tab = tabulate(lst, ['i', 'shift', 'org', 'cor', 'cond', 'l_space', 'r_space', 'tag', 'pos', 'dep', 'lemma', 'norm', 'ent_type', 'ent_iob', 'history'], tablefmt = 'psql')
    return tab

def main():
    parser = ArgumentParser()
    parser.add_argument('--hide-history', action = 'store_true')
    parser.add_argument('--color', action = 'store_true')
    parser.add_argument('--cor', default = None)
    parser.add_argument('--tag', default = None)
    parser.add_argument('--pos', default = None)
    parser.add_argument('--dep', default = None)
    args = parser.parse_args()

    for sent in sys.stdin:
        sent = decode(sent)
        if check(args, sent):
            tab = make_table(args, sent)
            print('src: ' + form_src(sent))
            print('trg: ' + form_trg(sent))
            if not args.hide_history:
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
            print(tab)

