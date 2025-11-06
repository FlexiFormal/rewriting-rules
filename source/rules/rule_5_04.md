Rule 5.4: "Let"-AP Comprehension Term Reduction
===============================================


```{rewrite-rule}
let : <let> = "let"

AP : <AP> = "imaginary"

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":let: $:x: \in \{:y: \mid :P:[:y:]\}$ be :AP:"

":let: :x: be :AP: such that $:P:[:x:]$"
```


Examples
--------

```{rewrite-rule}
"let $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ be imaginary"

"let $x$ be imaginary such that $x^n = 1$ for some $n \in \mathbb{N}$"
```
