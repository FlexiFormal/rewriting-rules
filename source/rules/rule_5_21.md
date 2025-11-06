Rule 5.21: Subset-NP Guard Reduction
=====================================


```{rewrite-rule}
NP : <NP> = "complex number"

opt_x : [<Var>] = "$x$"

y : <Var> = "$y$"

"subset :opt_x: of $\{:y: \mid :y: \text{ is a } :NP:\}$"

"set :opt_x: of :NP:"
```


Examples
--------

```{rewrite-rule}
"subsets of $\{z \mid z \text{ is a complex number}\}$"

"sets of complex numbers"
```
