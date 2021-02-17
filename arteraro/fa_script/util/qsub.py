from pathlib import Path

def qsub_command(code_path, group, h_rt, node, num_node, p=None, var_dict=None):
    line = 'qsub'
    if group is not None:
        line += ' -g {}'.format(group)
    if p is not None:
        line += ' -p {}'.format(p)
    line += ' -l {}={}'.format(node, num_node)
    line += ' -l h_rt={}'.format(h_rt)
    if var_dict is not None:
        var_list = ['{}={}'.format(key, value) for key, value in var_dict.items()]
        var_list = ','.join(var_list)
        line += ' -v ' + var_list
    line += ' {}'.format(code_path)
    return line

