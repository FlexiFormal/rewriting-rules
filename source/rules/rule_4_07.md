Rule 4.7: "Or"-Element Aggregation
==================================


```{rewrite-rule}
{ph}`t` : {cat}`Term` = {nl}`$n$`

{ph}`T_1`, $\dots$, {ph}`T_n` : {cat}`Term` = {nl}`$\mathbb{Z}$`, {nl}`$\{ x \in \mathbb{R} \mid x^3 \geq x^2 \}$`

{ph}`t` $\in$ {ph}`T_1` or ... or {ph}`t` $\in$ {ph}`T_n`

{ph}`t` $\in$ {ph}`T_1` $\cup \dots \cup$ {ph}`T_n`
```

Examples
--------

```{rewrite-rule}
$n \in \mathbb{Z}$ or $n \in \{ x \in \mathbb{R} \mid x^3 \geq x^2 \}$

$n \in \mathbb{Z} \cup \{ x \in \mathbb{R} \mid x^3 \geq x^2 \}$
```
