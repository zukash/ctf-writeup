---
type: writeup
tags: crypto RSA
---

# fusion

## 要約

* <https://github.com/wani-hackase/wanictf2023-writeup/tree/main/cry/fusion>
* pの偶数bitとqの奇数bitが与えられる
* `p * q == n` の関係を意識しながら筆算をすると解ける
* 下からi桁目までの掛け算が終了したとき、nのi桁目までの結果は確定する
* pのi桁目をflipすると、pqのi桁目もflipされる

## 考察

## 解法
