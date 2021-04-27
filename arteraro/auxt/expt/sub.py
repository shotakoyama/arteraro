from arteraro.auxt.script import SubScript

class ExptSubScript(SubScript):
    def make_workdir(self, script):
        workdir = str(script.outdir.make_outdir_path().resolve())
        return workdir

