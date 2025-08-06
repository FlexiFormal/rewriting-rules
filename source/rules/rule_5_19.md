Rule 5.19: Relation-Term Guard Reduction
========================================


```{rewrite-rule}
$\{R[t[y_1,\dots,y_n]] \mid \varphi[y_1,\dots,y_n]\}$

$\{z \mid \text{there exist } y_1,\dots,y_n \text{ such that } z = t[y_1,\dots,y_n] \text{ and } R[z] \text{ and } \varphi[y_1,\dots,y_n]\}$
```


Examples
--------

```{rewrite-rule}
$\{\langle p,n \rangle \in \mathbb{N} \times \mathbb{N} \mid p \text{ is a prime divisor of } n\}$

$\{z \mid \text{there exist } p,n \text{ such that } z = \langle p,n \rangle \text{ and } z \in \mathbb{N} \times \mathbb{N} \text{ and } p \text{ is a prime divisor of } n\}$
```
