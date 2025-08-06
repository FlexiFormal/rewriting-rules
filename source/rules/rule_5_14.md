Rule 5.14: Determiner-VP Comprehension Term Reduction
=====================================================


```{rewrite-rule}
{ph}`Det` [{ph}`NP` | {ph}`AP`] $x \in \{y \mid \varphi[y]\}$ that {ph}`VP`

{ph}`Det` [{ph}`NP` | {ph}`AP`] $x$ that {ph}`VP` with $\varphi[x]$
```


Examples
--------

```{rewrite-rule}
all $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that solve the equation $E$

all $x$ that solve the equation $E$ with $x^n = 1$ for some $n \in \mathbb{N}$
```

```{rewrite-rule}
those complex numbers $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that solve the equation $E$

those complex numbers $x$ that solve the equation $E$ with $x^n = 1$ for some $n \in \mathbb{N}$
```

```{rewrite-rule}
certain imaginary $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that solve the equation $E$

certain imaginary $x$ that solve the equation $E$ with $x^n = 1$ for some $n \in \mathbb{N}$
```
