Guarded Identifiers
===================


```{warning}
This needs work to get the terminology straight.

Is $R[x]$ a guarded identifier only if it is used in the place where $x$ is
being declared?
Or also in other places if it can be used for the declaration?
Etc.
(the places where the term is used have to be updated accordingly as well)
```

A guarded identifier is a formula that grammatically acts as an identifier
but contains restrictions on the domain.

Example:

```{rewrite-rule}
For every $x \in \mathbb{R}$ ...
```

This can be treated as a short-form for:

```{rewrite-rule}
For every $x$ such that $x \in \mathbb{R}$ ...
```

We typically write this as $R[x]$, where $R$
is the formula and $x$ is the relevant identifier.

Some rewriting rules use guarded identifiers for simplification/contraction.
Identifying if a formula can act as a guarded identifier is not trivial.
For example, $k < x < n$ can be a guarded identifier if $k$ and $n$ are not free.





