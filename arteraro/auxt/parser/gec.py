def make_gec_dataset_arguments(args):
    bea19 = args.bea19 or not (args.conll or args.fce or args.jfleg)
    conll = args.conll or not (args.bea19 or args.fce or args.jfleg)
    fce = args.fce or not (args.bea19 or args.conll or args.jfleg)
    jfleg = args.jfleg or not (args.bea19 or args.conll or args.fce)
    return bea19, conll, fce, jfleg

def add_gec_dataset_arguments(parser):
    parser.add_argument('-b', '--bea19', action = 'store_true')
    parser.add_argument('-c', '--conll', action = 'store_true')
    parser.add_argument('-f', '--fce', action = 'store_true')
    parser.add_argument('-j', '--jfleg', action = 'store_true')

def make_gec_dataset_arguments_without_bea19(args):
    conll = args.conll or not (args.fce or args.jfleg)
    fce = args.fce or not (args.conll or args.jfleg)
    jfleg = args.jfleg or not (args.conll or args.fce)
    return conll, fce, jfleg

def add_gec_dataset_arguments_without_bea19(parser):
    parser.add_argument('-c', '--conll', action = 'store_true')
    parser.add_argument('-f', '--fce', action = 'store_true')
    parser.add_argument('-j', '--jfleg', action = 'store_true')

