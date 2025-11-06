Rule 3.1: Adjective Determiner Reduction
========================================

```{rewrite-rule}
Adj : <Adj> = "applicable"

Prep : <Prep> = "in"

t : <Term> = "$q$"

Det : <Det> = "a"

NP : <NP> = "non-initial state"

":Adj: :Prep: :t: for :Det: :NP: :t:"

":Adj: :Prep: :Det: :NP: :t:"
```


Examples
--------

```{rewrite-rule}
"applicable in $q$ for a non-initial state $q$"

"applicable in a non-initial state $q$"
```
