---
type: writeup
tags:
---

# matrixrsa

## 要約

## 考察

行列 ((a, m), (0, a)) ^ n の形
<https://www.wolframalpha.com/input?i=%28%28a%2Cm%29%2C%280%2Ca%29%29+%5E+n>

decrypt関数
上の行列の位数（の倍数）を知りたい。
少し考えると、`n * (p - 1) * (q - 1)` が見つかる。

```python
def decrypt(encflag, pq):
    enc_0, enc_1 = encflag
    p, q = pq
    n = p * q
    mat = matrix(Zmod(n), [[enc_0, enc_1], [0, enc_0]])
    d = pow(e, -1, n * (p - 1) * (q - 1))
    msg = mat ** d
    return int(msg[0, 1])
```

`enc0 = a^e`
`enc1 = a^(e-1) * e * m`
である。
`enc0`, `enc1 * 2` を渡せば、`2m` が帰ってくる。
手元で1/2倍して`m`が得られる。

ただし、`enc1 * 2 < n`などの制約があるので、何回かガチャを引く。

## 解法
