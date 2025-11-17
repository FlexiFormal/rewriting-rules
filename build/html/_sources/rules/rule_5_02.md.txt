Rule 5.2: "Let" Comprehension Term Reduction
============================================


```{rewrite-rule}
let : <let> = "let"

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":let: $:x: \in \{:y: \mid :P:[:y:]\}$"

--- "Let" Comprehension Term Reduction

":let: :x: be an element such that $:P:[:x:]$"
```


Examples
--------

```{rewrite-rule}
"let $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$"

--- "Let" Comprehension Term Reduction

"let $x$ be an element such that $x^n = 1$ for some $n \in \mathbb{N}$"
```
