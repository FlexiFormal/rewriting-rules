Rule 5.17: Term Guard Reduction
===============================


```{rewrite-rule}
t[a_1, ..., a_n] : <Term> = "${ph}"a`^2$`

y_1, ..., y_n : <Var> = "$y$"

P[b_1, ..., b_n] : <Pred> = "$:b: \in \mathbb{N}$"

z : <Var> = "$z$"

"$\{:t:[:y_1:, \dots, :y_n:] \mid :P:[:y_1:, \dots, :y_n:]\}$"

--- Term Guard Reduction

"$\{:z: \mid \text{there exist } :y_1:, \dots, :y_n: \text{ such that } :z: = :t:[:y_1:, \dots, :y_n:] \text{ and } :P:[:y_1:, \dots, :y_n:]\}$"
```


Examples
--------

```{rewrite-rule}
"$\{n^2 \mid n \in \mathbb{N}\}$"

"$\{z \mid \text{there exist an } n \text{ such that } z = n^2 \text{ and } n \in \mathbb{N}\}$"
```
