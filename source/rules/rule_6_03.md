Rule 6.3: Singleton Conversion
==============================


```{rewrite-rule}
a : <Term> = "$2$"

A : <Term> = "$\{p \mid p \text{ is an even prime}\}$"

|- $|:A:| = 1$

|- $:a: \in :A:$

":A:"

--- Singleton Conversion

"$\{:a:\}$"
```


````{note}
Note that this is just a special case of rule [Rule 7](07_equality_conversion.md).
````

Examples
--------

```{rewrite-rule}
|- $|\{p \mid p \text{ is an even prime}\}| = 1$

|- $2 \in \{p \mid p \text{ is an even prime}\}$

"$\{p \mid p \text{ is an even prime}\}$"

--- Singleton Conversion

"$\{2\}$"
```
