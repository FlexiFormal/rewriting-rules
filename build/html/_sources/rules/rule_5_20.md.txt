Rule 5.20: Element-NP Guard Reduction
=====================================


```{rewrite-rule}
NP : <NP> = "complex number"

opt_x : [<Var>] = "$x$"

y : <Var> = "$y$"

"element :opt_x: of $\{:y: \mid :y: \text{ is a } :NP:\}$"

":NP: :opt_x:"
```


Examples
--------

```{rewrite-rule}
"element $x$ of $\{z \mid z \text{ is a complex number}\}$"

"complex number $x$"
```
