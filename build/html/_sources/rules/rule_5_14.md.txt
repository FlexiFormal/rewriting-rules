Rule 5.14: Determiner-VP Comprehension Term Reduction
=====================================================


```{rewrite-rule}
{ph}`Det` : {cat}`Det` = {nl}`all`

{ph}`opt_NP_or_AP` : [{cat}`NP` | {cat}`AP`] = {nl}``

{ph}`VP` : {cat}`VP` = {nl}`solve the equation $E$`

{ph}`x` : {cat}`Var` = {nl}`$x$`

{ph}`y` : {cat}`Var` = {nl}`$z$`

{ph}`P`[{ph}`a`] : {cat}`Pred` = {nl}`${ph}`a`^n = 1 \text{ for some } n \in \mathbb{N}$`

{ph}`Det` {ph}`opt_NP_or_AP` ${ph}`x` \in \{{ph}`y` \mid {ph}`P`[{ph}`y`]\}$ that {ph}`VP`

{ph}`Det` {ph}`opt_NP_or_AP` {ph}`x` that {ph}`VP` with ${ph}`P`[{ph}`x`]$
```


Examples
--------

```{rewrite-rule}
all $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that solve the equation $E$

all $x$ that solve the equation $E$ with $x^n = 1$ for some $n \in \mathbb{N}$
```

```{rewrite-rule}
those complex numbers $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that solve the equation $E$

those complex numbers $x$ that solve the equation $E$ with $x^n = 1$ for some $n \in \mathbb{N}$
```

```{rewrite-rule}
certain imaginary $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that solve the equation $E$

certain imaginary $x$ that solve the equation $E$ with $x^n = 1$ for some $n \in \mathbb{N}$
```
