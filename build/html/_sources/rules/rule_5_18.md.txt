Rule 5.18: Relation Guard Reduction
===================================


```{rewrite-rule}
{ph}`R`[{ph}`a`] : {cat}`Guarded Identifier` = {nl}`$1 \leq {ph}`a` \leq n$`

{ph}`y` : {cat}`Var` = {nl}`$y$`

{ph}`P`[{ph}`b`] : {cat}`Pred` = {nl}`$1/{ph}`b` < \varepsilon$`

$\{{ph}`R`[{ph}`y`] \mid {ph}`P`[{ph}`y`]\}$

$\{{ph}`y` \mid {ph}`R`[{ph}`y`] \text{ and } {ph}`P`[{ph}`y`]\}$
```


Examples
--------

```{rewrite-rule}
$\{1 \leq i \leq n \mid 1/i < \varepsilon\}$

$\{i \mid 1 \leq i \leq n \text{ and } 1/i < \varepsilon\}$
```
