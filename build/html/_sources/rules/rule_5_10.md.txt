Rule 5.10: "Choose"-PP Comprehension Term Reduction
===================================================


```{rewrite-rule}
choose : <choose> = "choose"

Prop : <Prop> = "$\Re(x) > 0$"

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":choose: a $:x: \in \{:y: \mid :P:[:y:]\}$ with :Prop:"

--- "Choose"-PP Comprehension Term Reduction

":choose: a :x: with $:P:[:x:]$ and :Prop:"
```


Examples
--------

```{rewrite-rule}
"choose an $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ with $\Re(x) > 0$"

--- "Choose"-PP Comprehension Term Reduction

"choose an $x$ with $x^n = 1$ for some $n \in \mathbb{N}$ and $\Re(x) > 0$"
```
