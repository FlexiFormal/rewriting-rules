Rule 3.2: Atom Determiner Reduction
===================================

```{rewrite-rule}
Det : <Det> = "those"

opt_NP : [<NP>] = "states"

t : <Term> = "$q$"

R`[x] : <guarded identifier> = "$:x: \in Q \setminus F$"

":Det: :opt_NP: :t: with :R:[:t:]"

":Det: :opt_NP: :R:[:t:]"
```

Example:

```{rewrite-rule}
"those states $q$ with $q \in Q \setminus F$"

"those states $q \in Q \setminus F$"
```

