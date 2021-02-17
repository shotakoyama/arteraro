from argparse import ArgumentParser
import numpy as np
from arteraro.fa_script.errant.util import (
        ErrantCat2Result,
        valid_single_errant_result,
        test_single_errant_result,
        ensemble_errant_result,
        valid_rescore_errant_results,
        test_rescore_errant_result)

def bea19_valid(tab):
    tab.append(valid_single_errant_result('bea19'))
    valid_ensemble = ensemble_errant_result('bea19', 'valid')
    if valid_ensemble:
        tab.append(valid_ensemble.cat_score())
    valid_rescore = valid_rescore_errant_results('bea19')
    if valid_rescore:
        tab.append(max(valid_rescore).cat_score())
    return tab

def fce_valid(tab):
    tab.append(valid_single_errant_result('fce'))
    valid_ensemble = ensemble_errant_result('fce', 'valid')
    if valid_ensemble:
        tab.append(valid_ensemble.cat_score())
    valid_rescore = valid_rescore_errant_results('fce')
    if valid_rescore:
        tab.append(max(valid_rescore).cat_score())
    return tab

def fce_test(tab):
    tab.append(test_single_errant_result('fce'))
    test_ensemble = ensemble_errant_result('fce', 'test')
    if test_ensemble:
        tab.append(test_ensemble.cat_score())
    test_rescore = test_rescore_errant_result('fce')
    if test_rescore:
        tab.append(test_rescore.cat_score())
    return tab

def main():
    parser = ArgumentParser()
    parser.add_argument('-x', action='store_true')
    parser.add_argument('-b', action='store_true')
    parser.add_argument('-f', action='store_true')
    args = parser.parse_args()

    tab = [ErrantCat2Result.error_types]
    if not args.b:
        tab = bea19_valid(tab)
    if not args.f:
        tab = fce_valid(tab)
        tab = fce_test(tab)
    tab = np.array(tab).T

    if args.x:
        for row in tab:
            error_type = row[0] + ' ' * (10 - len(row[0]))
            line = ['{:.02f}'.format(round(float(x) * 100, 2)) for x in row[1:]]
            line = [' ' * (6 - len(x)) + x for x in line]
            line = ' '.join(['<td>{} </td>'.format(x) for x in line])
            line = '      <tr> <td> {} </td> {} </tr>'.format(error_type, line)
            print(line)
    else:
        for row in tab:
            print('\t'.join(row))

