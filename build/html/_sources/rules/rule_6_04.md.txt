Rule 6.4: Parametrized $\iota$-Conversion
=========================================


```{rewrite-rule}
f : <Term> = "$\delta$"

A : <Term> = "$Q \times \Sigma$"

B : <Term> = "$Q$"

a : <Term> = "$(q,c)$"

b : <Term> = "$q'$"

|- $:f: : :A: \to \mathcal{P}(:B:)$

|- $\forall :a: \in :A:. |:f:(:a:)| = 1$

"$:b: \in :f:(:a:)$"

"$:b: = :f:(:a:)$"
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
|- $\delta : Q \times \Sigma \to \mathcal{P}(Q)$

|- $\forall (q,c) \in Q \times \Sigma. |\delta(q,c)| = 1$

"$q' \in \delta(q,c)$"

"$q' = \delta(q,c)$"
```
