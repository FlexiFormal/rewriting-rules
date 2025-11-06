Section 5: Comprehension Term Reduction
=======================================

A comprehension term is, in its most general form, an expression of the form
$C := \{R[t[y_1, \dots, y_m]] \mid \varphi[y_1, \dots, y_m]\}$, where $R$ is a
[guarded identifier](/guarded_identifiers.md), and $t$ and $\varphi$ are a term
and a (possibly informal) formula, resp., whose free variables are among $y_1, \dots, y_m$.
We consider $R$ trivial if no relational constraints are
specified, and we consider $t$ trivial if it is a plain variable, which lets us classify
comprehension terms as

  - **unguarded** if both $R$ and $t$ are trivial (e.g. "$\{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$"),
  - **term-guarded** if just $t$ is non-trivial (e.g. "$\{n^2 \mid n \in \mathbb{N}\}$"),
  - **relation-guarded** if just $R$ is non-trivial (e.g. "$\{1 \leq i \leq n \mid 1/i < \varepsilon\}$"), or
  - **relation-term-guarded** if both $R$ and $t$ are non-trivial (e.g.
    "$\{\langle p,n \rangle \in \mathbb{N} \times \mathbb{N} \mid p \text{ is a prime divisor of } n\}$").

We call a rewriting operation that eliminates a comprehension term from an
expression a comprehension term reduction.
If we want to reduce an expression of the form "$x \in C$" (or, analogously, the
verbalized variant "$x$ is/be an element of $C$"), where $C$ is a comprehension term,
we have to distinguish several cases depending on the structure of $C$.
Moreover, for each case we have to take the
structure of the sentence that contains the expression "$x \in C$" into account,
where we distinguish between

  - **assertion expressions**, i.e. expressions starting with an (optional) `then` (see below),
  - **declaration expressions**, i.e. sentences starting with `let` (see below),
  - **choice expressions**, i.e. sentences starting with `choose` (see below) or
  - **determiner expressions**, i.e. expressions starting with a determiner.

Moreover, in the case of declaration, choice and determiner expressions we
can have additional trailing expressions after the comprehension term that can
affect the result of the comprehension term reduction. Such trailing expressions
can involve additional adjective phrases, verb phrases, noun phrases
or proposition phrases.

```{code-block} nbnf
<then> = 'then'
       | 'hence'
       | 'thus'
       | 'therefore'
       | 'assume'
```

```{code-block} nbnf
<let> = 'let'
```

```{code-block} nbnf
<choose> = 'choose'
         | 'take'
         | 'consider'
         | 'pick'
```


```{toctree}
:maxdepth: 1

./rules/rule_5_01.md
./rules/rule_5_02.md
./rules/rule_5_03.md
./rules/rule_5_04.md
./rules/rule_5_05.md
./rules/rule_5_06.md
./rules/rule_5_07.md
./rules/rule_5_08.md
./rules/rule_5_09.md
./rules/rule_5_10.md
./rules/rule_5_11.md
./rules/rule_5_12.md
./rules/rule_5_13.md
./rules/rule_5_14.md
./rules/rule_5_15.md
./rules/rule_5_16.md
./rules/rule_5_17.md
./rules/rule_5_18.md
./rules/rule_5_19.md
./rules/rule_5_20.md
./rules/rule_5_21.md
```
