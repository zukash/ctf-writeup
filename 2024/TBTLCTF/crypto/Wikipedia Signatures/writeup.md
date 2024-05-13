---
tags:
createdAt: 2024/05/13
---

# Wikipedia Signatures

## 概要

* RSA を使った署名
* `TARGET` 以外の任意文字列の sign が手に入る
* `sign(TARGET)` を作りたい

## 観察

* $\mathrm{sign}(2m) = \mathrm{sign}(2) \cdot \mathrm{sign}(m)$

## 解法

* $\mathrm{sign}(2m)$ に対して、$\mathrm{sign}(2)$ の逆元をかける
