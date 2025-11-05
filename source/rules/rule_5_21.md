Rule 5.21: Subset-NP Guard Reduction
=====================================


```{rewrite-rule}
{ph}`NP` : {cat}`NP` = {nl}`complex number`

{ph}`opt_x` : [{cat}`Var`] = {nl}`$x$`

{ph}`y` : {cat}`Var` = {nl}`$y$`

subset {ph}`opt_x` of $\{{ph}`y` \mid {ph}`y` \text{ is a }{ph}`NP`\}$

set {ph}`opt_x` of {ph}`NP`
```


Examples
--------

```{rewrite-rule}
subsets of $\{z \mid z \text{ is a complex number}\}$

sets of complex numbers
```
