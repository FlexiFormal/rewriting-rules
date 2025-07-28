Section 2: Variable Reduction
=============================


Expressions that contain a subexpression $e$ of the form
"$x$ such that" followed by an expression $e'$ that contains another,
redundant occurrence of $x$ can often be condensed by merging $e$ with $e'$.

```{toctree}
:maxdepth: 1

./rules/rule_2_1.md
./rules/rule_2_2.md
./rules/rule_2_3.md
```


````{note}
There are cases in which we can eliminate the variable in an adjective
or verb variable reduction completely.
However, such an elimination depends on the context in which the expression to be reduced occurs.
For instance if we were to blindly eliminate the variable $X$
in this example

```{rewrite-rule}
Consider a set $X$ such that $X$ is infinite.

Consider a set that is finite.
```
 any reference to $X$ that occurs in the context of that statement
 would suddenly be undeclared.
 ````


