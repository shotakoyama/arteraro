from pathlib import Path

def qsub_command(code_path, group, h_rt, node, num_node, var_dict=None):
    line = 'qsub'
    if group is not None:
        line += ' -g {}'.format(group)
    line += ' -l {}={}'.format(node, num_node)
    line += ' -l h_rt={}'.format(h_rt)
    if var_dict is not None:
        var_list = ['{}={}'.format(key, value) for key, value in var_dict.items()]
        var_list = ','.join(var_list)
        line += ' -v ' + var_list
    line += ' {}'.format(code_path)
    return line

