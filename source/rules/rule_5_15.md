Rule 5.15: Determiner-PP Comprehension Term Reduction
=====================================================


```{rewrite-rule}
{ph}`Det` [{ph}`NP` | {ph}`AP`] $x \in \{y \mid \varphi[y]\}$ with {ph}`PP`

{ph}`Det` [{ph}`NP` | {ph}`AP`] $x$ with $\varphi[x]$ and {ph}`PP`
```


Examples
--------

```{rewrite-rule}
all $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ with $\Re(x) > 0$

all $x$ with $x^n = 1$ for some $n \in \mathbb{N}$ and $\Re(x) > 0$
```

```{rewrite-rule}
those complex numbers $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ with $\Re(x) > 0$

those complex numbers $x$ with $x^n = 1$ for some $n \in \mathbb{N}$ and $\Re(x) > 0$
```

```{rewrite-rule}
certain imaginary $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ with $\Re(x) > 0$

certain imaginary $x$ with $x^n = 1$ for some $n \in \mathbb{N}$ and $\Re(x) > 0$
```
