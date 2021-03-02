# prep

## prep

These rules generate error for preposition.

cond: whose POS tag is `IN` and dependency tag is `prep`, `ROOT` or `conj`

### standard_prep

*of*, *to*, *in*, *for*, *on*, *with*, *at* →, ε, *of*, *to*, *in*, *for*, *with*, *by*, *at*

### prep_about

*about* → ε, *in*, *on*, *of*, *to*, *at*

### prep_above

*above* → *on*, *from*, *to*, *over*

### prep_across

*across* → *beyond*, *over*, *through*, *throughout*, *during*

### prep_after

*after* → *for*, *by*, *over*, *from*, *when*

### prep_against

*against* → *to*, *for*, *of*, *with*

### prep_amid

*amid* → ε, *in*, *on*, *at*, *about*, *between*, *among*

### prep_amidst

*amidst* → ε, *in*, *on*, *at*, *about*, *between*, *amongst*

### prep_among

*among* → ε, *in*, *on*, *at*, *about*, *between*, *amid*

### prep_amongst

*amongst* → ε, *in*, *on*, *at*, *about*, *between*, *amidst*

### prep_as

*as* → *by*, *of*, *in*, *on*, *at*, *like*

### prep_before

*before* → *on*, *for*, *when*

### prep_behind

*behind* → *after*, *from*, *of*, *out*

### prep_below

*below* → *in*, *on*, *by*, *with*, *under*, *through*, *within*

### prep_between

*between* → ε, *in*, *on*, *at*, *about*, *among*, *amongst*, *amid*, *amidst*

### prep_beyond

*beyond* → *on*, *over*, *above*, *out of*, *far from*

### prep_by

*by* → ε, *in*, *on*, *at*, *for*, *with*, *of*, *from*, *through*, *until*, *till*

### prep_during

*during* → *in*, *for*, *while*, *when*, *through*, *across*

### prep_from

*from* → ε, *in*, *at*, *of*, *with*, *about*, *since*

### prep_into

*into* → ε (0.2), *in* (0.3), *to* (0.3), *toward* (0.1), *towards* (0.1)

### prep_like

*like* → *as* (0.8), *that* (0.1), *than* (0.1)

### prep_out

*out* → ε

### prep_over

*over* → *on*, *from*, *to*, *above*

### prep_since

*since* → *from*

### prep_than

*than* → ε (0.2), *to* (0.4), *from* (0.2), *over* (0.1), *beyond* (0.1)

### prep_through

*through* → *in*, *over*, *across*, *into*, *of*, *with*, *by*, *throughout*, *thru*

### prep_throughout

*throughout* → *in*, *over*, *across*, *into*, *of*, *with*, *by*, *through*

### prep_toward

*toward*, *towards* → *to*, *with*, *of*, *for*, *in*, *into*

### prep_under

*under* → *in*, *on*, *by*, *with*, *below*, *through*, *within*

### prep_until

*until* → *by*, *for*, *to*, *in*, *up to*, *when*

### prep_till

*till* → *by*, *for*, *to*, *in*, *up to*, *when*

### prep_upon

*upon* → *on*, *up*, *up on*, *over*, *after*, *to*

### prep_within

*within* → *with*, *in*, *of*, *on*

### post_vb_prep

cond1: the left word has POS tag `VB`, `VBD`, `VBG`, `VBN`, `VBP`, or `VBZ`

cond2: the left word has dependency tag `acl`, `advcl`, `xcomp`, `pcomp`

cond3: the right word has POS tag `NOUN`, `DET`, `ADJ`, `PROPN`

cond4: the right word has POS tag `SCONJ` and has dependency tag `mark`

If cond1 and cond2 and (cond3 or cond4) are satisfied, this rule inserts *to*, *in*, *on*, *at*, *by*, *for*, *with*, or *of* between the words.

## mark

These rules generate error for marker.

cond: whose POS tag is `IN` and dependency tag is `mark`

### standard_mark

*as*, *if*, *because*, *so*, *whether*, *while*, *since*, *although*, *than*, *through*, *once*, *whereas*, *whilst*, *like*, *except* → ε

### mark_for

*for* → ε (0.2), *to* (0.6), *on* (0.1), *in* (0.1)

## agent

These rules generate error for agent preposition.

cond: whose POS tag is `IN` and dependency tag is `agent`

### agent_by

*by* → ε, *of*, *from*, *with*, *on*

### agent_between

*between* → ε, *by*, *in*, *on*, *at*, *from*, *with*, *about*, *among*, *amongst*, *amid*, *amidst*

## pcomp

These rules generate error for preposition which makes pcomp.

cond: whose POS tag is `IN` and dependency tag is `pcomp`

### pcomp_of

*of* → ε

### pcomp_to

*to* → ε

### pcomp_on

*on* → *at*, *in*, *of*

### pcomp_for

*for* → *to* (0.4), *at* (0.2), *in* (0.2), *on* (0.2)

### pcomp_at

*at* → *on*, *in*, *of*

### pcomp_by

*by* → *at*, *in*, *on*, *of*, *from*

## dative

These rules generate error for preposition which introduces dative.

cond: whose POS tag is `IN` and dependency tag is `dative`

### dative_to

*to* → ε (0.4), *for* (0.6)

### dative_for

*for* → ε (0.4), *to* (0.6)

## advmod

### prep_advmod

This rule generates error for preposition which introduces advmod.

*at*, *as* (whose POS tag is `IN` and dependency tag is `advmod`) → ε

