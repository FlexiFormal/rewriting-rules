Rule 2.3: Atom Variable Reduction
=================================

```{rewrite-rule}
{ph}`NP` : {cat}`NP` = {nl}`a state`

{ph}`t` : {cat}`Term` = {nl}`$q$`

{ph}`R`$[${ph}`x`$]$ : {cat}`guarded identifier` = {nl}``{ph}`x` $\in Q \setminus F$``

{ph}`NP` {ph}`t` (such that | with) {ph}`R`$[${ph}`t`$]$

{ph}`NP` {ph}`R`$[${ph}`t`$]$
```


Examples
--------

```{rewrite-rule}
a state $q$ with $q \in Q \setminus F$

a state $q \in Q \setminus F$
```
