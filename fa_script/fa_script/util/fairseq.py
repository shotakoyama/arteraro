def fairseq_preprocess_command(train_pref, valid_pref, dest_dir, src_dict_path, log_path):
    lst = ['fairseq-preprocess',
            '--source-lang src',
            '--target-lang trg',
            '--trainpref {}'.format(train_pref),
            '--validpref {}'.format(valid_pref),
            '--destdir {}'.format(dest_dir),
            '--workers 40']
    if src_dict_path is not None:
        lst.append('--srcdict {}'.format(src_dict_path))
    lst.append('--joined-dictionary > {}'.format(log_path))
    return ' '.join(lst)

class FairseqTrainCommand(list):
    def __init__(self, data_bin_path, log=None):
        super().__init__(['fairseq-train', data_bin_path])
        self.log = log

    def restore_file(self, restore_file):
        self.append('--restore-file {}'.format(restore_file))

    def seed(self, seed):
        self.append('--seed {}'.format(seed))

    def log(self):
        self += ['--log-interval 1', '--log-format simple']

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

    def arch(self, prenorm, arch, share_all_embeddings, dropout, attention_dropout, activation_dropout, activation_fn):
        self.append('--arch transformer')
        if prenorm:
            self += [
                '--encoder-normalize-before',
                '--decoder-normalize-before']
        if arch == 'big':
            self += [
                '--encoder-embed-dim 1024',
                '--encoder-ffn-embed-dim 4096',
                '--encoder-attention-heads 16',
                '--decoder-embed-dim 1024',
                '--decoder-ffn-embed-dim 4096',
                '--decoder-attention-heads 16']
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

    def __str__(self):
        if self.log is None:
            lst = self
        else:
            lst = self + ['| tee {}.log'.format(self.log)]
        return ' '.join(lst)

