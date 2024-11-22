---
tags:
  - crypto/rsa
  - crypto/equation/bit_extension_search
createdAt: 2024/11/22
---

# fusion

* <https://github.com/wani-hackase/wanictf2023-writeup/tree/main/cry/fusion>
* <https://qiita.com/kusano_k/items/b63cc22c38cbf172f79d#fusion-normal>

## 概要

* RSA
* p と q に関するヒントが与えられる
  * p の偶数ビット目
  * q の奇数ビット目

## 観察

* 下から $i$ 桁目までの掛け算が終了したとき、$n$ の $i$ 桁目までの結果は確定する
* ヒントを頼りに必要条件で絞りながら列挙してくと、候補が爆発的に増えることがない

## 解法

* 下から一桁ずつ試していく
* `solve.py` 参照
* <https://github.com/zukash/ctftools/blob/main/ctftools/crypto/equation.py>
