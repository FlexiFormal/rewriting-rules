Rule 3.2: Atom Determiner Reduction
===================================

Let $R[x]$ be a [guarded identifier](/guarded_identifiers.md).

```{rewrite-rule}
{ph}`Det` [{ph}`NP`] $x$ with $R[x]$

{ph}`Det` [{ph}`NP`] $R[x]$
```

Example:

```{rewrite-rule}
those states $q$ with $q \in Q \setminus F$

those states $q \in Q \setminus F$
```

