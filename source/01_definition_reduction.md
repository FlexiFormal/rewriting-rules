Section 1: Definition Reduction
===============================

Consider a symbol $c$ with definiens $\delta$.
Replace $\delta$ by $c$ in a statem $S$ does not change the meaning of $S$.
However, when performing such a replacement we have to be careful
to properly adapt $\delta$ to the grammatical structure of $S$.
For instance, consider the expression "$a$ is applicable in $q$"
(where $a$ denotes an input symbol and $q$ a state of an NFA)
and the definiens "$\delta(a,q)\ne\emptyset$" of "applicable".
If we want to reduce this definiens in, e.g., "an input symbol $a$ with $\delta(a,q)\ne\emptyset$ for all final states $q$" we have te replace "with $\delta(a,q)\ne\emptyset$"
with, e.g. "such that $a$ is applicable in $q$"
 to get the grammatically correct expression
"an input symbol $a$ such that $a$ is applicable in $q$ for all final states $q$".
Note that we can iteratively apply further reweriting operations to this result to get a more compact expression,
for instance "an input symbol $a$ that is applicable in all final states".


Examples
========


```{rewrite-rule}
an input symbol $a$ with $\delta(a,q)\ne\emptyset$ for all final states $q$

$a$ is applicable to $q$ iff $\delta(a,q)\ne\emptyset$

an input symbol $a$ such that $a$ is applicable in $q$ for all final states $q$
```
