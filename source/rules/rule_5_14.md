Rule 5.14: Determiner-VP Comprehension Term Reduction
=====================================================


```{rewrite-rule}
Det : <Det> = "all"

NPorAP_opt : [<NP> | <AP>] = ""

VP : <VP> = "solve the equation $E$"

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":Det: :NPorAP_opt: $:x: \in \{:y: \mid :P:[:y:]\}$ that :VP:"

--- Determiner-VP Comprehension Term Reduction

":Det: :NPorAP_opt: :x: that :VP: with $:P:[:x:]$"
```


Examples
--------

```{rewrite-rule}
"all $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that solve the equation $E$"

--- Determiner-VP Comprehension Term Reduction

"all $x$ that solve the equation $E$ with $x^n = 1$ for some $n \in \mathbb{N}$"
```

```{rewrite-rule}
"those complex numbers $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that solve the equation $E$"

--- Determiner-VP Comprehension Term Reduction

"those complex numbers $x$ that solve the equation $E$ with $x^n = 1$ for some $n \in \mathbb{N}$"
```

```{rewrite-rule}
"certain imaginary $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that solve the equation $E$"

--- Determiner-VP Comprehension Term Reduction

"certain imaginary $x$ that solve the equation $E$ with $x^n = 1$ for some $n \in \mathbb{N}$"
```
