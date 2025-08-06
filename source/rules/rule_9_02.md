Rule 9.2: Sequence Structure Expansion
======================================


```{rewrite-rule}
sequence $x_1, \dots, x_n$ of {ph}`noun`

{ph}`noun` $:=$ A {ph}`noun` is a (structure | pair | triple | ...) {ph}`symbolic term` (with ... | of ... | where ...)

sequence $x_1, \dots, x_n$ of {ph}`noun` $x_i :=$ {ph}`symbolic term`$_i$
```


Examples
--------

```{rewrite-rule}
sequence $t_1, \dots, t_n$ of transitions

transition $:=$ A transition is a triple $\langle q, c, q' \rangle$ with $q' \in \delta(q,c)$.

sequence $t_1, \dots, t_n$ of transitions $t_i := \langle q_i, c_i, q'_i \rangle$
```
