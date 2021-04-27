from arteraro.auxt.script import JobScript

class ExptJobScript(JobScript):
    def __init__(self, outdir):
        self.outdir = outdir
        super().__init__()

