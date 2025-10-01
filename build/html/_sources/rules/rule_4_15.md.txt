Rule 4.15: "Either"-NP Aggregation
==================================


```{rewrite-rule}
{ph}`Det_1`, $\ldots$, {ph}`Det_n` : a | no = {nl}`a`, {nl}`no`

{ph}`NP_1`, $\ldots$, {ph}`NP_n` : {cat}`NP` = {nl}`prime`, {nl}`even number`

{ph}`t` : {cat}`Term` = {nl}`$x$`

{ph}`t` is {ph}`Det_1` {ph}`NP_1` or ... or {ph}`t` is {ph}`Det_n` {ph}`NP_n` : {cat}`NP` (and | but) {ph}`t` is not both {ph}`Det_1` {ph}`NP_1` and ... and {ph}`Det_n` {ph}`NP_n`

{ph}`t` is either {ph}`Det_1` {ph}`NP_1` or ... or {ph}`Det_n` {ph}`NP_n`
```

Examples
--------

```{rewrite-rule}
$x$ is a prime or $x$ is no even number but $x$ is not both a prime and no even number

$x$ is either a prime nor no even number
```


