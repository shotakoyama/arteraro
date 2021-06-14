# afiksilo

## How to use

### command line

#### `afiksilo`

You can test your afiksilo model.
If you want to use afiksilo, run command `afiksilo path/to/model.pickle`.
You type a word, and you get words whose suffixes are replaced.

Here is an example. If you type "word" and enter key, you will get "words worded wording wordless".

```
word
words worded wording wordless
```

### `afiksilo-prepare`

You can get word frequency data from standard inputs.
Then, the frequency data are saved.

```
afiksilo-prepare frequency.tsv < data.txt
```

### `afiksilo-make_model`

You can make model using frequency data that `afiksilo-prepare` has made.
This model can be used for `afiksilo` command.
Furthermore, this model is used in an error-generating module `confusion`.
This rule does not use `afiksilo` as library.
You can see detail of `confusion` from [arteraro/erarigilo/en/word_selection/confusion.py](https://github.com/nymwa/arteraro/blob/main/arteraro/erarigilo/en/word_selection/confusion.py).

```
afiksilo-make-model path/to/frequency.tsv path/to/afiksilo_dict.pickle --min-freq 1000 --min-length 3
```

