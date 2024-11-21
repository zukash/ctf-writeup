---
tags:
  - crypto/secret_sharing/shamir
  - crypto/polynomial/interpolation
  - crypto/misc/chinese_remainder_theorem
  - todo
createdAt: 2024/11/21
---

# Share

ref. <https://www.0xatticus.com/posts/hitcon2023/hitcon2023_share/>

## 概要

* shamir's secret sharing
* 独自実装はバグを疑う
  * 数値範囲
* 多項式補間
  * lagrange_polynomial

## 観察

* $n$ 変数に対して $n-1$ 個の条件しかなく解けなさそう
* `secret` を全探索したとしても、どれが正しいのか判断できないのでは？
* `poly` の生成が `getRandomRange(0, self.p - 1)` になっている
  * 「定数項以外に $p-1$ が含まれない多項式」という空間に限定されている
  * 多項式補間の結果、この空間外の多項式になったならば、真の `poly` ではない、と判断できる

## 解法

* Chinse Remainder Theorem より、小さな $p$ の問題に分解できる
* $p$ が小さいので `secret` の全探索が可能
* `solve.py` 参照
