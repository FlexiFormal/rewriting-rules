Rule 5.19: Relation-Term Guard Reduction
========================================


```{rewrite-rule}
R[a] : <Guarded Identifier> = "$:a: \in \mathbb{N} \times \mathbb{N}$"

t[b_1, ..., b_n] : <Term> = "$\langle :b_1:, :b_2: \rangle$"

y : <Var> = "$y$"

P[c_1, ..., c_n] : <Pred> = ":c_1: is a prime divisor of :c_2:"

z : <Var> = "$z$"

"$\{:R:[:t:[:y_1:, \dots, :y_n:]] \mid :P:[:y_1:, \dots, :y_n:]\}$"

"$\{:z: \mid \text{there exist } :y_1:, \dots, :y_n: \text{ such that } :z: = :t:[:y_1:, \dots, :y_n:] \text{ and } :R:[:z:] \text{ and } :P:[:y_1:, \dots, :y_n:]\}$"
```


Examples
--------

```{rewrite-rule}
"$\{\langle p,n \rangle \in \mathbb{N} \times \mathbb{N} \mid p \text{ is a prime divisor of } n\}$"

"$\{z \mid \text{there exist } p,n \text{ such that } z = \langle p,n \rangle \text{ and } z \in \mathbb{N} \times \mathbb{N} \text{ and } p \text{ is a prime divisor of } n\}$"
```
