Rule 3.2: Atom Determiner Reduction
===================================

```{rewrite-rule}
Det : <Det> = "those"

NP_opt : [<NP>] = "states"

t : <Term> = "$q$"

R[x] : <guarded identifier> = "$:x: \in Q \setminus F$"

":Det: :NP_opt: :t: with :R:[:t:]"

--- Atom Determiner Reduction

":Det: :NP_opt: :R:[:t:]"
```

Example:

```{rewrite-rule}
"those states $q$ with $q \in Q \setminus F$"

--- Atom Determiner Reduction

"those states $q \in Q \setminus F$"
```

