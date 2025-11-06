Rule 5.6: "Choose" Comprehension Term Reduction
===============================================


```{rewrite-rule}
choose : <choose> = "choose"

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":choose: a $:x: \in \{:y: \mid :P:[:y:]\}$"

":choose: a :x: with $:P:[:x:]$"
```


Examples
--------

```{rewrite-rule}
"choose an $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$"

"choose an $x$ with $x^n = 1$ for some $n \in \mathbb{N}$"
```
