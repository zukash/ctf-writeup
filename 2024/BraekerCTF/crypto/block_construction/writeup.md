---
tags:
createdAt: 2024/03/13
---

# block_construction

## 概要

* 汎用性 少ない
* AES-ECB は 16bytes 文字列空間の全単射写像

## 観察

* `AES_ECB(cx...x) == AES_ECB(xx...x)` ならば `c == x`
* `random.seed(int(time()))`
  * int(time()) の候補は多くない

## 解法

* `int(time())` で全探索
  * 1秒あたり10時間分くらい遡れる
