Rule 4.9: "Or"-NP Aggregation
=============================


```{rewrite-rule}
Det_1, ..., Det_n : a | no = "a", "a"

NP_1, ..., NP_n : <NP> = "proper class", "set"

t : <Term> = "$x$"

":t: is :Det_1: :NP_1: or ... or :t: is :Det_n: :NP_n:"

--- "Or"-NP Aggregation

":t: is :Det_1: :NP_1: or ... or :Det_n: :NP_n:"
```

Examples
--------

```{rewrite-rule}
"$x$ is a proper class or $x$ is a set"

"$x$ a proper class or a set"
```


