Rule 5.1: "Then" Comprehension Term Reduction
=============================================


```{rewrite-rule}
{ph}`then` $x \in \{y \mid \varphi[y]\}$

{ph}`then` $\varphi[x]$
```


Examples
--------

```{rewrite-rule}
assume $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$

assume $x^n = 1$ for some $n \in \mathbb{N}$
```
