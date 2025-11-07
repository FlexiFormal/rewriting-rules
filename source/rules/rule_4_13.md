Rule 4.13: "Either"-VP Aggregation
==================================


```{rewrite-rule}
VP_1, ..., VP_n : <VP> = "contain $y$", "include $z$"

t : <Term> = "$x$"

":t: :VP_1: or ... or :t: :VP_n: @(and | but)@ :t: does not both :VP_1: and ... and :VP_n:"

--- "Either"-VP Aggregation

":t: either :VP_1: or ... or :VP_n:"
```

Examples
--------

```{rewrite-rule}
"$x$ contains $y$ or $x$ includes $z$ but $x$ does not both contain $y$ and include $z$"

--- "Either"-VP Aggregation

"$x$ either contains $y$ or includes $z$"
```


