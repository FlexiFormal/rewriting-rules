Rule 6.4: Parametrized $\iota$-Conversion
=========================================


```{rewrite-rule}
{ph}`f` : {cat}`Term` = {nl}`$\delta$`

{ph}`A` : {cat}`Term` = {nl}`$Q \times \Sigma$`

{ph}`B` : {cat}`Term` = {nl}`$Q$`

{ph}`a` : {cat}`Term` = {nl}`$(q,c)$`

{ph}`b` : {cat}`Term` = {nl}`$q'$`

$\vdash {ph}`f` : {ph}`A` \to \mathcal{P}({ph}`B`)$

$\vdash \forall {ph}`a` \in {ph}`A`. |{ph}`f`({ph}`a`)| = 1$

${ph}`b` \in {ph}`f`({ph}`a`)$

${ph}`b` = {ph}`f`({ph}`a`)$
```


Examples
--------

We call a finite automaton with transition function
$\delta : Q \times \Sigma \to \mathcal{P}(Q)$ *deterministic* if
$\vdash \forall (q,c) \in Q \times \Sigma. |\delta(q,c)| = 1$ holds.
In this case we can regard $\delta$ as a function from
$Q \times \Sigma$ to $Q$ which allows us (by abuse of notation) to
write expressions of the form $q' \in \delta(q,c)$ as
$q' = \delta(q,c)$ which is captured by the following instance of
the above rewrite rule:

```{rewrite-rule}
$\vdash \delta : Q \times \Sigma \to \mathcal{P}(Q)$

$\vdash \forall (q,c) \in Q \times \Sigma. |\delta(q,c)| = 1$

$q' \in \delta(q,c)$

$q' = \delta(q,c)$
```
