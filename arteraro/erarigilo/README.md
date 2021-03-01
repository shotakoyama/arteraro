# erarigilo

More details for error generating rules are under `en`.

## commands

### erg_paste

This pastes src data and trg data to one file with removing by condition of the minimun number of words and the maximum number of words.

```
en_erg_paste (src file path) (trg file path) --min-len (min words) --max-len (max words) > (output file path)
```

### en_erg_form

This convert json file of error generated data to tsv data.

```
en_erg_form < noised.txt > formed.txt
```

### en_erg_tokenizer

This applies SpaCy tokenizer.

`--remove-non-english` removes non-english sentences.

```
en_erg_tokenizer --remove-non-english < rawdata.txt > tokenized.txt
```


### en_erg_preprocess

This applies SpaCy tokenizer & tagger & parser, and makes json data.

`--remove-non-english` removes non-english sentences.

```
en_erg_preprocess --remove-non-english < rawdata.txt > labeled.json
```

### en_erg_noise

This generates artificial errors.
Please set `config.yaml` where you run `en_erg_noise`.

If you use GNU parallel for parallelization of `en_erg_noise`, you can get speed up with setting `OMP_NUM_THREADS=1` because `lemminflect` uses multiple cores and disturbs GNU parallel without direction of core limitation.

### en_erg_pj

You can visualize json data which are made by `en_erg_preprocess` or `en_erg_noise`.

