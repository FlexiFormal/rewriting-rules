Rule 5.21: Subset-NP Guard Reduction
=====================================


```{rewrite-rule}
NP : <NP> = "complex number"

x_opt : [<Var>] = "$x$"

y : <Var> = "$y$"

"subset :x_opt: of $\{:y: \mid :y: \text{ is a } :NP:\}$"

--- Subset-NP Guard Reduction

"set :x_opt: of :NP:"
```


Examples
--------

```{rewrite-rule}
"subsets of $\{z \mid z \text{ is a complex number}\}$"

--- Subset-NP Guard Reduction

"sets of complex numbers"
```
