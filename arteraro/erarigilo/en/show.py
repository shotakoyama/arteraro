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

def is_free(cor, tag, pos, dep):
    return (cor is None) and (tag is None) and (pos in None) and (dep is None)

def is_ok(cor, tag, pos, dep, token):
    cor_cond = (cor is None) or (cor == token.cor)
    tag_cond = (tag is None) or (tag == token.tag)
    pos_cond = (pos is None) or (pos == token.pos)
    dep_cond = (dep is None) or (dep == token.dep)
    return cor_cond and tag_cond and pos_cond and dep_cond

def check(cor, tag, pos, dep, sent):
    if is_free(cor, tag, pos, dep):
        return True
    return any(is_ok(cor, tag, pos, dep, token) for token in sent)

def make_row(color_cond, cor_query, tag_query, pos_query, dep_query, token_query):
    left_space = 'o' if token.left_space else 'x'
    right_space = 'o' if token.right_space else 'x'
    org_str = token.org if token.org is not None else '____'
    cor_str = token.cor if token.cor is not None else '____'
    tag_str = token.tag if token.tag is not None else '____'
    pos_str = token.pos if token.pos is not None else '____'
    dep_str = token.dep if token.dep is not None else '____'
    lem_str = token.lemma if token.lemma is not None else '____'
    nrm_str = token.norm if token.norm is not None else '____'
    ent_type = token.ent_type if token.ent_type is not None else '____'
    ent_iob = token.ent_iob if token.ent_iob is not None else '____'
    if len(token.history) > 0:
        history = ' '.join(token.history)
    else:
        history = '____'

    if color_cond and (cor_query == cor_str):
        cor = '\033[31m' + cor + '\033[0m'
    if color_cond and (tag_query == tag_str):
        tag = '\033[31m' + tag + '\033[0m'
    if color_cond and (pos_query == pos_str):
        pos = '\033[31m' + pos + '\033[0m'
    if color_cond and (dep_query == dep_str):
        dep = '\033[31m' + dep + '\033[0m'
    cond = '*' if (not is_free(cor_query, tag_query, pos_query, dep_query)) and is_ok(cor_query, tag_query, pos_query, dep_query, token) else ' '
    return [str(token.index), str(token.shift), org, cor, cond, left_space, right_space, tag, pos, dep, lem, nrm, ent_type, ent_iob, history]

def make_table(color, cor, tag, pos, dep, sent):
    lst = []
    for token in sent:
        lst.append(token)
        lst += token.addition
    lst = [make_row(color, cor, tag, pos, dep, token) for token in lst]
    tab = tabulate(lst, ['i', 'shift', 'org', 'cor', 'cond', 'l_space', 'r_space', 'tag', 'pos', 'dep', 'lemma', 'norm', 'ent_type', 'ent_iob', 'history'], tablefmt = 'psql')
    return tab

def en_show(
        hide_history = False,
        color = False,
        cor = None,
        tag = None,
        pos = None,
        dep = None):

    for sent in sys.stdin:
        sent = decode(sent)
        if check(cor, tag, pos, dep, sent):
            tab = make_table(color, cor, tag, pos, dep, sent)
            print('src: ' + form_src(sent))
            print('trg: ' + form_trg(sent))
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
            print(tab)

