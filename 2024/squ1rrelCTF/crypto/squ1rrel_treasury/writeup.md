---
tags:
createdAt: 2024/05/06
---

# squ1rrel_treasury

## 概要

* AES
* iv を自由に設定できる

## 観察

* `name:balance` 形式の文字列を AES にかけて保存している
* AES にかける前に iv と xor を取っている

## 解法

* key を生成した後で、balance が増えるように iv をいじる
