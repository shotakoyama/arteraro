# arteraro

Arteraro is derived from Esperanto and means "artificial error."

Please feel free to comment! Any issue is welcome. Please use this code Arteraro.

- Various Errors Improve Neural Grammatical Error Correction (PACLIC 2021)
	- Please use `v2.0.0` to reproduce results of this paper.
	- paper, outputs and analyses
		- [PACLIC_2021_Various](https://github.com/nymwa/PACLIC_2021_Various)
	- pretrained models
		- [163M_pretrain](https://github.com/nymwa/163M_pretrain)
	- How to reproduce?
		- Please see [nymwa/arterarejo2](https://github.com/nymwa/arterarejo2)
	- You can download models for artificial error generation.
		- [afiksilo_dict.pickle](https://drive.google.com/file/d/1078gRbXeAR8AcPKVQ67bMnCYumMBxvsd/view?usp=sharing)
			- dictionary for afiksilo
		- [orto_dict.pickle](https://drive.google.com/file/d/1DTkcujzZRqH7W9UCR2iTh17nySeHEaG7/view?usp=sharing)
			- dictionary for ortobruilo
		- [score.dat](https://drive.google.com/file/d/1xGxDZgSN_J0_0Gnm1vo8xhqjk7VIoYMq/view?usp=sharing)
			- model for falsliter
- ニューラル文法誤り訂正のための多様な規則を用いる人工誤り生成 (言語処理学会第27回年次大会)
	- Please use `v1.0.1` to redroduce results of this paper.
	- 誤り生成規則は `v1.0.1` のものを使用しています．
	- 論文中のCoNLL-2014データセットに関するスコアに誤りがありましたので，修正原稿([リンク](https://github.com/nymwa/anlp_nlp2021_aeg/blob/main/nlp2021.pdf))を公開しました．CoNLL-14の値に関してはこちらを参照ください．
	- また，論文中に載せられなかった実験結果や分析などを[こちら](https://github.com/nymwa/anlp_nlp2021_aeg/blob/main/analysis.pdf)で公開しています．こちらも参照ください．
	- モデルによる訂正の出力は[こちら](https://github.com/nymwa/anlp_nlp2021_aeg/tree/main/outputs)に公開しました．
	- 学習済みモデル（1モデル）を使って Google Colaboratory で文法誤り訂正を実行できる [Jupyter Notebook](https://gist.github.com/nymwa/982e92c4810f0ee31886378052af1459) を公開しました．
	- paper, outputs and analyses
		- Please see [nymwa/anlp_nlp2021_aeg](https://github.com/nymwa/anlp_nlp2021_aeg)
	- How to reproduce?
		- Please see [nymwa/arterarejo](https://github.com/nymwa/arterarejo)

## Where are documents of error generating rules for artificial error generation?

You can see at [arteraro/erarigilo/README.md](https://github.com/nymwa/arteraro/tree/main/arteraro/erarigilo).

## Installation

### 1. environment

#### requirements
- Python version >= 3.8
	- fairseq v0.10.0~2 seems to fail with python 3.9 because of change about typing.
	- So, if you want to use python 3.9, please use fairseq of the latest commit.
- PyTorch version >= 1.8.0

#### recommended
- CUDA version: 11.1
- cudnn version: 8.2.0
- nccl version: 2.8.4-1
- gdrcopy version: 2.0
- openmpi version: 4.0.5
- fairseq version: 0.10.2

### 2. install packages using `pip install requirements.txt`

You must use SpaCy 2.3. Do not use SpaCy v1 or SpaCy v3.

### 3. install `fairseq`

If you want to reproduce our experiments in the same environment that we used, you must use `fairseq==0.10.2`.
However, `fairseq==0.10.2` has a bug of using multiple nodes, and you must rewrite one line to run experiments using multiple nodes.
This bug seems to be corrected in the latest commit. You can also use the latest fairseq.

To install `fairseq==0.10.2`, you have to run `git clone https://github.com/pytorch/fairseq.git -b v0.10.2`, and install by `pip install -e .`.

Then, you have to rewrite a line in `fairseq/distributed_utils.py` like below, to run fairseq using multiple nodes.

```
  283:             torch.multiprocessing.spawn(
  284:                 fn=distributed_main,
  285:                 args=(main, args, kwargs),
- 286:                 nprocs=args.distributed_num_procs,
+ 286:                 nprocs = min(
+ 287:                 torch.cuda.device_count(),
+ 288:                 args.distributed_world_size),
  287:             )
  288:         else:
  289:             distributed_main(args.device_id, main, args, kwargs)
```

I recommend you to install `apex` following https://github.com/pytorch/fairseq#requirements-and-installation

### 4. install `arteraro`

You run `pip install -e .` under `/path/to/arteraro`. Then now you can use arteraro in your environment.

Let's generate artificial errors for better grammatical error correction!

