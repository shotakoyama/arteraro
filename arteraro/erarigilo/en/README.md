# en

## sub categories

- functional
	- error generating rules for functional words
	- Some rules are to be moved to word selection because they are not rules for functional words (e.g. another, so, there).
- inflection
	- error generating rules for inflection of word
- word_order
	- error generating rules for word order
- word_selection
	- error generating rules for word selection
- writing_system
	- error generating rules for writing system

## del (delnoise.py)

This rule deletes frequent punctuations and words randomly.

The list of punctuations to be deleted: , . - " ' ) ( : $ / ; ? % & = _ ! [ ] @ * + < ` # > \ { ~ } ^

The list of words to be deleted:
the a an 's 're to of in for on with as at by from about than into against under during around up down before after out over like back off away back through just am was are were is be being been have has had do did does and or but because if since while this these that those there it they them which what whose who whom where when how why whether can could may might ought shall should will would dare

## mask

This rule masks words or characters randomly.

You can set parameters p, threshold_mean, and threshold_std except mean and std.

threshold_mean and threshold_std make a beta distribution for deciding whether sampled error is for character or word.

p is parameter for geometric distribution. This rule samples the number of character masks for a word from this distribution.

mask token for character: □

mask token for word: ▨

