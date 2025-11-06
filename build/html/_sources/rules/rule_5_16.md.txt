Rule 5.16: Subset Comprehension Term Reduction
==============================================


```{rewrite-rule}
then : <then> = "assume"

y : <Var> = "$z$"

X : <Var> = "$X$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":then: $\{:y: \mid :P:[:y:]\} \subseteq :X:$"

":then: $:y: \in :X:$ for all :y: with $:P:[:y:]$"
```


Examples
--------

```{rewrite-rule}
"assume $\{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\} \subseteq X$"

"assume $z \in X$ for all $z$ with $z^n = 1$ for some $n \in \mathbb{N}$"
```
