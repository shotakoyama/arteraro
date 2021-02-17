from arteraro.fa_script.score.errant import ErrantScoreRunScript

class ErrantRescoreRunScript(ErrantScoreRunScript):
    def __init__(self, base_dir, l):
        self.l = l
        super().__init__(base_dir)

    def get_script_name(self):
        lmil = int(self.l * 1000)
        return 'score.{}.sh'.format(lmil)

    def output_path(self):
        lmil = int(self.l * 1000)
        output = 'best.{}.m2'.format(lmil)
        result = 'result.{}.res'.format(lmil)
        result_cat1 = 'result.{}.cat1'.format(lmil)
        result_cat2 = 'result.{}.cat2'.format(lmil)
        result_cat3 = 'result.{}.cat3'.format(lmil)
        return output, result, result_cat1, result_cat2, result_cat3

