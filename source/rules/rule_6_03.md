Rule 6.3: Singleton Conversion
==============================


```{rewrite-rule}
a : <Term> = "$2$"

A : <Term> = "$\{p \mid p \text{ is an even prime}\}$"

|- $|:A:| = 1$

|- $:a: \in :A:$

":A:"

"$\{:a:\}$"
```


Examples
--------

```{rewrite-rule}
|- $|\{p \mid p \text{ is an even prime}\}| = 1$

|- $2 \in \{p \mid p \text{ is an even prime}\}$

"$\{p \mid p \text{ is an even prime}\}$"

"$\{2\}$"
```
