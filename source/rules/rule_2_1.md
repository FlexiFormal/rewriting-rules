Rule 2.1: Adjective Variable Reduction
======================================


```{rewrite-rule}
NP : <NP> = "an input symbol"

t : <Term> = "$a$"

AP : <AP> = "applicable in $q$"

":NP: :t: @(such that :t: is | with :t: being)@ :AP:"

--- Adjective Variable Reduction

":NP: :t: that is :AP:"
```


Examples
--------

```{rewrite-rule}
"an input symbol $a$ such that $a$ is applicable in $q$"

--- Adjective Variable Reduction

"an input symbol $a$ that is applicable in $q$"
```
