def fairseq_interactive_command(
        data_bin,
        path,
        beam,
        nbest,
        buffer_size,
        batch_size,
        lenpen):
    lst = ['fairseq-interactive',
            str(data_bin),
            '--path {}'.format(path),
            '--beam {}'.format(beam),
            '--nbest {}'.format(nbest),
            '--buffer-size {}'.format(buffer_size),
            '--batch-size {}'.format(batch_size),
            '--lenpen {}'.format(lenpen)]
    return ' '.join(lst)

