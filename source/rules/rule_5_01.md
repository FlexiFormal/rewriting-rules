Rule 5.1: "Then" Comprehension Term Reduction
=============================================


```{rewrite-rule}
then : <then> = "assume"

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1$ for some $n \in \mathbb{N}$"

":then: $:x: \in \{:y: \mid :P:[:y:]\}$"

":then: :P:[:x:]"
```


Examples
--------

```{rewrite-rule}
"assume $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$"

"assume $x^n = 1$ for some $n \in \mathbb{N}$"
```
