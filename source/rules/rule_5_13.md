Rule 5.13: Determiner-AP Comprehension Term Reduction
=====================================================


```{rewrite-rule}
Det : <Det> = "all"

opt_NP_or_AP : [<NP> | <AP>] = ""

AP : <AP> = "imaginary"

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":Det: :opt_NP_or_AP: $:x: \in \{:y: \mid :P:[:y:]\}$ that is :AP:"

--- Determiner-AP Comprehension Term Reduction

":Det: :AP: :opt_NP_or_AP: :x: with $:P:[:x:]$"
```


Examples
--------

```{rewrite-rule}
"all $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that are imaginary"

--- Determiner-AP Comprehension Term Reduction

"all imaginary $x$ with $x^n = 1$ for some $n \in \mathbb{N}$"
```

```{rewrite-rule}
"those complex numbers $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that are imaginary"

--- Determiner-AP Comprehension Term Reduction

"those imaginary complex numbers $x$ with $x^n = 1$ for some $n \in \mathbb{N}$"
```

```{rewrite-rule}
"certain real $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that are positive"

--- Determiner-AP Comprehension Term Reduction

"certain positive real $x$ with $x^n = 1$ for some $n \in \mathbb{N}$"
```
