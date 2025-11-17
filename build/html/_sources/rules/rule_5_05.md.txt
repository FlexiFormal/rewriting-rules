Rule 5.5: "Let"-PP Comprehension Term Reduction
===============================================


```{rewrite-rule}
let : <let> = "let"

Prop : <Prop> = "$\Im(x) > 0$"

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":let: $:x: \in \{:y: \mid :P:[:y:]\}$ with :Prop:"

--- "Let"-PP Comprehension Term Reduction

":let: :x: be an element such that $:P:[:x:]$ and :Prop:"
```


Examples
--------

```{rewrite-rule}
"let $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ with $\Im(x) > 0$"

--- "Let"-PP Comprehension Term Reduction

"let $x$ be an element such that $x^n = 1$ for some $n \in \mathbb{N}$ and $\Im(x) > 0$"
```
