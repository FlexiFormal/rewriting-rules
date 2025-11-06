Rule 9.3: Family Structure Expansion
====================================


```{rewrite-rule}
noun : <noun> = "edge"

t : <Term> = "$\langle v, v' \rangle$"

x : <Var> = "$e$"

i : <Var> = "$i$"

I : <Term> = "$I$"

:noun: := "A :noun: is a @'structure' | 'pair' | 'triple' | ...@ :t: @'with' | 'of' | 'where'@ ..."

"family $(:x:_{:i:})_{:i: \in :I:}$ of :noun:"

"family $(:x:_{:i:})_{:i: \in :I:}$ of :noun: $:x:_{:i:} :=$ $:t:_{:i:}$"
```


Examples
--------

```{rewrite-rule}
"edge := "An edge is a pair $\langle v, v' \rangle$ of nodes $v, v'$.""

"family $(e_i)_{i \in I}$ of edges"

"family $(e_i)_{i \in I}$ of edges $e_i := \langle v_i, v'_i \rangle$"
```
