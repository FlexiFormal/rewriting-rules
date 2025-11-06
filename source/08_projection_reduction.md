Section 8: Projection Reduction
===============================

Let $\pi_i$ denote the $i$-th projection from a Cartesian product
$A_1 \times \dots \times A_n$ to its $i$-th component $A_i$.
Applying $\beta$-reduction to such a projection applied to an
element of $A_i \times \dots \times A_n$ yields the following
rewrite rule:

```{rewrite-rule}
a_1, ..., a_n : <Term> = "$\sin(x)$", "$\cos(x + 1)$"

i : <Term> = "$1 + 1$"

|- $:i: = j$

"$\pi_{:i:}(\langle :a_1:, \dots, :a_n: \rangle)$"

--- Projection Reduction

":a_j:"
```


Examples
--------

```{rewrite-rule}
|- $1 + 1 = 2$

"$\pi_{1 + 1}(\langle \sin(x), \cos(x + 1) \rangle)$"

"$\cos(x + 1)$"
```
