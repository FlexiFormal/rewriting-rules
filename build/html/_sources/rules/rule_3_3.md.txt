Rule 3.3: Tuple Determiner Reduction
====================================


```{rewrite-rule}
{ph}`Det` : {cat}`Det` = {nl}`any`

{ph}`opt_NP` : [{cat}`NP`] = {nl}``

{ph}`t_1`, $\ldots$, {ph}`t_n` : {cat}`Term` = {nl}`$x$`, {nl}`$y$`

{ph}`T_1`, $\ldots$, {ph}`T_n` : {cat}`Term` = {nl}`$\mathbb{R}$`, {nl}`$\mathbb{R}$`

{ph}`Det` {ph}`opt_NP` {ph}`t_1`, $\ldots$, {ph}`t_n` with $\langle$ {ph}`t_1`, $\ldots$, {ph}`t_n` $\rangle \in$ {ph}`T_1` $\times \ldots \times$ {ph}`T_n`

{ph}`Det` $\langle$ {ph}`t_1`, $\ldots$, {ph}`t_n` $\rangle \in$ {ph}`T_1` $\times \ldots \times$ {ph}`T_n`
```

````{note}
This could also be considered a special case of
a generalized form of [Rule 3.2](rule_3_2.md):

```{rewrite-rule}
{ph}`Det` : {cat}`Det` = {nl}`those` 

{ph}`opt_NP` : [{cat}`NP`] = {nl}`states`

{ph}`t_1`, $\ldots$, {ph}`t_n` : {cat}`Term` = {nl}`$p$`, {nl}`$q$`

{ph}`R`$[${ph}`x_1`, $\ldots$, {ph}`x_n`$]$ : {cat}`guarded identifier` = {nl}``{ph}`x_1`, {ph}`x_2` $\in Q \setminus F$``

{ph}`Det` {ph}`opt_NP` {ph}`t_1`, $\ldots$, {ph}`t_n` with {ph}`R`$[${ph}`t_1`, $\ldots$, {ph}`t_n`$]$

{ph}`Det` {ph}`opt_NP` {ph}`R`$[${ph}`t_1`, $\ldots$, {ph}`t_n`$]$
```
````

Example:

```{rewrite-rule}
any $x, y$ with $\langle x, y \rangle \in \mathbb{R} \times \mathbb{R}$

any $\langle x, y \rangle \in \mathbb{R} \times \mathbb{R}$
```

```{rewrite-rule}
those states $p, q$ with $p, q \in Q \setminus F$

those states $q \in Q \setminus F$
```


