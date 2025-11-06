Rule 5.15: Determiner-PP Comprehension Term Reduction
=====================================================


```{rewrite-rule}
Det : <Det> = "all"

opt_NP_or_AP : [<NP> | <AP>] = ""

Prop : <Prop> = "$\Re(x) > 0$"

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":Det: :opt_NP_or_AP: $:x: \in \{:y: \mid :P:[:y:]\}$ with :Prop:"

":Det: :opt_NP_or_AP: :x: with $:P:[:x:]$ and :Prop:"
```


Examples
--------

```{rewrite-rule}
"all $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ with $\Re(x) > 0$"

"all $x$ with $x^n = 1$ for some $n \in \mathbb{N}$ and $\Re(x) > 0$"
```

```{rewrite-rule}
"those complex numbers $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ with $\Re(x) > 0$"

"those complex numbers $x$ with $x^n = 1$ for some $n \in \mathbb{N}$ and $\Re(x) > 0$"
```

```{rewrite-rule}
"certain imaginary $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ with $\Re(x) > 0$"

"certain imaginary $x$ with $x^n = 1$ for some $n \in \mathbb{N}$ and $\Re(x) > 0$"
```
