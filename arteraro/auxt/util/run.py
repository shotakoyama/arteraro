from .load import check_sub_config

def generate_run(script_list, run_script_class, sub_script_class):
    if check_sub_config():
        sub_script = sub_script_class(script_list)
    else:
        run_script = run_script_class(script_list)

