from pathlib import Path
from arteraro.fa_script.util.script import RunScript
from arteraro.fa_script.util.fairseq import fairseq_interactive_command

class GenerateRunScript(RunScript):
    def __init__(self, base_dir, checkpoint, buffer_size, batch_size, source, output, select):
        self.checkpoint = checkpoint
        self.buffer_size = buffer_size
        self.batch_size = batch_size
        self.source = source
        self.output = output
        self.select = select
        super().__init__(base_dir)

    def get_script_name(self):
        return 'generate.sh'

    def make(self):
        data_bin = self.get_data_bin()
        command = fairseq_interactive_command(
                data_bin,
                self.checkpoint,
                self.config['generate'].get('beam', 12),
                self.buffer_size,
                self.batch_size,
                self.config['generate'].get('lenpen', 0.6),
                self.source,
                self.output)
        self.append(command)
        self.append('cat {} | select_best > {}'.format(self.output, self.select))

    def get_data_bin(self):
        return Path(self.config['data']).resolve() / '0' / 'data-bin'

