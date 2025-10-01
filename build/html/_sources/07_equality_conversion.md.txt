Section 7: Equality Conversion
==============================

Provalby equal expressions can be replaced by each other:

```{rewrite-rule}
{ph}`A` : {cat}`Term` = {nl}`$\bigcup_{n \in \mathbb{N}} R^n$`

{ph}`B` : {cat}`Term` = {nl}`$R^+$`

$\vdash {ph}`A` = {ph}`B`$

{ph}`A`

{ph}`B`
```


Examples
--------

Let $R^+$ denote the transitive closure of a relation $R$.

```{rewrite-rule}
$\vdash \bigcup_{n \in \mathbb{N}} R^n = R^+$

$\bigcup_{n \in \mathbb{N}} R^n$

$R^+$
```
