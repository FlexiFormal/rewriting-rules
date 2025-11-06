Rule 4.5: Tuple Aggregation
===========================


```{rewrite-rule}
t_1, ..., t_n : <Term> = "$n$", "$\sqrt{n}$"

T_1, ..., T_n : <Term> = "$\mathbb{N}$", "$\mathbb{N}$"

"$:t_1: \in :T_1:$ and ... and $:t_n: \in :T_n:$"

--- Tuple Aggregation

"$\langle :t_1:, \dots, :t_n: \rangle \in :T_1: \times \dots \times :T_n:$"
```

Examples
--------

```{rewrite-rule}
"$n \in \mathbb{N}$ and $\sqrt{n} \in \mathbb{N}$"

"$\langle n, \sqrt{n} \rangle \in \mathbb{N} \times \mathbb{N}$"
```
