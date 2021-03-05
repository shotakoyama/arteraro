# pron

cond: the word has lemma `-PRON-` (see https://github.com/explosion/spaCy/blob/v2.3.2/website/docs/api/annotation.md#lemmatization-lemmatization )

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

## 3rd singular feminine

### 3sng_fem_subj

cond: dependency tag is `nsubj`, `nsubjpass`, `conj`, `appos`, `nmod`, `compound`, `attr`

*she* → *her*, *hers*, *they*, *them*, *their*, *he*

### 3sng_fem_pobj

cond: dependency tag is `pobj`

*her* → *hers*, *their*, *them*, *herself*, *him*

### 3sng_fem_dobj

cond: dependency tag is dobj

*her* → ε (0.1), *she* (0.05), *him* (0.05), *for her* (0.3), *to her* (0.3), *on her* (0.05), *in her* (0.05), *at her* (0.05), *of her* (0.05)

### 3sng_fem_nsubj_obj

cond: dependency tag is `nsubj`, `nsubjpass`, `conj`, `appos`, `nmod`, `compound`, or `attr`

*her* → ε, *she*, *hers*, *them*, *him*

### 3sng_fem_dative

cond: dependency tag is `dative`

*her* → ε (0.1), *she* (0.05), *him* (0.05), *for her* (0.3), *to her* (0.35), *on her* (0.05), *in her* (0.05), *at her* (0.05)

### 3sng_fem_poss

*hers* → ε, *she*, *her*, *theirs*, *his*, *they*, *yours*

### 3sng_fem_poss_det

cond: dependecy tag is `poss`

*her* → ε, *she*, *hers*, *their*, *his*, *a*, *an*, *the*, *its*

### 3sng_fem_reflexive

cond: dependecy tag is `dobj`, `conj`, `nsubj`, `nsubjpass`, `npadvmod`, `dative`, or `attr`

*herself* → ε (0.2),
*to herself* (0.1),
*of herself* (0.1),
*for herself* (0.1),
*by herself* (0.1),
*with herself* (0.1),
*herselves* (0.01),
*to herselves* (0.01),
*of herselves* (0.01),
*for herselves* (0.01),
*by herselves* (0.01),
*with herselves* (0.01),
*themself* (0.01),
*to themself* (0.01),
*of themself* (0.01),
*for themself* (0.01),
*by themself* (0.01),
*with themself* (0.01),
*she* (0.045),
*her* (0.045),
*hers* (0.045),
*himself* (0.045)

### 3sng_fem_appos_reflexive

cond: dependency tag is `appos`

*herself* → ε, *her*, *themself*, *her self*, *for herself*, *by herself*, *himself*

### 3sng_fem_pobj_reflexive

cond: dependency tag is `pobj`

*herself* → *her*, *her self*, *themself*, *she*, *himself*

## 3rd singular inanimate

### 3sng_inan_subj

cond: dependency tag is `nsubj`, `nsubjpass`, `conj`, `appos`, `nmod`, `compound`, or `attr`

*it* → ε, *its*, *they*, *he*, *she*, *this*, *that*, *which*

### 3sng_inan_pobj

cond: dependency tag is `pobj`

*it* → *its*, *them*, *him*, *her*, *this*, *that*, *which*

### 3sng_inan_dobj

cond: dependency tag is `dobj`

*it* → ε, *its*, *them*, *him*, *her*, *this*, *that*, *which*, *for it*, *to it*, *on it*, *in it*, *at it*, *of it*

### 3sng_inan_dative

cond: dependency tag is `dative`

*it* → ε, *its*, *her*, *him*, *them*, *for it*, *to it*, *on it*, *in it*, *at it*

### 3sng_inan_poss

*its* → ε, *it*, *thers*, *their*, *his*, *hers*, *whose*, *a*, *an*, *the*

### 3sng_inan_reflexive

cond: dependency tag is `dobj`, `conj`, `nsubj`, `nsubjpass`, `npadvmod`, `dative`, or `attr`

*itself* → ε (0.2),
*to itself* (0.1),
*fo itself* (0.1),
*for itself* (0.1),
*by itself* (0.1),
*with itself* (0.1),
*themself* (0.005),
*to themself* (0.005),
*of themself* (0.005),
*for themself* (0.005),
*by themself* (0.005),
*with themself* (0.005),
*themselves* (0.005),
*to themselves* (0.005),
*of themselves* (0.005),
*for themselves* (0.005),
*by themselves* (0.005),
*with themselves* (0.005),
*itselves* (0.005),
*to itselves* (0.005),
*of itselves* (0.005),
*for itselves* (0.005),
*by itselves* (0.005),
*with itselves* (0.005),
*himself* (0.005),
*to himself* (0.005),
*of himself* (0.005),
*for himself* (0.005),
*by himself* (0.005),
*with himself* (0.005),
*herself* (0.005),
*to herself* (0.005),
*of herself* (0.005),
*for herself* (0.005),
*by herself* (0.005),
*with herself* (0.005),
*she* (0.025),
*her* (0.025),
*hers* (0.025),
*he* (0.025),
*him* (0.025),
*his* (0.025)

### 3sng_inan_appos_reflexive

cond: dependency tag is `appos`

*itself* → ε, *it*, *they*, *them*, *themselves*, *it self*, *for itself*, *by itself*, *themself*, *herself*, *himself*

### 3sng_inan_pobj_reflexive

cond: dependency tag is `pobj`

*itself* → *it*, *it self*, *herself*, *himself*

## 3rd singular masculine

### 3sng_masc_subj

cond: dependency tag is `nsubj`, `nsubjpass`, `conj`, `appos`, `nmod`, `compound`, `attr`

*he* → *she*, *his*, *him*, *they*, *them*, *their*

### 3sng_masc_pobj

cond: dependency tag is `pobj`

*him* → *her*, *he*, *his*, *their*, *them*, *himself*

### 3sng_masc_dobj

cond: dependency tag is `dobj`

*him* → ε (0.1), *her* (0.05), *he* (0.05), *for him* (0.3), *to him* (0.3), *on him* (0.05), *in him* (0.05), *at him* (0.05), *of him* (0.05)

### 3sng_masc_nsubj_obj

cond: dependency tag is `nsubj`, `nsubjpass`, `conj`, `appos`, `nmod`, `compound`, or `attr`

*him* → ε, *her*, *he*, *his*

### 3sng_masc_dative

cod: dependency tag is `dative`

*him* → ε (0.1), *her* (0.05), *he* (0.05), *for him* (0.3), *to him* (0.35), *on him* (0.05), *in him* (0.05), *at him* (0.05)

### 3sng_masc_poss

*his* → ε, *he*, *him*, *her*, *a*, *an*, *the*, *its*, *theirs*

### 3sng_masc_reflexive

cond: dependency tag is `dobj`, `conj`, `nsubj`, `nsubjpass`, `npadvmod`, `dative`, or `attr`

*himself* → ε (0.2),
*to himself* (0.1),
*of himself* (0.1),
*for himself* (0.1),
*by himself* (0.1),
*with himself* (0.1),
*himselves* (0.01),
*to himselves* (0.01),
*of himselves* (0.01),
*for himselves* (0.01),
*by himselves* (0.01),
*with himselves* (0.01),
*themself* (0.01),
*to themself* (0.01),
*of themself* (0.01),
*for themself* (0.01),
*by themself* (0.01),
*with themself* (0.01),
*he* (0.045),
*his* (0.045),
*him* (0.045),
*herself* (0.045)

### 3sng_masc_appos_reflexive

cond: dependency tag is `appos`

*himself* → ε, *him*, *themself*, *him self*, *for himself*, *by himself*, *herself*

### 3sng_masc_pobj_reflexive

cond: dependency tag is `pobj`

*himself* → ε, *him*, *him self*, *themself*, *he*, *herself*

## 3rd plural

### 3plu_subj

cond: dependency tag is `nsubj`, `nsubjpass`, `conj`, `appos`, `nmod`, `compound`, or `attr`

*they* → *them*, *their*, *he*, *him*, *she*, *her*, *themself*, *themselves*

### 3plu_pobj

cond: dependency tag is `pobj`

*them* → *they*, *their*, *him*, *her*

### 3plu_dobj

cond: dependency tag is `dobj`

*them* → ε (0.05), *they* (0.05), *her* (0.05), *him* (0.05), *for them* (0.2), *to them* (0.2), *on them* (0.1), *in them* (0.1), *at them* (0.1), *of them* (0.1)

### 3plu_nsubj_obj

cond: dependency tag is `nsubj`, `nsubjpass`, `conj`, `appos`, `nmod`, `compound`, or `attr`

*them* → ε, *they*, *their*, *him*, *her*

### 3plu_dative

cond: dependency tag is `dative`

*them* → ε (0.05), *they* (0.05), *him* (0.05), *her* (0.05), *for them* (0.3), *to them* (0.35), *on them* (0.05), *in them* (0.05), *at them* (0.05)

### 3plu_poss

*theirs* → ε, *they*, *them*, *their*, *its*, *his*, *hers*

### 3plu_poss_det

*their* → ε, *they*, *them*, *theirs*, *a*, *an*, *the*, *its*, *his*, *her*

### 3sng_neut_reflexive

cond: dependency tag is `dobj`, `conj`, `nsubj`, `nsubjpass`, `npadvmod`, `dative`, or `attr`

*themself* → ε (0.2)
*to themself* (0.1),
*of themself* (0.1),
*for themself* (0.1),
*by themself* (0.1),
*with themself* (0.1),
*themselves* (0.01),
*to themselves* (0.01),
*of themselves* (0.01),
*for themselves* (0.01),
*by themselves* (0.01),
*with themselves* (0.01),
*himself* (0.005),
*to himself* (0.005),
*of himself* (0.005),
*for himself* (0.005),
*by himself* (0.005),
*with himself* (0.005),
*herself* (0.005),
*to herself* (0.005),
*of herself* (0.005),
*for herself* (0.005),
*by herself* (0.005),
*with herself* (0.005),
*she* (0.03),
*her* (0.03),
*hers* (0.03),
*he* (0.03),
*him* (0.03),
*his* (0.03)

### 3sng_neut_appos_reflexive

cond: dependency tag is `appos`




*themself* → ε, *they*, *them*, *themselves*, *them self*, *for themself*, *by themself*, *by himself*, *herself*, *himself*

### 3sng_neut_pobj_reflexive

cond: dependency tag is `pobj`

*themself* → *them*, *them self*, *herself*, *himself*

### 3plu_reflexive

cond: dependency tag is `dobj`, `conj`, `nsubj`, `nsubjpass`, `npadvmod`, `dative`, or `attr`

*themself* → ε (0.2)
*to themselves* (0.1),
*of themselves* (0.1),
*for themselves* (0.1),
*by themselves* (0.1),
*with themselves* (0.1),
*themself* (0.01),
*to themself* (0.01),
*of themself* (0.01),
*for themself* (0.01),
*by themself* (0.01),
*with themself* (0.01),
*himself* (0.005),
*to himself* (0.005),
*of himself* (0.005),
*for himself* (0.005),
*by himself* (0.005),
*with himself* (0.005),
*herself* (0.005),
*to herself* (0.005),
*of herself* (0.005),
*for herself* (0.005),
*by herself* (0.005),
*with herself* (0.005),
*they* (0.06),
*them* (0.06),
*their* (0.06)

### 3plu_appos_reflexive

cond: dependency tag is `appos`

*themself* → ε, *they*, *them*, *themselves*, *them self*, *for themself*, *by themself*, *by himself*, *herself*, *himself*

### 3sng_neut_pobj_reflexive

cond: dependency tag is `pobj`

*themself* → *them*, *them self*, *herself*, *himself*

### 3plu_reflexive

cond: dependency tag is `dobj`, `conj`, `nsubj`, `nsubjpass`, `npadvmod`, `dative`, or `attr`

*themself* → ε (0.2)
*to themselves* (0.1),
*of themselves* (0.1),
*for themselves* (0.1),
*by themselves* (0.1),
*with themselves* (0.1),
*themself* (0.01),
*to themself* (0.01),
*of themself* (0.01),
*for themself* (0.01),
*by themself* (0.01),
*with themself* (0.01),
*himself* (0.005),
*to himself* (0.005),
*of himself* (0.005),
*for himself* (0.005),
*by himself* (0.005),
*with himself* (0.005),
*herself* (0.005),
*to herself* (0.005),
*of herself* (0.005),
*for herself* (0.005),
*by herself* (0.005),
*with herself* (0.005),
*they* (0.06),
*them* (0.06),
*their* (0.06)

### 3plu_appos_reflexive

cond: dependency tag is `appos`

I mistook and forgot adding *by herself* in them.

*themself* → ε, *they*, *them*, *themselves*, *them self*, *for themself*, *by themself*, *by himself*, *herself*, *himself*

### 3sng_neut_pobj_reflexive

cond: dependency tag is `pobj`

*themself* → *them*, *them self*, *herself*, *himself*

### 3plu_reflexive

cond: dependency tag is `dobj`, `conj`, `nsubj`, `nsubjpass`, `npadvmod`, `dative`, or `attr`

*themself* → ε (0.2)
*to themselves* (0.1),
*of themselves* (0.1),
*for themselves* (0.1),
*by themselves* (0.1),
*with themselves* (0.1),
*themself* (0.01),
*to themself* (0.01),
*of themself* (0.01),
*for themself* (0.01),
*by themself* (0.01),
*with themself* (0.01),
*himself* (0.005),
*to himself* (0.005),
*of himself* (0.005),
*for himself* (0.005),
*by himself* (0.005),
*with himself* (0.005),
*herself* (0.005),
*to herself* (0.005),
*of herself* (0.005),
*for herself* (0.005),
*by herself* (0.005),
*with herself* (0.005),
*they* (0.06),
*them* (0.06),
*their* (0.06)

### 3plu_appos_reflexive

cond: dependency tag is `appos`

I mistook and forgot adding *by herself* in them.

*themself* → ε, *they*, *them*, *themselves*, *them self*, *for themself*, *by themself*, *by himself*, *herself*, *himself*

### 3sng_neut_pobj_reflexive

cond: dependency tag is `pobj`

*themself* → *them*, *them self*, *herself*, *himself*

### 3plu_reflexive

cond: dependency tag is `dobj`, `conj`, `nsubj`, `nsubjpass`, `npadvmod`, `dative`, or `attr`

*themself* → ε (0.2)
*to themselves* (0.1),
*of themselves* (0.1),
*for themselves* (0.1),
*by themselves* (0.1),
*with themselves* (0.1),
*themself* (0.01),
*to themself* (0.01),
*of themself* (0.01),
*for themself* (0.01),
*by themself* (0.01),
*with themself* (0.01),
*himself* (0.005),
*to himself* (0.005),
*of himself* (0.005),
*for himself* (0.005),
*by himself* (0.005),
*with himself* (0.005),
*herself* (0.005),
*to herself* (0.005),
*of herself* (0.005),
*for herself* (0.005),
*by herself* (0.005),
*with herself* (0.005),
*they* (0.06),
*them* (0.06),
*their* (0.06)

### 3plu_appos_reflexive

cond: dependency tag is `appos`

I mistook and forgot adding *by herselves* in them.

*themselves* → ε, *they*, *them*, *themself*, *them selves*, *for themselves*, *by themselves*, *by himselves*, *herself*, *himself*

### 3plu_pobj_reflexive

cond: dependency tag is `pobj`

*themselves* → *them*, *them selves*, *herself*, *himself*

