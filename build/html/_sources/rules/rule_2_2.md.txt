Rule 2.2: Verb Variable Reduction
=================================


```{rewrite-rule}
NP : <NP> = "a prime number"

t : <Term> = "$p$"

VP : <VP> = "divides $n$"

":NP: :t: such that :t: :VP:"

":NP: :t: that :VP:"
```


Examples
--------

```{rewrite-rule}
"a prime number $p$ such that $p$ divides $n$"

"a prime number $p$ that divides $n$"
```
