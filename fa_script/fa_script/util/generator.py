from fa_script.util.load import check_sub_config

class ScriptGenerator:
    def __init__(self, run_generator, sub_generator):
        self.run_generator = run_generator
        self.sub_generator = sub_generator

    def __call__(self):
        self.run_generator()
        if check_sub_config():
            self.sub_generator()

