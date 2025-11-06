Rule 5.12: Determiner-NP Comprehension Term Reduction
=====================================================


```{rewrite-rule}
Det : <Det> = "all"

opt_AP : [<AP>] = ""

NP : <NP> = "real number"

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":Det: :opt_AP: $:x: \in \{:y: \mid :P:[:y:]\}$ that is a :NP:"

":Det: :opt_AP: :NP: :x: with $:P:[:x:]$"
```


Examples
--------

```{rewrite-rule}
"all $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that are real numbers"

"all real numbers $x$ with $x^n = 1$ for some $n \in \mathbb{N}$"
```

```{rewrite-rule}
"certain positive $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that are real numbers"

"certain positive real numbers $x$ with $x^n = 1$ for some $n \in \mathbb{N}$"
```
