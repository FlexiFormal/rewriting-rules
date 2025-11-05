Rule 9.1: Variable Structure Expansion
======================================


```{rewrite-rule}
{ph}`noun` : {cat}`noun` = {nl}`finite automaton`

{ph}`t` : {cat}`Term` = {nl}`$\langle Q, \Sigma, \delta, q_0, F \rangle$`

{ph}`x` : {cat}`Var` = {nl}`$\mathcal{A}$`

{ph}`noun` := A {ph}`noun` is a (structure | pair | triple | ...) {ph}`t` (with ... | of ... | where ...)

{ph}`noun` {ph}`x`

{ph}`noun` ${ph}`x` :=$ {ph}`t`
```


Examples
--------

```{rewrite-rule}
finite automaton := A finite automaton is a structure $\langle Q, \Sigma, \delta, q_0, F \rangle$, where $Q$ is a set whose elements are called states, and ...

finite automaton $\mathcal{A}$

finite automaton $\mathcal{A} := \langle Q, \Sigma, \delta, q_0, F \rangle$
```
