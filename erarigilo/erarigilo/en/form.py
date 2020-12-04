import sys
import json
from erarigilo.en.util.token import EnToken
from erarigilo.en.util.sent import EnSent

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

    # 削除された語は除く
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

def main():
    for sent in sys.stdin:
        sent = sent.strip()
        sent = json.loads(sent)
        sent = EnSent.decode(sent, token_class = EnToken)
        src = form_src(sent)
        trg = form_trg(sent)
        out = src + '\t' + trg
        print(out)

