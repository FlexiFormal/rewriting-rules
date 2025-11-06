Rule 4.12: "Neither"-VP Aggregation
===================================


```{rewrite-rule}
VP_1, ..., VP_n : <VP> = "contain $y$", "include $z$"

t : <Term> = "$x$"

":t: does not :VP_1: and ... and :t: does not :VP_n:"

--- "Neither"-VP Aggregation

":t: does neither :VP_1: nor ... nor :VP_n:"
```

Examples
--------

```{rewrite-rule}
"$x$ does not contain $y$ and $x$ does not include $z$"

"$x$ does neither contain $y$ nor include $z$"
```


