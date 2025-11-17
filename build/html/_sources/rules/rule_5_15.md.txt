Rule 5.15: Determiner-PP Comprehension Term Reduction
=====================================================


```{rewrite-rule}
Det : <Det> = "all"

NPorAP_opt : [<NP> | <AP>] = ""

Prop : <Prop> = "$\Re(x) > 0$"

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":Det: :NPorAP_opt: $:x: \in \{:y: \mid :P:[:y:]\}$ with :Prop:"

--- Determiner-PP Comprehension Term Reduction

":Det: :NPorAP_opt: :x: with $:P:[:x:]$ and :Prop:"
```


Examples
--------

```{rewrite-rule}
"all $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ with $\Re(x) > 0$"

--- Determiner-PP Comprehension Term Reduction

"all $x$ with $x^n = 1$ for some $n \in \mathbb{N}$ and $\Re(x) > 0$"
```

```{rewrite-rule}
"those complex numbers $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ with $\Re(x) > 0$"

--- Determiner-PP Comprehension Term Reduction

"those complex numbers $x$ with $x^n = 1$ for some $n \in \mathbb{N}$ and $\Re(x) > 0$"
```

```{rewrite-rule}
"certain imaginary $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ with $\Re(x) > 0$"

--- Determiner-PP Comprehension Term Reduction

"certain imaginary $x$ with $x^n = 1$ for some $n \in \mathbb{N}$ and $\Re(x) > 0$"
```
