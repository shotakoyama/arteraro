# det

# art

This rule generates error for article.

*a*, *an*, *the* (whose POS tag is `DET`) → ε (0.2), a (0.2), an (0.2), the (0.3), this (0.025), that (0.025), these (0.025), those (0.025)

## ins_det

This rule inserts determiner between words.

cond 1: The left word has POS tag `VB`, `VBD`, `VBG`, `VBN`, `VBP`, `VBZ`, `IN`.

cond 2: The right word is the most left word of the sentence.

cond 3: The right word has POS tag `NN`, `NNS`, `JJ`, `JJN`, `JJS`.

If (cond1 or cond2) and cond3, this rule applies, and insert
a (0.3), an (0.3), the (0.3), this (0.025), that (0.025), these (0.025), those (0.025).

## demonstrative

This rule  generates error for demonstrative.

*this*, *that*, *these*, *those* (whose dependency tag is `det`) → ε, *this*, *that*, *these*, *those*, *a*, *an*, *the*

## demonstrative_extra

This rule generates error for demonstrative.

*this*, *that*, *these*, *those* (whose dependency tag is `nsubj`, `nsubjpass`, `pobj`, `dobj`, `conj`, `appos`, `attr`, `advmod`, `ROOT`, `quantmod`, `npadvmod` and POS tag is not `WDT`) → ε, *this*, *that*, *these*, *those*, *a*, *an*, *the*

## det_no

This rule generates error for *no*.
This rule will be moved to `word selection`.

*no* (whose POS tag is `DET`) → *not*, *non*, *any*

## det_any

This rule generates error for *any*.
This rule will be moved to `word selection`.

*any* (whose POS tag is `DET`) → ε (0.4), *some* (0.1), *every* (0.1), *a* (0.1), *an* (0.1), *all* (0.1), *anything* (0.1)

## det_some

This rule generates error for *some*.
This rule will be moved to `word selection`.

*some* (whose POS tag is `DET`) → ε (0.4), *a* (0.05), *an* (0.05), *the* (0.05), *those* (0.05), *these* (0.05), *few* (0.05), *little* (0.05), *something* (0.05), *somewhere* (0.05), *much* (0.05), *many* (0.05), *so* (0.05)


## det_all

This rule generates error for *all*.
This rule will be moved to `word selection`.

*all* (whose POS tag is `DET`) → *both*, *each*, *every*

## det_both

This rule generates error for *both*.
This rule will be moved to `word selection`.

*both* (whose POS tag is `DET`) → ε, *all*, *each*, *every*

## det_each

This rule generates error for *each*.
This rule will be moved to `word selection`.

*each* (whose POS tag is `DET`) → ε, *all*, *both*, *every*

## det_every

This rule generates error for *every*.
This rule will be moved to `word selection`.

*every* (whose POS tag is `DET`) → ε, *all*, *both*, *each*

## another

This rule generates error for *another*.
This rule will be moved to `word selection`.

*another* (whose POS tag is `DET` → *other*, *the other*, 

## other

This rule generates error for *other*.
This rule will be moved to `word selection`.

*other* → *another*, *others*

## so

This rule generates error for *so*.
This rule will be mowed to `word selection`.

*so* → ε, *such*, *too*

## such

This rule generates error for *such*.
This rule will be moved to `word selection`.

*such* → ε, *so*, *very*

## there

This rule generates error for *there*.
This rule will be moved to `word selectionn`.

*there* → ε (0.5), *here* (0.3), *they* (0.1), *it* (0.1)

## here

This rule generates error for *here*.
This rule will be moved to `word selection`.

*here* → ε (0.5), *there* (0.3), *they* (0.1), *it* (0.1)

