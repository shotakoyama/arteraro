# inflection

## adj_infl

This rule changes inflection of adjective.
It changes the form to JJ, JJR, or JJS using `lemminflect`.

## noun_infl

This rule changes inflection of noun.
It changes the form to NN, NNS using `lemminflect`.

## verb_infl

This rule changes inflection of verb.
It changes the form to VB, VBD, VBG, VBN, VBP or VBZ.
If the preceeding word do not have POS tag `AUX`, this rule randomly inserts words (
*have*, *has*, *had*,  *have been*, *have be*, *have being*, *has been*, *has be*, *has being*, *had been*, *had be*, *had being*, *be*, *am*, *is*, *are*, *was*, *were* for VBZ,
*have been*, *have be*, *have being*, *has been*, *has be*, *has being*, *had been*, *had be*, *had being*, *be*, *am*, *is*, *are*, *was*, *were* for VBN)

