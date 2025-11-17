Rule 4.11: "Either"-AP Aggregation
==================================


```{rewrite-rule}
AP_1, ..., AP_n : <AP> = "odd", "prime"

t : <Term> = "$x$"

":t: is :AP_1: or ... or :t: is :AP_n: @(and | but)@ :t: is not both :AP_1: and ... and :AP_n:"

--- "Either"-AP Aggregation

":t: is either :AP_1: or ... or :AP_n:"
```

Examples
--------

```{rewrite-rule}
"$x$ is odd or $x$ is prime but $x$ is not both odd or prime"

--- "Either"-AP Aggregation

"$x$ is either odd or prime"
```


