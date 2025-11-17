Rule 6.2: Iota-Subset Reduction
===============================


```{rewrite-rule}
a : <Term> = "$n - 5$"

A : <Term> = "$\mathbb{Z}$"

"$\{:a:\} \subseteq :A:$"

--- Iota-Subset Reduction

"$:a: \in :A:$"
```


Examples
--------

```{rewrite-rule}
"$\{n - 5\} \subseteq \mathbb{Z}$"

--- Iota-Subset Reduction

"$n - 5 \in \mathbb{Z}$"
```
