Rule 3.3: Tuple Determiner Reduction
====================================


```{rewrite-rule}
{ph}`Det` $x_1, \ldots, x_n$ with $\langle x_1, \ldots, x_n \rangle \in X_1 \times \ldots \times X_N$

{ph}`Det` $\langle x_1, \ldots, x_n \rangle \in X_1 \times \ldots \times X_N$
```

````{note}
This could also be considered a special case of
a generalized form of [Rule 3.2](rule_3_2.md):

```{rewrite-rule}
{ph}`Det` [{ph}`NP`] $x_1, \ldots, x_n$ with $R[x_1, \ldots, x_n]$

{ph}`Det` [{ph}`NP`] $R[x_1, \ldots, x_n]$
```
````

Example:

```{rewrite-rule}
any $x, y$ with $\langle x, y \rangle \in \mathbb{R} \times \mathbb{R}$

any $\langle x, y \rangle \in \mathbb{R} \times \mathbb{R}$
```


