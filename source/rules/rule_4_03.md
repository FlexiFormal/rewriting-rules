Rule 4.3: "And"-VP Aggregation
==============================


```{rewrite-rule}
VP_1, ..., VP_n : <VP> = "intersects with $y$", "contains $z$"

t : <Term> = "$x$"

":t: :VP_1: and ... and :t: :VP_n:"

":t: :VP_1: and ... and :VP_n:"
```

Examples
--------

```{rewrite-rule}
"$x$ intersects with $y$ and $x$ contains $z$"

"$x$ intersects with $y$ and contains $z$"
```


