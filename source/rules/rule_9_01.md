Rule 9.1: Variable Structure Expansion
======================================


```{rewrite-rule}
noun : <noun> = "finite automaton"

t : <Term> = "$\langle Q, \Sigma, \delta, q_0, F \rangle$"

x : <Var> = "$\mathcal{A}$"

:noun: := "A :noun: is a @'structure' | 'pair' | 'triple' | ...@ :t: @'with' | 'of' | 'where'@ ..."

":noun: :x:"

":noun: $:x: := :t:$"
```


Examples
--------

```{rewrite-rule}
"finite automaton := "A finite automaton is a structure $\langle Q, \Sigma, \delta, q_0, F \rangle$, where $Q$ is a set whose elements are called states, and ...""

"finite automaton $\mathcal{A}$"

"finite automaton $\mathcal{A} := \langle Q, \Sigma, \delta, q_0, F \rangle$"
```
