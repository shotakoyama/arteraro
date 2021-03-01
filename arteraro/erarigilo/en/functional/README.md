# functional

## sub categories

- det
	- error generating rules for determinar
- inter
	- error generating rules for interogative word
- prep
	- error generating rules for preposition
- pron
	- error generating rules for pronoun

## auxpass

This rule removes passive auxiliary.

Whether the word is passive auxiliary or not is decided by dependency tag `auxpass`.

## conj_and (conj.py)

This rule generates error for conjunction *and*.

*and* → ε (0.95), *but* (0.05)

## conj_but (conj.py)

This rule generates error for conjunction *but*.

*but* → ε (0.9), *and* (0.1)

## contr

This rule generates errors for contraction.


