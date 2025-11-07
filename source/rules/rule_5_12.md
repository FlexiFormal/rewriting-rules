Rule 5.12: Determiner-NP Comprehension Term Reduction
=====================================================


```{rewrite-rule}
Det : <Det> = "all"

AP_opt : [<AP>] = ""

NP : <NP> = "real number"

x : <Var> = "$x$"

y : <Var> = "$z$"

P[a] : <Pred> = "$:a:^n = 1 \text{ for some } n \in \mathbb{N}$"

":Det: :AP_opt: $:x: \in \{:y: \mid :P:[:y:]\}$ that is a :NP:"

--- Determiner-NP Comprehension Term Reduction

":Det: :AP_opt: :NP: :x: with $:P:[:x:]$"
```


Examples
--------

```{rewrite-rule}
"all $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that are real numbers"

--- Determiner-NP Comprehension Term Reduction

"all real numbers $x$ with $x^n = 1$ for some $n \in \mathbb{N}$"
```

```{rewrite-rule}
"certain positive $x \in \{z \mid z^n = 1 \text{ for some } n \in \mathbb{N}\}$ that are real numbers"

--- Determiner-NP Comprehension Term Reduction

"certain positive real numbers $x$ with $x^n = 1$ for some $n \in \mathbb{N}$"
```
