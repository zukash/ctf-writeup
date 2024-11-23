---
tags:
  - pwn/bof
createdAt: 2024/11/22
---

# BeginnersBof

## 概要

* 典型的な Buffer Overflow の問題

## 観察

* `buf` のサイズ以上に入力を受け付けてしまっている
* stack 領域の `buf` 以降に任意の文字列を書き込むことができる

## 解法

* return address を書き換えて `win` に向ける
* offset を調べるのが面倒なのでたくさん送る
