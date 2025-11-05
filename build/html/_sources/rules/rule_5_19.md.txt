Rule 5.19: Relation-Term Guard Reduction
========================================


```{rewrite-rule}
{ph}`R`[{ph}`a`] : {cat}`Guarded Identifier` = {nl}`${ph}`a` \in \mathbb{N} \times \mathbb{N}$`

{ph}`t`[{ph}`b_1`, ..., {ph}`b_n`] : {cat}`Term` = {nl}`$\langle {ph}`b_1`, {ph}`b_2` \rangle$`

{ph}`y` : {cat}`Var` = {nl}`$y$`

{ph}`P`[{ph}`c_1`, ..., {ph}`c_n`] : {cat}`Pred` = {nl}`{ph}`c_1` is a prime divisor of {ph}`c_2``

{ph}`z` : {cat}`Var` = {nl}`$z$`

$\{{ph}`R`[{ph}`t`[{ph}`y_1`, \dots, {ph}`y_n`]] \mid {ph}`P`[{ph}`y_1`, \dots, {ph}`y_n`]\}$

$\{{ph}`z` \mid \text{there exist } {ph}`y_1`, \dots, {ph}`y_n` \text{ such that } {ph}`z` = {ph}`t`[{ph}`y_1`, \dots, {ph}`y_n`] \text{ and } {ph}`R`[{ph}`z`] \text{ and } {ph}`P`[{ph}`y_1`, \dots, {ph}`y_n`]\}$
```


Examples
--------

```{rewrite-rule}
$\{\langle p,n \rangle \in \mathbb{N} \times \mathbb{N} \mid p \text{ is a prime divisor of } n\}$

$\{z \mid \text{there exist } p,n \text{ such that } z = \langle p,n \rangle \text{ and } z \in \mathbb{N} \times \mathbb{N} \text{ and } p \text{ is a prime divisor of } n\}$
```
