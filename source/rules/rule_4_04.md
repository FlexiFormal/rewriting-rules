Rule 4.4: "Or"-VP Aggregation
=============================


```{rewrite-rule}
VP_1, ..., VP_n : <VP>= "intersects with $y$", "contains $z$"

t : <Term> = "$x$"

":t: :VP_1: or ... or :t: :VP_n:"

--- "Or"-VP Aggregation

":t: :VP_1: or ... or :VP_n:"
```

Examples
--------

```{rewrite-rule}
"$x$ intersects with $y$ or $x$ contains $z$"

"$x$ intersects with $y$ or contains $z$"
```


