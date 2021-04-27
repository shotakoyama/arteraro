from arteraro.auxt.script import RunScript

class PrepareRunScript(RunScript):
    def make_path(self):
        return 'prepare.sh'

    def get_job(self):
        return self.config['prepare'].get('job', 1)

