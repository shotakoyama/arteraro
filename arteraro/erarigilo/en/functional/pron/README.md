# pron

cond: the word has lemma `-PRON-` (see [https://github.com/explosion/spaCy/blob/v2.3.2/website/docs/api/annotation.md#lemmatization-lemmatization])

## 1st singular

### 1sng_subj

cond: dependecy tag is `nsubj`, `nsubjpass`, `conj`, `appos`, or `attr`

*I* → ε, *i*, *it*, *me*, *we*

### 1sng_nusbj_obj

cond: dependency tag is `nsubj`, `nsubjpass`, `conj`, `appos`, or `attr`

*me* → ε, *I*, *my*

### 1sng_dobj

cond: dependency tag is `dobj`

*me* → ε (0.1), *I* (0.1), *for me* (0.3), *to me* (0.3), *on me* (0.05), *in me* (0.05), *at me* (0.05), *of me* (0.05)

### 1sng_pobj

cond: dependency tag is `pobj`

*me* → ε, *I*, *my*

### 1sng_dative

cond: dependency tag is `dative`

*me* → ε (0.1), *I* (0.1), *for me* (0.3), *to me* (0.35), *on me* (0.05), *in me* (0.05), *at me* (0.05)

### 1sng_poss

*mine* → *my*, *me*, *ours*, *his*, *hers*

### 1sng_poss_det

*my* → ε, *I*, *me*, *mine*, *a*, *an*, *the*, *its*, *his*, *her*, *their*

### 1sng_reflexive

cond: dependency tag is `dobj`, `conj`, `nsubj`, `nsubjpass`, `npadvmod`, `dative`, `attr`

*myself* → ε (0.2),
*to myself* (0.1),
*of myself* (0.1),
*for myself* (0.1),
*by myself* (0.1),
*with myself* (0.1),
*myselves* (0.02),
*to myselves* (0.02),
*of myselves* (0.02),
*for myselves* (0.02),
*by myselves* (0.02),
*with myselves* (0.02),
*me* (0.1),
*my* (0.02),
*mine* (0.02),
*yourself* (0.02),
*ourselves* (0.02)

### 1sng_appos_reflexive

cond: dependency tag is `appos`

*myself* → ε, *my*, *myselves*, *my self*, *for myself*, *by myself*

### 1sng_pobj_reflexive

cond: dependency tag is `pobj`

*myself* → *me*, *my self*, *myselves*, *I*

## 1st plural

### 1plu_subj

cond: dependency tag is `nsubj`, `nsubjpass`, `conj`, `appos`, `nmod`, `compound`, or `attr`

*we* → *I*, *us*, *our*, *me*, *they*, *you*

### 1plu_pobj

cond: dependency tag is `pobj`

*us* → *we*, *ours*, *our*, *ourselves*

### 1plu_dobj

cond: dependency tag is `dobj`

*us* → ε (0.1), *we* (0.1), *for us* (0.3), *to us* (0.35), *on us* (0.05), *in us* (0.05), *at us* (0.05)

### 1plu_nsubj_obj

cond: dependency tag is `nsubj`, `nsubjpass`, `conj`, `appos`, `nmod`, `compound`, or `attr`

*us* → ε, *we*, *our*

### 1plu_dative

cond: dependency tag is `dative`

*us* → ε (0.1), *we* (0.1), *for us* (0.3), *to us* (0.35), *on us* (0.05), *in us* (0.05), *at us* (0.05)

### 1plu_poss

*ours* → *our*, *us*, *we*, *mine*, *theirs*, *yours*

### 1plu_poss_det

*our* → ε, *we*, *us*, *ours*, *a*, *the*, *an*, *theirs*, *its*, *my*

### 1plu_reflexive

cond: dependency tag is `dobj`, `conj`, `nsubj`, `nsubjpass`, `npadvmod`, `dative`, or `attr`

*ourselves* → ε (0.2),
*to ourselves* (0.1),
*of ourselves* (0.1),
*for ourselves* (0.1),
*by ourselves* (0.1),
*with ourselves* (0.1), 
*ourself* (0.02),
*to ourself* (0.02),
*of ourself* (0.02),
*for ourself* (0.02),
*by ourself* (0.02),
*with ourself* (0.02)<
*us* (0.1),
*our* (0.02),
*ours* (0.02),
*yourselves* (0.02),
*myself* (0.02)

### 1plu_appos_reflexive

cond: dependency tag is `appos`

*ourselves* → ε, *us*, *ourself*, *our selves*, *for ourselves*, *by ourselves*

### 1plu_pobj_reflexive

cond: dependency tag is `pobj`

*ourselves* → ε, *us*, *ourself*, *our selves*, *for ourselves*, *by ourselves*

## 2nd

### 2nd_subj

cond: dependency tag is `nsubj`, `nusbjpass`, `conj`, `appos`, `nmod`, `compound`, or `attr`

*you* → *u*, *yo*, *your*, *yours*, *me*, *they*

### 2nd_pobj

cond: dependency tag is `pobj`

*you* → *u*, *yo*, *your*, *yours*, *yourself*, *yourselves*

### 2nd_dobj

cond: dependency tag is `dobj`

*you* → ε (0.1), *u*, (0.05), *yo* (0.05), *for you* (0.3), *to you* (0.3), *on you* (0.05), *in you* (0.05), *at you* (0.05), *of you* (0.05)

### 2nd_dative

cond: dependency tag is `dative`

*you* → ε (0.1), *u*, (0.05), *yo* (0.05), *for you* (0.3), *to you* (0.35), *on you* (0.05), *in you* (0.05), *at you* (0.05)

### 2nd_poss

*yours* → *you*, *your*, *theirs*, *mine*, *ours*, *theirs*

### 2nd_poss_det

*your* → ε, *you*, *yours*, *their*, *a*, *an*, *the*, *its*, *they*

### 2sng_reflexive

cond: dependency tag is `dobj`, `conj`, `nsubj`, `nsubjpass`, `npadvmod`, `dative`, or `attr`

*yourself* →  ε (0.2),
*to yourself* (0.1),
*of yourself* (0.1),
*for yourself* (0.1),
*by yourself* (0.1),
*with yourself* (0.1),
*yourselves* (0.02),
*to yourselves* (0.02),
*of yourselves* (0.02),
*for yourselves* (0.02),
*by yourselves* (0.02),
*with yourselves* (0.02),
*you* (0.1),
*your* (0.02),
*yours* (0.02),
*themself* (0.02),
*myself* (0.02)

### 2sng_appos_reflexive

cond: dependency tag is `appos`

*yourself* → ε, *you*, *yourselves*, *your self*, *yourselves*, *your*

### 2sng_pobj_reflexive

cond: dependency tag is `pobj`

*yourself* → *you*, *your self*, *yourselves*, *your*

### 2plu_reflexive

cond: dependency tag is `dobj`, `conj`, `nsubj`, `nsubjpass`, `npadvmod`, `dative`, or `attr`

*yourselves* → ε (0.2),
*to yourselves* (0.1),
*of yourselves* (0.1),
*for yourselves* (0.1),
*by yourselves* (0.1),
*with yourselves* (0.1),
*yourself* (0.02),
*to yourself* (0.02),
*of yourself* (0.02),
*for yourself* (0.02),
*by yourself* (0.02),
*with yourself* (0.02),
*you* (0.1),
*your* (0.02),
*yours* (0.02),
*themselves* (0.02),
*ourselves* (0.02)

### 2plu_appos_reflexive

cond: dependency tag is `appos`

*yourselves* → ε, *you*, *yourself*, *your selves*, *for yourselves*, *by yourselves*

### 2plu_pobj_reflexive

cond: dependency tag is `pobj`

*yourselves* → *you*, *your self*, *myselves*, *your*

