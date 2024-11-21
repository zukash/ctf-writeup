---
tags:
  - crypto/rsa
  - crypto/equation/bit_extension_search
createdAt: 2024/05/13
---

# easy-rsa

## 概要

* RSA
* p と q に関するヒントが与えられる
  * `q & p`
  * `q & (p << 1)`

## 観察

* 下から $i$ 桁目までの掛け算が終了したとき、$n$ の $i$ 桁目までの結果は確定する
* ヒントを頼りに必要条件で絞りながら列挙してくと、候補が爆発的に増えることがない

## 解法

* 下から一桁ずつ試していく
* `solve.py` 参照
* <https://github.com/zukash/ctftools/blob/main/ctftools/crypto/equation.py>
