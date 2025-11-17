Rule 4.14: "Neither"-NP Aggregation
===================================


```{rewrite-rule}
Det_1, ..., Det_n : a | no = "a", "no"

NP_1, ..., NP_n : <NP> = "prime", "even number"

t : <Term> = "$x$"

":t: is not :Det_1: :NP_1: and ... and :t: is not :Det_n: :NP_n:"

--- "Neither"-NP Aggregation

":t: is neither :Det_1: :NP_1: nor ... nor :Det_n: :NP_n:"
```

Examples
--------

```{rewrite-rule}
"$x$ is not a prime and $x$ is no even number"

--- "Neither"-NP Aggregation

"$x$ is neither a prime nor no even number"
```


