Rule 2.3: Atom Variable Reduction
=================================

```{rewrite-rule}
NP : <NP> = "a state"

t : <Term> = "$q$"

R[x] : <guarded identifier> = "$:x: \in Q \setminus F$"

":NP: :t: @such that | with@ :R:[:t:]"

--- Atom Variable Reduction

":NP: :R:[:t:]"
```


Examples
--------

```{rewrite-rule}
"a state $q$ with $q \in Q \setminus F$"

--- Atom Variable Reduction

"a state $q \in Q \setminus F$"
```
