def make_script_name(phase, dataset, stage, ensemble=True):
    name = '{}_{}_{}.sh'.format(phase, dataset, stage)
    if ensemble:
        name = 'ensemble_{}'.format(name)
    return name
