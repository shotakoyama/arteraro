# erarigilo

The development of erarigilo was moved to [nymwa/erarigilo](https://github.com/nymwa/erarigilo).

New erarigilo is updated to use SpaCy v3.

The development of erarigilo here will not be done.

---

"erarigilo" derives from Esperanto, and means "error-making tool".

More details for error generating rules are under `en`.

## commands

### erg ready

This applies SpaCy tokenizer.

### erg run

This generates artificial errors.
Please set `config.yaml` where you run `en_erg_noise`.

If you use GNU parallel for parallelization, you can get speed up with setting `OMP_NUM_THREADS=1` because `lemminflect` uses multiple cores and disturbs GNU parallel without direction of core limitation.

### erg form

You can convert json data by erarigilo into tsv parallel data.

### erg show

You can visualize json data which are made erarigilo.

