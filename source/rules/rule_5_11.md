Rule 5.11: Determiner Comprehension Term Reduction
==================================================


```{rewrite-rule}
{ph}`Det` [{ph}`NP` | {ph}`AP`] $x \in \{y \mid \varphi[y]\}$

{ph}`Det` [{ph}`NP` | {ph}`AP`] $x$ with $\varphi[x]$
```


Examples
--------

```{rewrite-rule}
all $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$

all $x$ with $x^n = 1$ for some $n \in \mathbb{N}$
```

```{rewrite-rule}
those complex numbers $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$

those complex numbers $x$ with $x^n = 1$ for some $n \in \mathbb{N}$
```

```{rewrite-rule}
certain imaginary $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$

certain imaginary $x$ with $x^n = 1$ for some $n \in \mathbb{N}$
```
