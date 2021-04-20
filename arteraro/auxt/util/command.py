from pathlib import Path

def spm_command(model, dropout = None):
    path = Path(model).resolve()
    line = 'pyspm-encode --model-file {}'.format(model)
    if dropout is not None:
        line += ' --dropout {}'.format(dropout)
    return line

def parallel_command(j, L, command):
    line = 'parallel --pipe -j {} -k --L {} {}'.format(j, L, command)
    return line

