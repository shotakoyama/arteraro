from pathlib import Path

def spm_command(spm_model, dropout = None):
    path = Path(spm_model).resolve()
    line = 'pyspm_encode --model_file {}'.format(path)
    if dropout is not None:
        line += f' --dropout {dropout}'
    return line

