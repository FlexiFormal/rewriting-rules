Rule 5.17: Term Guard Reduction
===============================


```{rewrite-rule}
$\{t[y_1,\dots,y_n] \mid \varphi[y_1,\dots,y_n]\}$

$\{z \mid \text{there exist } y_1,\dots,y_n \text{ such that } z = t[y_1,\dots,y_n] \text{ and } \varphi[y_1,\dots,y_n]\}$
```


Examples
--------

```{rewrite-rule}
$\{n^2 \mid n \in \mathbb{N}\}$

$\{z \mid \text{there exist an } n \text{ such that } z = n^2 \text{ and } n \in \mathbb{N}\}$
```
