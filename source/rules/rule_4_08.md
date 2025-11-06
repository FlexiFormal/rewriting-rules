Rule 4.8: "And"-NP Aggregation
==============================


```{rewrite-rule}
Det_1, ..., Det_n : a | no = "a", "no"

NP_1, ..., NP_n : <NP> = "prime number", "even number"

t : <Term> = "$x$"

":t: is :Det_1: :NP_1: and ... and :t: is :Det_n: :NP_n:"

":t: is :Det_1: :NP_1: and ... and :Det_n: :NP_n:"
```

Examples
--------

```{rewrite-rule}
"$x$ is a prime number and $x$ no even number"

"$x$ a prime number and no even number"
```


