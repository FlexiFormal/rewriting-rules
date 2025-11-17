Rule 5.11: Determiner Comprehension Term Reduction
==================================================


```{rewrite-rule}
Det : <Det> = "all"

NPorAP_opt : [<NP> | <AP>] = ""

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":Det: :NPorAP_opt: $:x: \in \{:y: \mid :P:[:y:]\}$"

--- Determiner Comprehension Term Reduction

":Det: :NPorAP_opt: :x: with $:P:[:x:]$"
```


Examples
--------

```{rewrite-rule}
"all $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$"

--- Determiner Comprehension Term Reduction

"all $x$ with $x^n = 1$ for some $n \in \mathbb{N}$"
```

```{rewrite-rule}
"those complex numbers $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$"

--- Determiner Comprehension Term Reduction

"those complex numbers $x$ with $x^n = 1$ for some $n \in \mathbb{N}$"
```

```{rewrite-rule}
"certain imaginary $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$"

--- Determiner Comprehension Term Reduction

"certain imaginary $x$ with $x^n = 1$ for some $n \in \mathbb{N}$"
```
