from arteraro.fa_script.score.m2 import M2ScoreRunScript

class M2RescoreRunScript(M2ScoreRunScript):
    def __init__(self, base_dir, l):
        self.l = l
        super().__init__(base_dir)

    def get_script_name(self):
        lmil = int(self.l * 1000)
        return 'score.{}.sh'.format(lmil)

    def output_path(self):
        lmil = int(self.l * 1000)
        result = 'result.{}.res'.format(lmil)
        return result

