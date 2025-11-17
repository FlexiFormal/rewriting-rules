Rule 5.13: Determiner-AP Comprehension Term Reduction
=====================================================


```{rewrite-rule}
Det : <Det> = "all"

NPorAP_opt : [<NP> | <AP>] = ""

AP : <AP> = "imaginary"

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":Det: :NPorAP_opt: $:x: \in \{:y: \mid :P:[:y:]\}$ that is :AP:"

--- Determiner-AP Comprehension Term Reduction

":Det: :AP: :NPorAP_opt: :x: with $:P:[:x:]$"
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
