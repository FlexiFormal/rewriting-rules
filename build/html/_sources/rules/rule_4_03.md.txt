Rule 4.3: "And"-VP Aggregation
==============================


```{rewrite-rule}
VP_1, ..., VP_n : <VP> = "intersects with $y$", "contains $z$"

t : <Term> = "$x$"

":t: :VP_1: and ... and :t: :VP_n:"

--- "And"-VP Aggregation

":t: :VP_1: and ... and :VP_n:"
```

Examples
--------

```{rewrite-rule}
"$x$ intersects with $y$ and $x$ contains $z$"

--- "And"-VP Aggregation

"$x$ intersects with $y$ and contains $z$"
```


