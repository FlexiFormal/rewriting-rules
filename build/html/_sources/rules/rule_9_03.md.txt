Rule 9.3: Family Structure Expansion
====================================


```{rewrite-rule}
{ph}`noun` : {cat}`noun` = {nl}`edge`

{ph}`t` : {cat}`Term` = {nl}`$\langle v, v' \rangle$`

{ph}`x` : {cat}`Var` = {nl}`$e$`

{ph}`i` : {cat}`Var` = {nl}`$i$`

{ph}`I` : {cat}`Term` = {nl}`$I$`

{ph}`noun` := A {ph}`noun` is a (structure | pair | triple | ...) {ph}`t` (with ... | of ... | where ...)

family $({ph}`x`_{{ph}`i`})_{{ph}`i` \in {ph}`I`}$ of {ph}`noun`

family $({ph}`x`_{{ph}`i`})_{{ph}`i` \in {ph}`I`}$ of {ph}`noun` ${ph}`x`_{{ph}`i`} :=$ ${ph}`t`_{{ph}`i`}$
```


Examples
--------

```{rewrite-rule}
edge := An edge is a pair $\langle v, v' \rangle$ of nodes $v, v'$.

family $(e_i)_{i \in I}$ of edges

family $(e_i)_{i \in I}$ of edges $e_i := \langle v_i, v'_i \rangle$
```
