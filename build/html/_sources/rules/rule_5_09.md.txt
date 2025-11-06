Rule 5.9: "Choose"-VP Comprehension Term Reduction
==================================================


```{rewrite-rule}
choose : <choose> = "choose"

VP : <VP> = "solve the equation $E$"

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":choose: a $:x: \in \{:y: \mid :P:[:y:]\}$ that :VP:"

":choose: a :x: that :VP: with $:P:[:x:]$"
```


Examples
--------

```{rewrite-rule}
"choose an $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that solves the equation $E$"

"choose an $x$ that solves the equation $E$ with $x^n = 1$ for some $n \in \mathbb{N}$"
```
