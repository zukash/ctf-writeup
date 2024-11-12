---
tags:
createdAt: 2024/11/12
---

# pppp

## 概要

* RSA
* matrix RSA
* $ap \equiv c \pmod {pq} \Rightarrow \gcd(pq, c) = p$
* $Z_n$ 上の行列 $A$ が対角化可能ならば $A^{\phi(n)} \equiv I$

## 観察

* $ap \equiv c \pmod {pq} \Rightarrow \gcd(pq, c) = p$
  * $pq \mid ap - c$ であり特に、$p \mid ap - c$ なので
* $Z_n$ 上の行列 $A$ が対角化可能ならば $A^{\phi(n)} \equiv I$
  * $P^{-1}AP = D$ として $P^{-1}A^{\phi(n)} P = (P^{-1}AP)^{\phi(n)} = D^{\phi(n)} = I$ なので

## 解法

* solve.py 参照
