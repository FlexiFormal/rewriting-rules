Rule 2.3: Atom Variable Reduction
=================================

Let $R$ be a symbolic atomic formula with a free variable $x$.


```{note}
There are some additional restrictions.
Something like that $x$ must be the first occurrence of an identifier in $R$.
```



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
