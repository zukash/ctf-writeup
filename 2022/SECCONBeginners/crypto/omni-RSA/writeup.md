---
tags:
- crypto/rsa
- crypto/bit_extension_search
- crypto/copper_smith_attack
- todo
createdAt: 2024/11/15
---

# omni-RSA

* ref. <https://furutsuki.hatenablog.com/entry/2022/06/05/152549>
* ref. <https://qiita.com/ushigai_sub/items/1182d7f49e7ff92646e7#hard-omni-rsa--240points--14solves->
* ref. <https://zenn.dev/hk_ilohas/articles/ctf4b2022-crypto#omni-rsa-%5Bhard%5D>

TODO: copper_smith_attack のパラメータ調整

## 概要

* 等式を目指す
* 合同方程式
* copper_smith_attack

## 観察

以下のように式変形をして等式を目指す。

```python
Zqr = Zmod((q - 1) * (r - 1))
Z470 = Zmod(2**470)

assert s == d % ((q - 1) * (r - 1)) & (2**470 - 1)
h, t = divmod(d % ((q - 1) * (r - 1)), 2**470)
assert s == t
assert h.bit_length() <= 42  # 512 - 470
assert Zqr(h * 2**470 + s) == Zqr(d)

assert e * d % phi == 1
assert Zqr(e * d) == 1
assert Zqr(e * (h * 2**470 + s)) == 1

# 合同式から等式へ
assert any(e * (h * 2**470 + s) == 1 + k * ((q - 1) * (r - 1)) for k in range(e + 1))
assert rq == r - q
assert any(e * (h * 2**470 + s) == 1 + k * ((q - 1) * (q + rq - 1)) for k in range(e + 1))
```

$h$ と $q$ は未知。方針は2つ。

* $h$ を消す方針 → $Z_{470}$ を考えて、$q$ についての合同方程式を解く
* $q$ を消す方針 → $Z_{q}$ を考えて、 $h$ についての small_roots を計算する

以下は前者の方針。

```python
# 等式から合同式へ
assert any(Z470(e * s) == Z470(1 + k * ((q - 1) * (rq + q - 1))) for k in range(e + 1))

# k は既知として進める
k = ((h * 2**470 + s) * e - 1) // ((q - 1) * (r - 1))
assert Z470(e * s) == Z470(1 + k * ((q - 1) * (rq + q - 1)))
f = lambda x: e * s - 1 - k * ((x - 1) * (rq + x - 1))
assert Z470(f(q)) == 0
```

$f(x) \equiv 0 \pmod {2^{470}}$ の解に $q$ が含まれる。

sage の `solve_mod` を使えば解が得られるが、速度面の問題があったので、以下は高速化の話。

以下が成立することを利用する。

```python
assert all(Zmod(2**i)(f(q)) == 0 for i in range(470))
```

下位 bit から 1 bit ずつ拡張しつつ枝刈りをすると速い。

## 解法

以下のようなコードで実現できる。

```python
S = [0]
for i in range(471):
    # extend
    S += [x | (1 << i) for x in S]
    # filter
    S = list(filter(lambda x: Zmod(1 << i)(f(x)) == 0, S))
```

下位 bit から拡張して枝刈りする手法は何度か出題されているので、多変数に拡張してライブラリ化した。

<https://github.com/zukash/ctftools/blob/main/ctftools/crypto/equation.py>
