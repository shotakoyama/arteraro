# word order

## adv_wo

This rule moves adverb (word whose POS tag is `adv`).
This rule samples moving distance from normal distribution.

## an_wo

This rule shuffles order of the consecutive adjectives (word whose POS tag is `JJ`, `JJR`, `JJS`, or `CD`), for example *big fat*.
This rule can shuffle order of the concatination of consecutive adjectives and the following consecutive nouns (word whose POS taag is `NN` or `NNS`), for example *big fat cat*.
Whether the rule shuffle order including nouns is determined by parameter `ratio`.

## norm_wo

This rule moves all the words in sentence.
This rule samples moving distance from normal distribution (which is formed by parameters `loc`, `scale`).
The beta distribution of this rule samples ratio, which is multiplied to moving distance.
This trick make the noised sentences move variable.

## of_wo

This rule converts *A of B* to *B of A*.
Each of A and B is a phrase which is (`ADJ` | `DET` | `NUM`) * +  NOUN + .
The distance is sampled from normal distribution.

## pp_wo

This rule moves prepositional phrase.
Prepositional phrase is extracted by (`IN` & `ADP` & `prep` & not *of*) ((`ADV` | `ADJ` | `DET` | `NUM` | `NOUN` | `PRON` | `PROPN`) & not `WDT`) * (`PRON` | `PROPN` | `NOUN`) (?! (`PUNCT` | `VERB` | `AUX` | `SYM` | `X` | `SCONJ`)).
The distance is sampled from normal distribution.

## wh_wo

This rule moves *how*, *what*, *who*, *which*, *whose*, *when*, *where*, *whither*, *whence*, *why*, *whether*.
The distance is sampled from normal distribution.

