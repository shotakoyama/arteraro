def tokenize_command(lang):
    if lang in {'en', 'de', 'fr'}:
        command = '{}-tokenize'.format(lang)
    else:
        command = 'sacremoses -l {} tokenize'.format(lang)
    return command

