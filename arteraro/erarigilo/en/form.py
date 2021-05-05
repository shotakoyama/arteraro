import sys
import json
from .util.token import EnToken
from .util.sent import EnSent

def form_src(sent):
    token_list = []
    for token in sent:
        token_list.append(token)
        token_list += token.addition

    word_list = []
    for token in token_list:
        if token.org is not None:
            word_list.append((token.index + token.shift, token.org, token.left_space, token.right_space))
        else:
            word_list.append((token.index + token.shift, token.cor, token.left_space, token.right_space))
    word_list.sort(key = lambda x : x[0])

    # to remove delated tokens from word_list
    word_list = [(index, word, left_space, right_space)
            for index, word, left_space, right_space
            in word_list
            if word != '']

    if len(word_list) > 0:
        text = word_list[0][1] # word
    else:
        text = ''

    for i in range(1, len(word_list)):
        if word_list[i - 1][3] and word_list[i][2]:
            text += ' '
        text += word_list[i][1]

    text = text.strip()
    return text

def form_trg(sent):
    lst = [token.cor for token in sent]
    return ' '.join(lst)

def en_form():
    for sent in sys.stdin:
        sent = sent.strip()
        sent = json.loads(sent)
        sent = EnSent.decode(sent, token_class = EnToken)

        src = form_src(sent)
        if sent.trg is None:
            trg = form_trg(sent)
        else:
            trg = sent.trg['text']

        out = src + '\t' + trg
        print(out)

