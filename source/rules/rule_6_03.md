Rule 6.3: Singleton Conversion
==============================


```{rewrite-rule}
{ph}`a` : {cat}`Term` = {nl}`$2$`

{ph}`A` : {cat}`Term` = {nl}`$\{p \mid p \text{ is an even prime}\}$`

$\vdash |{ph}`A`| = 1$

$\vdash {ph}`a` \in {ph}`A`$

{ph}`A`

$\{{ph}`a`\}$
```


Examples
--------

```{rewrite-rule}
$\vdash |\{p \mid p \text{ is an even prime}\}| = 1$

$\vdash 2 \in \{p \mid p \text{ is an even prime}\}$

$\{p \mid p \text{ is an even prime}\}$

$\{2\}$
```
