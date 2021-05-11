from .run import ScoreRunScript
from .sub import ScoreSubScript
from .gec_job import GECScoreJobScript, GECRerankingScoreJobScript

class ErrantScoreJobInterface:
    def make_environment_source_path(self):
        return self.eval_config['errant_source_path']

    def make(self):
        output_path = self.outdir.make_path('best.m2')
        self.append('errant_parallel -orig {} -cor {} -out {}'.format(
            self.original_path(),
            self.corrected_path(),
            output_path))
        reference = self.reference_path()
        self.append('errant_compare -ref {} -hyp {} > {}'.format(
            reference, output_path, self.outdir.make_path('result.txt')))
        self.append('errant_compare -ref {} -hyp {} -cat 1 > {}'.format(
            reference, output_path, self.outdir.make_path('result.cat1')))
        self.append('errant_compare -ref {} -hyp {} -cat 2 > {}'.format(
            reference, output_path, self.outdir.make_path('result.cat2')))
        self.append('errant_compare -ref {} -hyp {} -cat 3 > {}'.format(
            reference, output_path, self.outdir.make_path('result.cat3')))

class BEA19ValidScoreJobInterface(ErrantScoreJobInterface):
    def original_path(self):
        return self.eval_config['bea19']['valid_orig']

    def reference_path(self):
        return self.eval_config['bea19']['valid_m2']

class FCEValidScoreJobInterface(ErrantScoreJobInterface):
    def original_path(self):
        return self.eval_config['fce']['valid_orig']

    def reference_path(self):
        return self.eval_config['fce']['valid_m2']

class FCETestScoreJobInterface(ErrantScoreJobInterface):
    def original_path(self):
        return self.eval_config['fce']['test_orig']

    def reference_path(self):
        return self.eval_config['fce']['test_m2']

class BEA19ValidScoreJobScript(BEA19ValidScoreJobInterface, GECScoreJobScript):
    pass

class BEA19ValidRerankingScoreJobScript(BEA19ValidScoreJobInterface, GECRerankingScoreJobScript):
    pass

class FCEValidScoreJobScript(FCEValidScoreJobInterface, GECScoreJobScript):
    pass

class FCEValidRerankingScoreJobScript(FCEValidScoreJobInterface, GECRerankingScoreJobScript):
    pass

class FCETestScoreJobScript(FCETestScoreJobInterface, GECScoreJobScript):
    pass

class FCETestRerankingScoreJobScript(FCETestScoreJobInterface, GECRerankingScoreJobScript):
    pass

class BEA19ValidSingleScorePathInterface:
    def make_path(self):
        return 'score_bea19_valid.sh'

class FCEValidSingleScorePathInterface:
    def make_path(self):
        return 'score_fce_valid.sh'

class FCETestSingleScorePathInterface:
    def make_path(self):
        return 'score_fce_test.sh'

class BEA19ValidSingleScoreRunScript(BEA19ValidSingleScorePathInterface, ScoreRunScript):
    pass

class FCEValidSingleScoreRunScript(FCEValidSingleScorePathInterface, ScoreRunScript):
    pass

class FCETestSingleScoreRunScript(FCETestSingleScorePathInterface, ScoreRunScript):
    pass

class BEA19ValidSingleScoreSubScript(BEA19ValidSingleScorePathInterface, ScoreSubScript):
    pass

class FCEValidSingleScoreSubScript(FCEValidSingleScorePathInterface, ScoreSubScript):
    pass

class FCETestSingleScoreSubScript(FCETestSingleScorePathInterface, ScoreSubScript):
    pass

