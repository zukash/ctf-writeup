---
tags:
createdAt: 2024/03/10
---

# themachinist

## 概要

* 汎用性はなさそう

## 観察

* ある変数が 1337 に一致するなら flag がもらえる
* 入力した値が main address よりも大きいか小さいかを教えてくれる
* 1 bit flip できる

## 解法

* main address を二分探索で特定
* cmp の後の jmp 条件を flip させる