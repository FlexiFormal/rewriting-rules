Rule 5.8: "Choose"-AP Comprehension Term Reduction
==================================================


```{rewrite-rule}
choose : <choose> = "choose"

AP : <AP> = "imaginary"

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":choose: a $:x: \in \{:y: \mid :P:[:y:]\}$ that is a :AP:"

--- "Choose"-AP Comprehension Term Reduction

":choose: a :AP: :x: with $:P:[:x:]$"
```


Examples
--------

```{rewrite-rule}
"choose an $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that is imaginary"

--- "Choose"-AP Comprehension Term Reduction

"choose an imaginary $x$ with $x^n = 1$ for some $n \in \mathbb{N}$"
```
