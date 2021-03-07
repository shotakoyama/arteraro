# fa_select

## fairseq_to_yaml

This command converts fairseq output to yaml file to select best candidate and to rescore.

"--retain-whitespace" option stops removing BPE special characters.

"--retain-normalized" option stops denormalized process using [`reguligilo`](https://github.com/nymwa/arteraro/tree/main/arteraro/reguligilo).

```
fairseq-interactive /path/to/data-bin --some-arguments < source_file.src | fairseq_to_yaml > output.yaml
cat output.yaml | select_best > best.txt
```

## roberta_rescore

This command rescores fairseq output in yaml file.

Input to RoBERTa is detokenized if you set "--detokenize".
This make gain by rescoring a little better.

## select_best

This command selects the best candidate of fairseq output in yaml file.

## rescore_with_lambda

This command rescore fairseq output in yaml file.

```
roberta_rescore --detokenize < output.yaml > rescored.yaml
rescore_with_lambda -l 0.025 < rescored.yaml | select_best > best.25.txt
```

