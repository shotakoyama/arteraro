# pyspm

## pyspm_train

sentencepiece training

See [`arterarejo/bpe/bea_train_16000/run.sh`](https://github.com/nymwa/arterarejo/blob/main/bpe/bea_train_16000/run.sh).

## pyspm_encode

```
cat hoge.m2 | m2_to_src | reguligilo -a | pyspm_encode --model_file bpe.model > valid.bpe_encoded.src
```

## pyspm_decode

This command decodes sentencepiece encoded sentences.

