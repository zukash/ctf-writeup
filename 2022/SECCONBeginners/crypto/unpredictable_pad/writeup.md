---
tags:
createdAt: 2024/11/12
---

# unpredictable_pad

## 概要

* randcrack

## 観察

* 入力バリデーションの脆弱性
  * 負の数が入力できる
* Mersenne Twister 予測
  * random.getrandbits(32) の情報が 624 個あれば内部状態が復元可能

## 解法

solve.py 参照
