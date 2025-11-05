Rule 5.3: "Let"-NP Comprehension Term Reduction
===============================================


```{rewrite-rule}
{ph}`let` : {cat}`let` = {nl}`let`

{ph}`NP` : {cat}`NP` = {nl}`complex number`

{ph}`x` : {cat}`Var` = {nl}`$x$`

{ph}`y` : {cat}`Var` = {nl}`$z$`

{ph}`P`[{ph}`a`] : {cat}`Pred` = {nl}`${ph}`a`^n = 1 \text{ for some } n \in \mathbb{N}$`

{ph}`let` ${ph}`x` \in \{{ph}`y` \mid {ph}`P`[{ph}`y`]\}$ be a {ph}`NP`

{ph}`let` {ph}`x` be a {ph}`NP` such that ${ph}`P`[{ph}`x`]$
```


Examples
--------

```{rewrite-rule}
let $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ be a complex number

let $x$ be a complex number such that $x^n = 1$ for some $n \in \mathbb{N}$
```
