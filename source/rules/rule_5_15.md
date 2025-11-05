Rule 5.15: Determiner-PP Comprehension Term Reduction
=====================================================


```{rewrite-rule}
{ph}`Det` : {cat}`Det` = {nl}`all`

{ph}`opt_NP_or_AP` : [{cat}`NP` | {cat}`AP`] = {nl}``

{ph}`Prop` : {cat}`Prop` = {nl}`$\Re(x) > 0$`

{ph}`x` : {cat}`Var` = {nl}`$x$`

{ph}`y` : {cat}`Var` = {nl}`$z$`

{ph}`P`[{ph}`a`] : {cat}`Pred` = {nl}`${ph}`a`^n = 1 \text{ for some } n \in \mathbb{N}$`

{ph}`Det` {ph}`opt_NP_or_AP` ${ph}`x` \in \{{ph}`y` \mid {ph}`P`[{ph}`y`]\}$ with {ph}`Prop`

{ph}`Det` {ph}`opt_NP_or_AP` {ph}`x` with ${ph}`P`[{ph}`x`]$ and {ph}`Prop`
```


Examples
--------

```{rewrite-rule}
all $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ with $\Re(x) > 0$

all $x$ with $x^n = 1$ for some $n \in \mathbb{N}$ and $\Re(x) > 0$
```

```{rewrite-rule}
those complex numbers $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ with $\Re(x) > 0$

those complex numbers $x$ with $x^n = 1$ for some $n \in \mathbb{N}$ and $\Re(x) > 0$
```

```{rewrite-rule}
certain imaginary $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ with $\Re(x) > 0$

certain imaginary $x$ with $x^n = 1$ for some $n \in \mathbb{N}$ and $\Re(x) > 0$
```
