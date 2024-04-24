---
tags: EllipticCurve
createdAt: 2024/02/28
---

# Poison

## 概要

* $abG = baG$

## 観察

* 変数定義が分かりにくいので置き直す
* (Ms, Xs, Ys, Zs) から priv を計算したい
* 関係を整理する
  * Q: fixed point
  * M: random point
  * X = kG
  * Y = M + kQ = M + kpG
  * Z = Y - p'X = Y - kp'G
* Z - M = kpG - kp'G = (p - p')X が導かれる
* p - p' の候補は 2 種類しかない

## 解法

* Z - M と X を見比べることで p を特定する
