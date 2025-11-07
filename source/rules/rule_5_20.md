Rule 5.20: Element-NP Guard Reduction
=====================================


```{rewrite-rule}
NP : <NP> = "complex number"

x_opt : [<Var>] = "$x$"

y : <Var> = "$y$"

"element :x_opt: of $\{:y: \mid :y: \text{ is a } :NP:\}$"

--- Element-NP Guard Reduction

":NP: :x_opt:"
```


Examples
--------

```{rewrite-rule}
"element $x$ of $\{z \mid z \text{ is a complex number}\}$"

--- Element-NP Guard Reduction

"complex number $x$"
```
