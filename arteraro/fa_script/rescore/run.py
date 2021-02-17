from arteraro.fa_script.util.script import RunScript

class RescoreRegenerateRunScript(RunScript):
    def get_script_name(self):
        return 'rescore.sh'

    def make(self):
        source_yaml = 'output.yaml'
        target_yaml = 'rescored.yaml'
        self.append('roberta_rescore --detokenize < {} > {}'.format(source_yaml, target_yaml))
        for l in self.config['rescore']['lambda']:
            lmil = int(l * 1000)
            rescored_text = 'best.{}.txt'.format(lmil)
            self.append('rescore_with_lambda -l {} < {} | select_best > {} &'.format(l, target_yaml, rescored_text))
        self.append('wait')

