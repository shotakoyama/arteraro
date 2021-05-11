from pathlib import Path
from arteraro.auxt.script import JobScript
from arteraro.auxt.util.fairseq_interactive import fairseq_interactive_command

class RTTTranslateJobScript(JobScript):
    localdir = True

    def __init__(self, lang, index, segment):
        self.lang = lang
        self.index = index
        self.segment = segment
        super().__init__()

    def make_path(self):
        return '{}/{}/{}/{}.sh'.format(self.index, self.segment, self.lang, self.phase)

    def get_bpe_model_path(self):
        return str(Path(self.config['bridges'][self.lang]['bpe_model']).resolve())

    def get_data_bin_path(self):
        return str(Path(self.config['bridges'][self.lang][self.phase]['data_bin']).resolve())

    def get_checkpoint_path(self):
        return str(Path(self.config['bridges'][self.lang][self.phase]['checkpoint']).resolve())

    def get_outdir_path(self, file_path):
        return str(Path('{}/{}/{}/{}'.format(self.index, self.segment, self.lang, file_path)).resolve())

    def get_generation_command(self):
        beam = self.config.get('beam', 4)
        nbest = 1
        buffer_size = self.config['buffer_size']
        batch_size = self.config['batch_size']
        lenpen = self.config.get('lenpen', 0.6)
        return fairseq_interactive_command('$DATABIN', '$CHECKPOINT', beam, nbest, buffer_size, batch_size, lenpen)

    def get_max_length(self):
        return self.config['max_length']

    def make_variables(self):
        self.append('BPEMODEL={}'.format(self.get_bpe_model_path()))
        self.append('DATABIN={}'.format(self.get_data_bin_path()))
        self.append('CHECKPOINT={}'.format(self.get_checkpoint_path()))
        self.append('')

    def make_namedpipe(self):
        self.append('mkfifo ${SGE_LOCALDIR}/namedpipe')
        self.append('')

    def make(self):
        self.make_variables()
        self.make_namedpipe()
        self.make_translation()
        self.append('')
        self.make_outputs()

class RTTForeJobScript(RTTTranslateJobScript):
    phase = 'fore'

    def make_translation(self):
        input_file_path = str(Path('{}/{}/split.gz'.format(self.index, self.segment)).resolve())
        max_len = self.get_max_length()

        self.append('zcat {} \\'.format(input_file_path))
        self.append('   | tee >(indeksi --only-indices | cat > ${SGE_LOCALDIR}/namedpipe) \\')
        self.append('   | en-tokenize \\')
        self.append('   | reguligilo --all --quote \\')
        self.append('   | pyspm-encode --model-file $BPEMODEL \\')
        self.append('   | cat \\') # unbuffering: if the number of input sentences is not so small, the buffer of input of trunki and that of input of named pipe may stuck
        self.append('   | trunki -n {} -r -s ${{SGE_LOCALDIR}}/namedpipe -t ${{SGE_LOCALDIR}}/indices.txt \\'.format(max_len))
        self.append('   | {} \\'.format(self.get_generation_command()))
        self.append('   | grep \'^H\' \\')
        self.append('   | cut -f 3 \\')
        self.append('   | pyspm-decode --replace-unk {} \\'.format(chr(0xfffd)))
        self.append('   | progress \\')
        self.append('   > ${SGE_LOCALDIR}/translated.txt')

    def make_outputs(self):
        self.append('paste ${SGE_LOCALDIR}/indices.txt ${SGE_LOCALDIR}/translated.txt \\')
        self.append('   | pigz -c \\')
        self.append('   > {}'.format(self.get_outdir_path('fore.gz')))

class RTTBackJobScript(RTTTranslateJobScript):
    phase = 'back'

    def make_translation(self):
        max_len = self.get_max_length()

        self.append('zcat {} \\'.format(self.get_outdir_path('fore.gz')))
        self.append('   | tee >(cut -f 1 > ${SGE_LOCALDIR}/namedpipe) \\')
        self.append('   | cut -f 2 \\')
        self.append('   | pyspm-encode --model-file $BPEMODEL \\')
        self.append('   | cat \\')
        self.append('   | trunki -n {} -r -s ${{SGE_LOCALDIR}}/namedpipe -t ${{SGE_LOCALDIR}}/indices.txt \\'.format(max_len))
        self.append('   | {} \\'.format(self.get_generation_command()))
        self.append('   | grep \'^H\' \\')
        self.append('   | cut -f 3 \\')
        self.append('   | pyspm-decode --replace-unk {} \\'.format(chr(0xfffd)))
        self.append('   | malreguligilo \\')
        self.append('   | progress \\')
        self.append('   > ${SGE_LOCALDIR}/translated.txt')

    def make_outputs(self):
        self.append('paste ${SGE_LOCALDIR}/indices.txt ${SGE_LOCALDIR}/translated.txt \\')
        self.append('   | pigz -c \\')
        self.append('   > {}'.format(self.get_outdir_path('back.gz')))

