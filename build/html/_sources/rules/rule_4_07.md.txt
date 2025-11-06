Rule 4.7: "Or"-Element Aggregation
==================================


```{rewrite-rule}
t : <Term> = "$n$"

T_1, ..., T_n : <Term> = "$\mathbb{Z}$", "$\{ x \in \mathbb{R} \mid x^3 \geq x^2 \}$"

"$:t: \in :T_1:$ or ... or $:t: \in :T_n:$"

--- "Or"-Element Aggregation

"$:t: \in :T_1: \cup \dots \cup :T_n:$"
```

Examples
--------

```{rewrite-rule}
"$n \in \mathbb{Z}$ or $n \in \{ x \in \mathbb{R} \mid x^3 \geq x^2 \}$"

"$n \in \mathbb{Z} \cup \{ x \in \mathbb{R} \mid x^3 \geq x^2 \}$"
```
