Rule 5.1: "Then" Comprehension Term Reduction
=============================================


```{rewrite-rule}
{ph}`then` : {cat}`then` = {nl}`assume`

{ph}`x` : {cat}`Var` = {nl}`$x$`

{ph}`y` : {cat}`Var` = {nl}`$z$`

{ph}`P`[{ph}`a`] : {cat}`Pred` = {nl}``{ph}`a`$^n = 1$ for some $n \in \mathbb{N}$``

{ph}`then` {ph}`x` $\in \{${ph}`y` $\mid$ {ph}`P`$[${ph}`y`$]\}$

{ph}`then` {ph}`P`$[${ph}`x`$]$
```


Examples
--------

```{rewrite-rule}
assume $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$

assume $x^n = 1$ for some $n \in \mathbb{N}$
```
