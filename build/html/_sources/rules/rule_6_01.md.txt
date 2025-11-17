Rule 6.1: Iota-Element Reduction
================================


```{rewrite-rule}
a : <Term> = "$0$"

b : <Term> = "$b$"

"$:b: \in \{:a:\}$"

--- Iota-Element Reduction

"$:b: = :a:$"
```


Examples
--------

```{rewrite-rule}
"$b \in \{0\}$"

--- Iota-Element Reduction

"$b = 0$"
```
