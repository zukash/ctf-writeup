---
tags:
createdAt: 2024/03/09
---

# Security++

## 概要

* AES ECB のキーを 2 本にして、交互に使ったらどうなるか
* いつも通り末尾から一文字ずつ決めていける

## 観察

* enc.py をよく読んでないけど、AES ECB っぽい
* アイデア
  * 32を法として、全体が 1 byteになったとする
  * 末尾は pad(flag[-1]) になっているはず
  * pad(c) と比較して一致するなら、flag[-1] == c と特定できる

## 解法