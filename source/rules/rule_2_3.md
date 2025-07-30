Rule 2.3: Atom Variable Reduction
=================================

Let $R[x]$ be a [guarded identifier](/guarded_identifiers.md).


```{rewrite-rule}
{ph}`NP` $x$ (such that | with) $R[x]$.

{ph}`NP` $R[x]$.
```


Examples
--------

```{rewrite-rule}
a state $q$ with $q \in Q \setminus F$

a state $q \in Q \setminus F$
```
