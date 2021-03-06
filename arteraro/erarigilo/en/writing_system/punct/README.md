# punct

## bang

*!* → ε (0.4), *.* (0.2), *,* (0.2), *?* (0.2)

## colon

*:* → ε (0.4), *.* (0.2), *,* (0.2), *;* (0.2)

## semicolon

*;* → ε (0.4), *.* (0.2), *,* (0.2), *:* (0.2)

## comma

*,* → ε (0.9), *.* (0.05), *. .* (0.025), *;* (0.025)

## ins_left_comma

This rule inserts sampled string from
*,* (0.9), *, ,* (0.025), *.* (0.025), *;* (0.025), *:* (0.025).

cond: cond 1 or cond 2

cond 1: 1-a and 1-b

cond 1-a: 1-a-1 or 1-a-2

cond 1-a-1: PTB POS tag of the left word is `NN`, `NNS`, `NNP`, or `NNPS`

cond 1-a-2: PTB POS tag of the left word is `RB`, `RBR`, or `RBS` and Univ. POS tag is `ADV`

cond 1b: PTB POS tag of the right word is `CC`, `DT`, `IN`, `WDT`, WP`, `WP$`, or `WRB`

cond 2: 2-a and 2-b

cond 2-a: PTB POS tag of the left word is `NN`, `NNS`, `NNP`, or `NNPS`

cond 2-b: PTB POS tag of the right word is `RB`, `RBR`, `RBS` and Univ. POS tag is `ADV`

## ins_right_comma

This rule inserts sampled string from
*,* (0.9), *, ,* (0.025), *.* (0.025), *;* (0.025), *:* (0.025).

cond: cond 1 or cond 2

cond 1: 1-a and 1-b

cond 1-a: PTB POS tag of the left word is `NN`, `NNS`, `NNP`, or `NNPS`

cond 1-b: PTB POS tag of the left word is `RB`, `RBR`, `RBS` and Univ. PSO tag is `ADV`

cond 2: PTB POS tag of the right word is `VB`, `VBD`, `VBG`, `VBN`, `VBP`, or `VBZ`

## hatena

*?* → ε (0.1), *.* (0.75), *,* (0.1), *!* (0.05)

## hyphen

*-* → ε (0.85), *--* (0.1), *---* (0.025), *- -* (0.025)

## two_hyphens

*--* → ε (0.2), *-* (0.7), *---* (0.05), *- -* (0.05)

## ins_hyphen

This rule inserts sampled string from
*-* (0.7), *--* (0.25), *---* (0.025), *- -* (0.025).

cond: cond 1, 2, 3, or 4

cond 1: cond 1-a and cond 1-b

cond 1-a: PTB POS tag of the left word is `JJ`, `JJR`, `JJS`, `NN`, `NNS`, `RB`, or `CD`

cond 1-b: PTB POS tag of the right word is `JJ`, `JJR`, `JJS`, `NN`, `NNS`, `VBN`, or `VBG`

cond 2: cond 2-a and cond 2-b

cond 2-a: PTB POS tag of the left word is `JJ`, `JJR`, `JJS`, `CD`, `NN`, or `NNS`

cond 2-b: PTB POS tag of the right word is `RB`

cond 3: both PTB POS tag of the left word and that of the right word are `CD`

cond 4: cond 4-a and cond 4-b

cond 4-a: PTB POS tag of the left word is `VB`, `VBG`, `VBN`, `NN` or `NNS`

cond 4-b: PTB POS tag of the right word is `RP`

## period

*.* → ε (0.5), *,* (0.3), *. .* (0.05), *..* (0.05), *:* (0.025), *;* (0.025), *!* (0.025), *?* (0.025)

## quot

*``*, *''* → ε, *'*, *"*, *''*, *``*

