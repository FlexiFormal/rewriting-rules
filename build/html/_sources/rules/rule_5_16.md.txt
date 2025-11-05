Rule 5.16: Subset Comprehension Term Reduction
==============================================


```{rewrite-rule}
{ph}`then` : {cat}`then` = {nl}`assume`

{ph}`y` : {cat}`Var` = {nl}`$z$`

{ph}`X` : {cat}`Var` = {nl}`$X$`

{ph}`P`[{ph}`a`] : {cat}`Pred` = {nl}`${ph}`a`^n = 1 \text{ for some } n \in \mathbb{N}$`

{ph}`then` $\{{ph}`y` \mid {ph}`P`[{ph}`y`]\} \subseteq {ph}`X`$

{ph}`then` ${ph}`y` \in {ph}`X`$ for all {ph}`y` with ${ph}`P`[{ph}`y`]$
```


Examples
--------

```{rewrite-rule}
assume $\{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\} \subseteq X$

assume $z \in X$ for all $z$ with $z^n = 1$ for some $n \in \mathbb{N}$
```
