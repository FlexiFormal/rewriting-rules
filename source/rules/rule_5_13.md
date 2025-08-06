Rule 5.13: Determiner-AP Comprehension Term Reduction
=====================================================


```{rewrite-rule}
{ph}`Det` [{ph}`NP` | {ph}`AP`] $x \in \{y \mid \varphi[y]\}$ that is {ph}`AP`

{ph}`Det` {ph}`AP` [{ph}`NP` | {ph}`AP`] $x$ with $\varphi[x]$
```


Examples
--------

```{rewrite-rule}
all $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that are imaginary

all imaginary $x$ with $x^n = 1$ for some $n \in \mathbb{N}$
```

```{rewrite-rule}
those complex numbers $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that are imaginary

those imaginary complex numbers $x$ with $x^n = 1$ for some $n \in \mathbb{N}$
```

```{rewrite-rule}
certain real $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that are positive

certain positive real $x$ with $x^n = 1$ for some $n \in \mathbb{N}$
```
