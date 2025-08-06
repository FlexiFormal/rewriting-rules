Rule 5.16: Subset Comprehension Term Reduction
==============================================


```{rewrite-rule}
{ph}`then` $\{y \mid \varphi[y]\} \subseteq X$

{ph}`then` $y \in X$ for all $y$ with $\varphi[y]$
```


Examples
--------

```{rewrite-rule}
assume $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\} \subseteq X$

assume $z \in X$ for all $z$ with $z^n = 1$ for some $n \in \mathbb{N}$
```
