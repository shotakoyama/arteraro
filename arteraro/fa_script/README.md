# fa_script

`fa_scrit` is deprecated.

DO NOT USE `fa_script`.

Fairseq training script with Artificial error generation

You should see
[arterarejo/data/bea19_train/bea19_train_16000_10/config.yaml](https://github.com/nymwa/arterarejo/blob/main/data/bea19_train/bea19_train_16000_10/config.yaml),
[arterarejo/data/all/pretrain/config.yaml](https://github.com/nymwa/arterarejo/blob/main/data/all/pretrain/config.yaml),
[arterarejo/data/all/finetune/config.yaml](https://github.com/nymwa/arterarejo/blob/main/data/all/finetune/config.yaml),
[arterarejo/expt/baseline/baseline/config.yaml](https://github.com/nymwa/arterarejo/blob/main/expt/baseline/baseline/config.yaml),
[arterarejo/expt/pretrain_all/config.yaml](https://github.com/nymwa/arterarejo/blob/main/expt/pretrain_all/config.yaml),
[arterarejo/expt/finetune_all/config.yaml](https://github.com/nymwa/arterarejo/blob/main/expt/finetune_all/config.yaml),
to know how to use fa_script and how to write config.yaml.

## fa_data_pretrain

This command generates codes to prepare fairseq preprocessd data.

Here is a example,
[arterarejo/data/all/pretrain/config.yaml](https://github.com/nymwa/arterarejo/blob/main/data/all/pretrain/config.yaml).
Please `fa_data_pretrain` under `/path/to/arterarejo/data/all/pretrain`.

## fa_data_finetune

This command generates codes to prepare fairseq preprocessd data.

Here are examples,
[arterarejo/data/bea19_train/bea19_train_16000_10/config.yaml](https://github.com/nymwa/arterarejo/blob/main/data/bea19_train/bea19_train_16000_10/config.yaml),
[arterarejo/data/all/finetune/config.yaml](https://github.com/nymwa/arterarejo/blob/main/data/all/finetune/config.yaml).
Please `fa_data_finetune` under `/path/to/arterarejo/data/bea19_train/bea19_train_16000_10` or `/path/to/arterarejo/data/all/finetune`.

## fa_train_pretrain

This command generates codes to train fairseq model.

Here is a example,
[arterarejo/expt/pretrain_all/config.yaml](https://github.com/nymwa/arterarejo/blob/main/expt/pretrain_all/config.yaml).
Please `fa_train_pretrain` under `/path/to/arterarejo/expt/pretrain_all/`.

## fa_train_finetune

This command generates codes to train fairseq model.

Here are examples,
[arterarejo/expt/baseline/baseline/config.yaml](https://github.com/nymwa/arterarejo/blob/main/expt/baseline/baseline/config.yaml),
[arterarejo/expt/finetune_all/config.yaml](https://github.com/nymwa/arterarejo/blob/main/expt/finetune_all/config.yaml).
Please `fa_train_finetune` under `/path/to/arterarejo/expt/baseline/baseline/` or `/path/to/arterarejo/expt/finetune_all/`.

## fa_convert_eval_config

This command converts relative paths in eval_config to absolute paths.
Please run `fa_convert_eval_config eval_config.bea_train_16000.yaml eval_config.bea_train_16000.absolute.yaml` under `/path/to/arterarejo/expt/`.

## fa_generate_valid

This command generates codes to generate hypotheses for validation data.

## fa_generate_test

This command generates codes to generate hypotheses for test data.

## fa_score_valid

This command generates codes to score hypotheses of validation data.

## fa_score_test

This command generates codes to score hypotheses of test data.

## fa_ensemble

This command generates codes
to generate hypotheses with ensemble inference, and
to score these hypotheses.

## fa_rescore

This command generates codes
to rescore hypotheses with ensemble inference.

## fa_result_bea19

This command shows scores for BEA-19 valid dataset.

## fa_result_conll

This command shows score for CoNLL-2013 (valid) and CoNLL-2014 (test) dataset.

## fa_result_fce

This command shows score for FCE-valid and test dataset.

## fa_result_jfleg

This command show score for JFLEG valid and test dataset.

## fa_errant_cat2

This command show score for ERRANT error tag of BEA-19 valid, FCE-valid, FCE-test dataset.
Default setting shows tsv output.
"-x" option shows XML output.
"-b" option shows only BEA-19 valid scores.
"-f" option shows only FCE scores

