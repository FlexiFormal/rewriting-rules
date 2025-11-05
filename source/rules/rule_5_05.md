Rule 5.5: "Let"-PP Comprehension Term Reduction
===============================================


```{rewrite-rule}
{ph}`let` : {cat}`let` = {nl}`let`

{ph}`Prop` : {cat}`Prop` = {nl}`$\Im(x) > 0$`

{ph}`x` : {cat}`Var` = {nl}`$x$`

{ph}`y` : {cat}`Var` = {nl}`$z$`

{ph}`P`[{ph}`a`] : {cat}`Pred` = {nl}`${ph}`a`^n = 1 \text{ for some } n \in \mathbb{N}$`

{ph}`let` ${ph}`x` \in \{{ph}`y` \mid {ph}`P`[{ph}`y`]\}$ with {ph}`Prop`

{ph}`let` {ph}`x` be an element such that ${ph}`P`[{ph}`x`]$ and {ph}`Prop`
```


Examples
--------

```{rewrite-rule}
let $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ with $\Im(x) > 0$

let $x$ be an element such that $x^n = 1$ for some $n \in \mathbb{N}$ and $\Im(x) > 0$
```
