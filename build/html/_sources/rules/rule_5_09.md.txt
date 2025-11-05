Rule 5.9: "Choose"-VP Comprehension Term Reduction
==================================================


```{rewrite-rule}
{ph}`choose` : {cat}`choose` = {nl}`choose`

{ph}`VP` : {cat}`VP` = {nl}`solve the equation $E$`

{ph}`x` : {cat}`Var` = {nl}`$x$`

{ph}`y` : {cat}`Var` = {nl}`$z$`

{ph}`P`[{ph}`a`] : {cat}`Pred` = {nl}`${ph}`a`^n = 1 \text{ for some } n \in \mathbb{N}$`

{ph}`choose` a ${ph}`x` \in \{{ph}`y` \mid {ph}`P`[{ph}`y`]\}$ that {ph}`VP`

{ph}`choose` a {ph}`x` that {ph}`VP` with ${ph}`P`[{ph}`x`]$
```


Examples
--------

```{rewrite-rule}
choose an $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that solves the equation $E$

choose an $x$ that solves the equation $E$ with $x^n = 1$ for some $n \in \mathbb{N}$
```
