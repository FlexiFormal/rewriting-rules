Rule 3.2: Atom Determiner Reduction
===================================

```{rewrite-rule}
{ph}`Det` : {cat}`Det` = {nl}`those`

{ph}`opt_NP` : [{cat}`NP`] = {nl}`states`

{ph}`t` : {cat}`Term` = {nl}`$q$`

{ph}`R`$[${ph}`x`$]$ : {cat}`guarded identifier` = {nl}``{ph}`x` $\in Q \setminus F$``

{ph}`Det` {ph}`opt_NP` {ph}`t` with {ph}`R`$[${ph}`t`$]$

{ph}`Det` {ph}`opt_NP` {ph}`R`$[${ph}`t`$]$
```

Example:

```{rewrite-rule}
those states $q$ with $q \in Q \setminus F$

those states $q \in Q \setminus F$
```

