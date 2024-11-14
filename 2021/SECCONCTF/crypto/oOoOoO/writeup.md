---
tags:
- crypto/lll/subset_sum_problem
createdAt: 2024/11/12
---

# oOoOoO

## 概要

* LLL
* subset sum problem
* bytes 型を base256 とみなす
* 巨大な数同士を小さな係数で結びつける式

## 観察

* `bytes_to_long(c) % m` が与えられる
  * $\sum c_i 256^{i} \equiv s \pmod m$
  * 巨大な数同士を小さな係数で結びつける式 → LLL
* $\sum c_iA_i \equiv t \pmod m$ を満たす $c_i \in \{\alpha, \beta\}$ を見つける問題に帰着
* $\sum c_i'A_i \equiv t - \sum \alpha A_i \pmod m$ を満たす $c_i' \in \{0, \beta - \alpha\}$ を見つける問題に帰着
* 数列 $(\beta - \alpha)A_i$ の部分集合で、その和が $t - \sum \alpha A_i$ に合同なものを見つければよい

## 解法

> 数列 $(\beta - \alpha)A_i$ の部分集合で、その和が $t - \sum \alpha A_i$ に合同なものを見つければよい

部分和問題っぽいけど「合同なもの」を見つける必要がある。

$m$ を法として $a$ に合同なものは $a + km$ で表される。

数列は $(\beta - \alpha)A_i \bmod m$ を考えれば十分なので、$k$ の範囲は $0 \lt k \lt |A|$ に絞られる。

したがって、部分和問題を高々 $|A|$ 回解けばよい。
