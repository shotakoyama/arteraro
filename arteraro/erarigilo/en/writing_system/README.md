# writing system

## sub categories

- case
	- error generating rules for case (e.g. title case)
- punct
	- error generating rules for puctuation

## del_orth

This rule removes space between words.

## ins_orth

This rule inserts space into word.
This rule can insert space so that each separated part is contained in dictionary.
This process is done by [`ortobruilo`](https://github.com/nymwa/arteraro/tree/main/arteraro/ortobruilo).
The parameter `penalty` determines the ratio to use `ortobruilo`.

## spell

This rule generates spelling error.
This rule first samples the number of iterations to generate spelling error for a word from geometric distribution.
Then, it samples error generating operations (delete, swap, insert, replace).
Finally, it injects spelling errors with sampled operations.

Explanations for operations:
- delete
	- delete one character from word
- swap
	- swap two consecutive characters from word
- insert
	- insert one charater which sampled from [`falsliter`](https://github.com/nymwa/arteraro/tree/main/arteraro/falsliter) model
- replace
	- replace one charater which sampled from `falsliter` model

<img src="https://raw.githubusercontent.com/nymwa/arteraro/main/arteraro/erarigilo/en/writing_system/falsliter.png">

