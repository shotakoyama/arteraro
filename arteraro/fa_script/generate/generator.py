from pathlib import Path
from arteraro.fa_script.util.prod import make_index_list, make_epoch_list, make_prod
from arteraro.fa_script.util.base import make_base_dir, make_ensemble_base_dir
from arteraro.fa_script.util.load import load_config_and_eval_config
from arteraro.fa_script.util.output import OutputRunScriptGenerator

def get_checkpoint_path(index, epoch):
    return Path(str(index)).resolve() / 'checkpoints' / 'checkpoint{}.pt'.format(epoch)

def get_ensemble_checkpoint_path(result_table):
    path_list = [get_checkpoint_path(result.index, result.epoch) for result in result_table.maximum_list()]
    return ':'.join([str(x) for x in path_list])

class GenerateRunScriptGenerator(OutputRunScriptGenerator):
    def write(self, base_dir, checkpoint, buffer_size, source):
        script = self.script_class(
                base_dir,
                checkpoint,
                buffer_size,
                self.batch_size,
                source,
                'output.yaml',
                'best.txt')
        self.write_script(base_dir, script)

class SingleGenerateRunScriptGenerator(GenerateRunScriptGenerator):
    def __init__(self, dataset, script_class):
        super().__init__(dataset, script_class)
        self.batch_size = self.config['generate'].get('batch_size', 32)

class EnsembleGenerateRunScriptGenerator(GenerateRunScriptGenerator):
    def __init__(self, dataset, script_class):
        super().__init__(dataset, script_class)
        self.batch_size = self.config['generate'].get('ensemble_batch_size', 4)

class ValidSingleGenerateRunScriptGenerator(SingleGenerateRunScriptGenerator):
    def __call__(self):
        for index, epoch in make_prod(self.config):
            base_dir = make_base_dir(index, self.dataset, 'valid', epoch)
            base_dir.mkdir(parents = True, exist_ok = True)
            checkpoint_path = get_checkpoint_path(index, epoch)
            self.write(base_dir, checkpoint_path, self.buffer_size, self.source)

class TestSingleGenerateRunScriptGenerator(SingleGenerateRunScriptGenerator):
    def __call__(self):
        for result in self.make_result_table().maximum_list():
            base_dir = make_base_dir(result.index, self.dataset, 'test', result.epoch)
            base_dir.mkdir(parents = True, exist_ok = True)
            checkpoint_path = get_checkpoint_path(result.index, result.epoch)
            self.write(base_dir, checkpoint_path, self.buffer_size, self.source)

class EnsembleGenerateRunScriptGenerator(EnsembleGenerateRunScriptGenerator):
    def write_valid(self):
        base_dir = make_ensemble_base_dir(self.dataset, 'valid')
        base_dir.mkdir(parents = True, exist_ok = True)
        checkpoint_path = get_ensemble_checkpoint_path(self.make_result_table())
        self.write(base_dir, checkpoint_path, self.valid_buffer_size, self.valid_source)

    def write_test(self):
        base_dir = make_ensemble_base_dir(self.dataset, 'test')
        base_dir.mkdir(parents = True, exist_ok = True)
        checkpoint_path = get_ensemble_checkpoint_path(self.make_result_table())
        self.write(base_dir, checkpoint_path, self.test_buffer_size, self.test_source)

    def __call__(self):
        self.write_valid()
        self.write_test()

