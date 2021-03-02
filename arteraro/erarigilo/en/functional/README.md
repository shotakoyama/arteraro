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

This rule applies to word which is not punctuation and has `'` in itself.

This rule removes the whole word or removes `'` in word.

## part

This rule generates errors for particle.

word whose dependency tag is `prt` and POS tag is `RP` → ε (0.65), out (0.05), up (0.05), down (0.05), about (0.05), on (0.05), in (0.05), off (0.05)

## to

This rule generates error for `to` infinitive.

*to* (whose tag is `TO`) → ε (0.6), *by* (0.2), *for* (0.2)

