Rule 5.7: "Choose"-NP Comprehension Term Reduction
==================================================


```{rewrite-rule}
choose : <choose> = "choose"

NP : <NP> = "real number"

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":choose: a $:x: \in \{:y: \mid :P:[:y:]\}$ that is a :NP:"

--- "Choose"-NP Comprehension Term Reduction

":choose: a :NP: :x: with $:P:[:x:]$"
```


Examples
--------

```{rewrite-rule}
"choose an $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that is a real number"

"choose a real number $x$ with $x^n = 1$ for some $n \in \mathbb{N}$"
```
