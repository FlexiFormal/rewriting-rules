Section 7: Equality Conversion
==============================

Provalby equal expressions can be replaced by each other:

```{rewrite-rule}
A : <Term> = "$\bigcup_{n \in \mathbb{N}} R^n$"

B : <Term> = "$R^+$"

|- $:A: = :B:$

":A:"

--- Equality Conversion

":B:"
```


Examples
--------

Let $R^+$ denote the transitive closure of a relation $R$.

```{rewrite-rule}
|- $\bigcup_{n \in \mathbb{N}} R^n = R^+$

"$\bigcup_{n \in \mathbb{N}} R^n$"

--- Equality Conversion

"$R^+$"
```
