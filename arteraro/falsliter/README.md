# falsliter

Please refer [these sample codes](https://github.com/nymwa/arterarejo/tree/main/falsliter/crawl19_comm_parl).

## falsliter-data-spilt

This command splits standard inputs to N gzip files so that each file has nearly same data size.

```
zcat reguriligo_normalized_file.gz | faliliter-data-split data.1.gz:data.2.gz:data.3.gz
```

## falsliter-preprocess

This command converts sentences in standard inputs to (2n + 1)-gram list.

```
zcat data.1.gz | falsliter-preprocess 2 source_file.1.npy target_file.1.npy
```

## falsliter-data-merge

This command merges preprocessed files into one file.

```
falsliter-data-merge source_file.1.npy:source_file.2.npy:source_file.3.npy target_file.1.npy:target_flie.2.npy:target_file.3.npy src.npy trg.npy
```

## falsliter-train

This command trains falsliter-model.

```
falsliter-train src.npy trg.npy --max-epoch 20
```

## falsliter-dump

This command makes probability distribution of falsliter model prediction.

```
falsliter-dump checkpoints/checkpoint19.pt score.dat
```

## falsliter-merge-model

This command merges scores.
This trick work as checkpoint averaging.

```
falsliter-merge-model 2 1/score.dat:2/score.dat:3/score.dat
```

## falsliter-dist

This command shows distribution by prediction.

```
falsliter-dist 2 score.dat --T 2.0
```

For example, if you input `wrong`, then you can see distribution of `?` of `wr?ng`.

## falsliter-sample

This command samples character from distribution.

```
falsliter-sample 2 score.dat --T 2.0
```

