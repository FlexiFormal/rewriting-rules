Rule 5.18: Relation Guard Reduction
===================================


```{rewrite-rule}
R[a] : <Guarded Identifier> = "$1 \leq :a: \leq n$"

y : <Var> = "$y$"

P[b] : <Pred> = "$1/:b: < \varepsilon$"

"$\{:R:[:y:] \mid :P:[:y:]\}$"

--- Relation Guard Reduction

"$\{:y: \mid :R:[:y:] \text{ and } :P:[:y:]\}$"
```


Examples
--------

```{rewrite-rule}
"$\{1 \leq i \leq n \mid 1/i < \varepsilon\}$"

--- Relation Guard Reduction

"$\{i \mid 1 \leq i \leq n \text{ and } 1/i < \varepsilon\}$"
```
