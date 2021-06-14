# pyspm

## pyspm-train

sentencepiece training

See [`arterarejo/bpe/bea_train_16000/run.sh`](https://github.com/nymwa/arterarejo/blob/main/bpe/bea_train_16000/run.sh).

## pyspm-encode

```
cat hoge.m2 | m22src | reguligilo -a | pyspm-encode --model-file bpe.model > valid.bpe_encoded.src
```

## pyspm-decode

This command decodes sentencepiece encoded sentences.

