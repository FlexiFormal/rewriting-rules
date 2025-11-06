Rule 4.15: "Either"-NP Aggregation
==================================


```{rewrite-rule}
Det_1, ..., Det_n : a | no = "a", "no"

NP_1, ..., NP_n : <NP> = "prime", "even number"

t : <Term> = "$x$"

":t: is :Det_1: :NP_1: or ... or :t: is :Det_n: :NP_n: @and | but@ :t: is not both :Det_1: :NP_1: and ... and :Det_n: :NP_n:"

--- "Either"-NP Aggregation

":t: is either :Det_1: :NP_1: or ... or :Det_n: :NP_n:"
```

Examples
--------

```{rewrite-rule}
"$x$ is a prime or $x$ is no even number but $x$ is not both a prime and no even number"

"$x$ is either a prime nor no even number"
```


