Rule 5.20: Element-NP Guard Reduction
=====================================


```{rewrite-rule}
{ph}`NP` : {cat}`NP` = {nl}`complex number`

{ph}`opt_x` : [{cat}`Var`] = {nl}`$x$`

{ph}`y` : {cat}`Var` = {nl}`$y$`

element {ph}`opt_x` of $\{{ph}`y` \mid {ph}`y` \text{ is a {ph}`NP`}\}$

{ph}`NP` {ph}`opt_x`
```


Examples
--------

```{rewrite-rule}
element $x$ of $\{z \mid z \text{ is a complex number}\}$

complex number $x$
```
