from pathlib import Path
from arteraro.auxt.script import JobScript
from .fairseq import FairseqTrainCommand

class WorkerJobScript(JobScript):
    localdir = True

    def __init__(self, index, num_node, gpu_per_node = None, port = None):
        self.index = index
        self.num_node = num_node
        self.gpu_per_node = gpu_per_node
        self.port = port
        super().__init__()

    def make_path(self):
        return '{}/worker.sh'.format(self.index)

    def p_multi_node(self):
        return self.num_node > 1

    def p_copy(self):
        return self.config['train'].get('copy_data_bin', False)

    def p_tmp_save(self):
        return self.config['train'].get('tmp_save_dir', False)

    def make_tmp_save_dir(self):
        return Path('${SGE_LOCALDIR}/checkpoints')

    def make_data_bin_path(self, data_path, index):
        if self.p_copy():
            path = '${{SGE_LOCALDIR}}/{}/data-bin'.format(index)
        else:
            path = Path(data_path) / str(index) / 'data-bin'
            path = str(path.resolve())
        return path

    def make_data_bins(self, data_path, data_indices):
        data_bin_list = [self.make_data_bin_path(data_path, index) for index in data_indices]
        data_bins = ':'.join(data_bin_list)
        return data_bins

    def make_copy(self, data_indices):
        for index in data_indices:
            self.append('mkdir -p ${{SGE_LOCALDIR}}/{}'.format(index))

        for index in data_indices:
            data_path = Path(self.config['data']).resolve() / str(index) / 'data-bin'
            self.append('cp -r {} ${{SGE_LOCALDIR}}/{} &'.format(data_path, index))
        self.append('wait')

    def make_data_indices(self):
        data_indices = self.config['data_indices'][self.index]
        return data_indices

    def make_train_command(self, data_indices):
        data_bin = self.make_data_bins(self.config['data'], data_indices)
        log_file = str(Path(str(self.index)).resolve() / 'train.log')
        command = FairseqTrainCommand(data_bin, log_file)

        if 'restore_file' in self.config['train']:
            command.restore_file(str(Path(self.config['train']['restore_file'][self.index]).resolve()))

        if self.p_tmp_save():
            command.save_dir(self.make_tmp_save_dir())

        command.seed(self.config['train']['seed_list'][self.index])
        command.log()
        if 'save_interval' in self.config['train']:
            command.save_interval(self.config['train']['save_interval'])
        command.fp16()
        if self.config.get('no_c10d', False):
            command.no_c10d()
        command.epoch(self.config['train']['max_epoch'])
        command.batch(self.config['train']['update_freq'], self.config['train']['max_tokens'])
        command.arch(
                prenorm = self.config['train'].get('prenorm', True),
                arch = self.config['train']['arch'],
                share_all_embeddings = self.config['train'].get('share_all_embeddings', True),
                dropout = self.config['train'].get('dropout', 0.3),
                attention_dropout = self.config['train'].get('attention_dropout', 0.2),
                activation_dropout = self.config['train'].get('activation_dropout', 0.2),
                activation_fn = self.config['train'].get('activation_fn', 'gelu'))
        command.adam(*self.config['train'].get('adam_betas', [0.9, 0.999]))
        command.inverse_sqrt(
                self.config['train']['lr'],
                self.config['train']['warmup_updates'],
                self.config['train'].get('warmup_init_lr', 1.0e-07))
        command.clip_norm(self.config['train'].get('clip_norm', 1.0))
        command.weight_decay(self.config['train'].get('weight_decay', 1.0e-03))
        command.label_smoothed_cross_entropy(self.config['train'].get('label_smoothing', 0.1))
        if self.p_multi_node():
            command.distributed(self.num_node, self.gpu_per_node, self.port)
        return command

    def make(self):
        data_indices = self.make_data_indices()
        if self.p_copy():
            self.make_copy(data_indices)
        command = self.make_train_command(data_indices)
        self.append(str(command))

