---
tags: lfsr
createdAt: 2024/03/10
---

# BitWar

## 概要

## 観察

* hash 的な役割
  * 100桁以下のbit列を入力すると、8桁のbit列に変換される

## 解法

* output は flag を 1byte ずつ入力した結果と推測
* `{hash(c): c}` のテーブルを用意して復元
