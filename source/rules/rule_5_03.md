Rule 5.3: "Let"-NP Comprehension Term Reduction
===============================================


```{rewrite-rule}
let : <let> = "let"

NP : <NP> = "complex number"

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":let: $:x: \in \{:y: \mid :P:[:y:]\}$ be a :NP:"

--- "Let"-NP Comprehension Term Reduction

":let: :x: be a :NP: such that $:P:[:x:]$"
```


Examples
--------

```{rewrite-rule}
"let $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ be a complex number"

"let $x$ be a complex number such that $x^n = 1$ for some $n \in \mathbb{N}$"
```
