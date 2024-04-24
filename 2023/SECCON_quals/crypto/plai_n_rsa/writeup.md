---
type: writeup
tags:
---

# plai_n_rsa

## 概要

普通のRSA暗号では、`(e, n)`を公開しますが、今回は`(e, d, p+q)`が公開されています。

## 観察

`d`が公開されているので、`n`が分かれば解読できます。

式を変形していきます。

```python
d = pow(e, -1, phi)
assert e * d % phi == 1
assert (e * d - 1) % phi == 0
assert (e * d - 1) in [k * phi for k in range(e)]  # d < phi
assert (e * d - 1) in [k * (p - 1) * (q - 1) for k in range(e)]
assert (e * d - 1) in [k * (n - hint + 1) for k in range(e)]
assert [(e * d - 1) == k * (n - hint + 1) for k in range(e)].count(True)
```

最後の等式で、未知数は`n`のみです。

## 解法

```python
for k in range(1, e + 1):
    if (e * d - 1) % k != 0:
        continue
    phi = (e * d - 1) // k
    n = phi + hint - 1
    flag = long_to_bytes(pow(c, d, n))
    if b"SECCON" in flag:
        print(flag)
```
