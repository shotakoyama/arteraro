# en_erg_script

## how to use?

### command line

#### `en_erg_script`

This command generates scripts to generate artificial erronous sentences.

You have to write configuration files tu run `en_erg_script`.

One of them is `config.yaml`. You have to write configurations of error generating rules in this file.

This is example.

```
- starndard_prep:
   mean: 0.05
   std: 0.05
- spell
   mean: 0.05
   std: 0.05
   char_prob: 0.9
   score_path: /path/to/score.dat
   n: 2
   temp: 2.0
```

One of them is `aeg_config.yaml`.
You have to write configuration of process of artificial error generation.

This is example.

```
preprocessed_gzip_list:
   - /path/to/labeled.1.gz
   - /path/to/labeled.2.gz
   spm_model: /path/to/bpe.model
   src_dropout: 0.1
   trials: 50 # the number of trials of AEG
   min_len: 1 # min #word in sentence
   max_len: 500 # max #word in sentence
   threads: 40 # threads for GNU parallel
   corpus_size: 16000000 # standard input is stopped at this size
   lines: 10000 # the size of sentences which are inputted to AEG process (You have to set this so that GNU parallel do not fail.)
   forming_lines: 100000 # the size of sentences which are decoder from json to sentence pair at a time
   tokenization_lines: 100000 # the size of sentences which are inputted to sentencepiece at a time
```

One of them is `sub_config.yaml`.
If you can use `qsub` of Grid Engine, please use this.

This is example.

```
group: (your group)
h_rt: 4:0:0
```

