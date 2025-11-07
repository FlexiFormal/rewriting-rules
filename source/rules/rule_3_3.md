Rule 3.3: Tuple Determiner Reduction
====================================


```{rewrite-rule}
Det : <Det> = "any"

NP_opt : [<NP>] = ""

t_1, ..., t_n : <Term> = "$x$", "$y$"

T_1, ..., T_n : <Term> = "$\mathbb{R}$", "$\mathbb{R}$"

":Det: :NP_opt: $:t_1:, \ldots, :t_n:$ with $\langle :t_1:, \ldots, :t_n: \rangle \in :T_1: \times \ldots \times :T_n:$"

--- Tuple Determiner Reduction

":Det: $\langle :t_1:, \ldots, :t_n: \rangle \in :T_1: \times \ldots \times :T_n:$"
```

````{note}
This could also be considered a special case of
a generalized form of [Rule 3.2](rule_3_2.md):

```{rewrite-rule}
Det : <Det> = "those" 

NP_opt : [<NP>] = "states"

t_1, ..., t_n : <Term> = "$p$", "$q$"

R[x_1, ..., x_n] : <guarded identifier> = ":x_1:, :x_2: $\in Q \setminus F$"

":Det: :NP_opt: $:t_1:, \ldots, :t_n:$ with :R:[:t_1:, ..., :t_n:]"

---

":Det: :NP_opt: :R:[:t_1:, ..., :t_n:]"
```
````

Example:

```{rewrite-rule}
"any $x, y$ with $\langle x, y \rangle \in \mathbb{R} \times \mathbb{R}$"

--- Tuple Determiner Reduction

"any $\langle x, y \rangle \in \mathbb{R} \times \mathbb{R}$"
```

```{rewrite-rule}
"those states $p, q$ with $p, q \in Q \setminus F$"

--- Tuple Determiner Reduction

"those states $q \in Q \setminus F$"
```


