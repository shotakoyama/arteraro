class FairseqTrainCommand(list):
    def __init__(self, data_bin_path, log_file=None):
        super().__init__(['fairseq-train', data_bin_path])
        self.log_file = log_file

    def restore_file(self, restore_file):
        self.append('--restore-file {}'.format(restore_file))

    def save_dir(self, path):
        self.append('--save-dir {}'.format(path))

    def seed(self, seed):
        self.append('--seed {}'.format(seed))

    def log(self):
        self += ['--log-interval 1', '--log-format simple']

    def save_interval(self, interval):
        self.append('--save-interval {}'.format(interval))

    def fp16(self):
        self.append('--fp16')

    def no_c10d(self):
        self.append('--ddp-backend=no_c10d')

    def epoch(self, max_epoch):
        self.append('--max-epoch {}'.format(max_epoch))

    def batch(self, update_freq, max_tokens):
        self += [
            '--update-freq {}'.format(update_freq),
            '--max-tokens {}'.format(max_tokens)]

    def dimensions_template(self, embed, ffn_embed, heads):
        self += [
                '--encoder-embed-dim {}'.format(embed),
                '--encoder-ffn-embed-dim {}'.format(ffn_embed),
                '--encoder-attention-heads {}'.format(heads),
                '--decoder-embed-dim {}'.format(embed),
                '--decoder-ffn-embed-dim {}'.format(ffn_embed),
                '--decoder-attention-heads {}'.format(heads)]

    def dimensions(self, arch):
        if arch == 'tiny':
            self.dimensions_template(128, 512, 2)
        elif arch == 'small':
            self.dimensions_template(256, 1024, 4)
        elif arch == 'base':
            self.dimensions_template(512, 2048, 8)
        elif arch == 'big':
            self.dimensions_template(1024, 4096, 16)
        else:
            assert False

    def arch(self, prenorm, arch, share_all_embeddings, dropout, attention_dropout, activation_dropout, activation_fn):
        self.append('--arch transformer')

        if prenorm:
            self += [
                '--encoder-normalize-before',
                '--decoder-normalize-before']

        self.dimensions(arch)

        if share_all_embeddings:
            self.append('--share-all-embeddings')

        self += [
            '--dropout {}'.format(dropout),
            '--attention-dropout {}'.format(attention_dropout),
            '--activation-dropout {}'.format(activation_dropout),
            '--activation-fn {}'.format(activation_fn)]

    def adam(self, beta1, beta2):
        self += [
            '--optimizer adam',
            "--adam-betas '({}, {})'".format(beta1, beta2)]

    def inverse_sqrt(self, lr, warmup_updates, warmup_init_lr):
        self += [
            '--lr {}'.format(lr),
            '--lr-scheduler inverse_sqrt',
            '--warmup-updates {}'.format(warmup_updates),
            '--warmup-init-lr {}'.format(warmup_init_lr)]

    def constant(self, lr):
        self += [
            '--lr {}'.format(lr),
            '--lr-scheduler fixed']

    def clip_norm(self, clip_norm=1.0):
        self.append('--clip-norm {}'.format(clip_norm))

    def weight_decay(self, weight_decay):
        self.append('--weight-decay {}'.format(weight_decay))

    def label_smoothed_cross_entropy(self, label_smoothing=0.1):
        self += [
            '--criterion label_smoothed_cross_entropy',
            '--label-smoothing {}'.format(label_smoothing)]

    def reset_meters(self):
        self.append('--reset-meters')

    def reset_dataloader(self):
        self.append('--reset-dataloader')

    def reset_optimizer(self):
        self.append('--reset-optimizer')

    def reset_lr_scheduler(self):
        self.append('--reset-lr-scheduler')

    def distributed(self, num_nodes, gpus_per_node, port=54849):
        self += [
            '--distributed-world-size {}'.format(num_nodes * gpus_per_node),
            '--distributed-rank $(expr {} \* $OMPI_COMM_WORLD_RANK)'.format(gpus_per_node),
            '--distributed-init-method "tcp://${{1}}:{}"'.format(port),
            '--distributed-port {}'.format(port)]

    def __str__(self):
        if self.log_file is None:
            lst = self
        else:
            lst = self + ['| tee {}'.format(self.log_file)]
        return ' '.join(lst)

