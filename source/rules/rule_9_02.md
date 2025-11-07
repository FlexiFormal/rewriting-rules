Rule 9.2: Sequence Structure Expansion
======================================


```{rewrite-rule}
noun : <noun> = "transition"

t : <symbolic term> = "$\langle q, c, q' \rangle$"

x_1, ..., x_n : <Var> = "$t_1$", $\dots$, "$t_n$"

i : <Var> = "$i$"

:noun: := "A :noun: is a @'structure' | 'pair' | 'triple' | ...@ :t: @'with' | 'of' | 'where'@ ..."

"sequence $:x_1:, \dots, :x_n:$ of :noun:"

--- Sequence Structure Expansion

"sequence $:x_1:, \dots, :x_n:$ of :noun: $:x:_{:i:} := :t:_{:i:}$"
```


Examples
--------

```{rewrite-rule}
"transition := "A transition is a triple $\langle q, c, q' \rangle$ with $q' \in \delta(q,c)$""

"sequence $t_1, \dots, t_n$ of transitions"

--- Sequence Structure Expansion

"sequence $t_1, \dots, t_n$ of transitions $t_i := \langle q_i, c_i, q'_i \rangle$"
```
