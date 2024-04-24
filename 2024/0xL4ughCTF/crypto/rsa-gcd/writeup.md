---
tags: RSA
createdAt: 2024/02/28
---

# rsa-gcd

## 概要

* $n$ の素因数 $p$, $q$ を使ったヒントが与えられる
  * $(p + q)^e \equiv p^e + q^e \pmod n$
* next_prime で情報が落ちているように見えるが...
  * 素数定理より、次の素数までの間隔は実はそんなに大きくない

## 観察

* `next_prime(x) - x` の値は $log(x)$ くらいになるらしい
* out1 と out2 の両方が分かっている前提で進めて OK

## 解法

* $(p + q)^e \equiv p^e + q^e \pmod n$ を使って式を整理
* $p$ だけの式にしたら $n$ との gcd を取る
