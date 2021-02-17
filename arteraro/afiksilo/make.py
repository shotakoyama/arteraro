from argparse import ArgumentParser
from collections import defaultdict
from tqdm import tqdm
import lemminflect
import pickle

suffix_list = (
        'ability ibility bility able ible ble ably ibly bly'.split() +
        'acy ade age al ial an ance ancy ant ar arch archy ard arian ary aster ate ation ative'.split() +
        'ce se cide cle cule ule cracy craft crat cum cy d dom drome'.split() +
        'ed en n ence ency en ent er ee eer yer er ern ery ry esce escent ese esque ess est ette'.split() +
        'fic fication fold form iform free ful fy gamy gate gen gon gram graph graphy handed hood'.split() +
        'i ian ic ical ically ice ician ics id ie ier yer ify fy ile in ine ing ion ior iour'.split() +
        'ish ism ist ite itis ity ium ive itive ization isation ize ise'.split() +
        'le let like ling log logue logical logist logy ology looking ly lysis'.split() +
        'man men person mancy mania manship ment meter metry most ness nik nomy onomy ock oid or our tour'.split() +
        'ory ose osis osity ous eous pathy phile phil philia philiac phobe phobia phone phony ple proof red rel erel'.split() +
        's scape scope self selves ship some speak sphere ster th eth tion tious tude itude ty'.split() +
        'ular ulous ure ward wards way ways wide wise worthy y ey'.split() +
        'nce es ies ied ily e t'.split())

def load_vocab(freq_path, min_freq):
    vocab = {}
    with open(freq_path) as f:
        for x in f:
            word, freq = x.strip().split('\t')
            freq = int(freq)
            if freq >= min_freq:
                vocab[word] = freq
    return vocab

def remove_suffix(word, suffix):
    tmp = word[:-len(suffix)]
    if len(tmp) >= 2 and tmp[-1] == tmp[-2]:
        return [tmp, tmp[:-1]] # removing double consonant (e.g. dropped -> dropp -> drop)
    else:
        return [tmp]

# This code removes suffixes from the input word and make the list of words whose suffixes are removed.
def suffix_removed_words(word):
    removed_list = []
    removing_list = [word]
    while removing_list:
        word, removing_list = removing_list[0], removing_list[1:]
        for suffix in suffix_list:
            if len(word) > len(suffix) + 1 and word.endswith(suffix):
                removed = remove_suffix(word, suffix)
                removing_list += removed
                removed_list += removed
    return removed_list

# This code replaces suffixes from the input word and make the list of words whose suffix are replaced to another suffix.
def suffix_replaced_words(word):
    replaced_list = []
    for suffix in suffix_list:
        if len(word) > len(suffix) + 3 and word.endswith(suffix):
            candidates = [word[:-len(suffix)] + new_suffix
                    for new_suffix in suffix_list
                    if new_suffix != suffix]
            candidates = [candidate
                    for candidate in candidates
                    if len(candidate) >= len(word)]
            replaced_list += candidates
    return replaced_list

# This code inflects input word
def inflected_words(word):
    inflected_list = []
    for tag, lst in lemminflect.getAllInflections(word).items():
        inflected_list += lst
    return inflected_list

def filter_word(vocab, lst, minimum):
    return {word for word in lst if word in vocab and len(word) >= minimum}

def search_similar_words(vocab, word, minimum):
    similar_words = suffix_removed_words(word) + suffix_replaced_words(word) + inflected_words(word)
    similar_words = filter_word(vocab, similar_words, minimum)
    return similar_words

def build_afiksilo_dictionary(vocab, minimum):
    afiksilo_dict = defaultdict(list)

    # get similar candidates for each word
    for word in tqdm(vocab, bar_format = '{l_bar}{r_bar}'):
        candidate_list = search_similar_words(vocab, word, minimum)
        afiksilo_dict[word] += candidate_list
        for candidate in candidate_list:
            afiksilo_dict[candidate] = list(set(afiksilo_dict[candidate]) | {word} - {candidate})

    # get similar candidates of each similar candidates
    for word in tqdm(vocab, bar_format = '{l_bar}{r_bar}'):
        candidate_list = search_similar_words(vocab, word, minimum)
        for candidate in candidate_list:
            afiksilo_dict[word] = list(set(afiksilo_dict[word] + afiksilo_dict[candidate]) - {word})

    # adding candidates of candidates
    for _ in range(5):
        for word in tqdm(vocab, bar_format = '{l_bar}{r_bar}'):
            for candidate in afiksilo_dict[word]:
                afiksilo_dict[word] = list(set(afiksilo_dict[word] + afiksilo_dict[candidate]) - {word})

    return afiksilo_dict

def main():
    parser = ArgumentParser()
    parser.add_argument('freq_path', help = 'path to frequency list')
    parser.add_argument('model')
    parser.add_argument('--min-freq', type = int, default = 1000)
    parser.add_argument('--min-length', type = int, default = 3)
    args = parser.parse_args()

    vocab = load_vocab(args.freq_path, args.min_freq)
    afiksilo_dict = build_afiksilo_dictionary(vocab, args.min_length)
    model = {}
    for word, lst in afiksilo_dict.items():
        lst = list(set(lst) - {word})
        if len(lst) > 0:
            model[word] = lst

    with open(args.model, 'wb') as f:
        pickle.dump(model, f)

