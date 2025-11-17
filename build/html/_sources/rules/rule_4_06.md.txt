Rule 4.6: "And"-Element Aggregation
===================================


```{rewrite-rule}
t : <Term> = "$n$"

T_1, ..., T_n : <Term> = "$\mathbb{Z}$", "$\{ x \in \mathbb{R} \mid x^3 \geq x^2 \}$"

"$:t: \in :T_1:$ and ... and $:t: \in :T_n:$"

--- "And"-Element Aggregation

"$:t: \in :T_1: \cap \dots \cap :T_n:$"
```

Examples
--------

```{rewrite-rule}
"$n \in \mathbb{Z}$ and $n \in \{ x \in \mathbb{R} \mid x^3 \geq x^2 \}$"

--- "And"-Element Aggregation

"$n \in \mathbb{Z} \cap \{ x \in \mathbb{R} \mid x^3 \geq x^2 \}$"
```
