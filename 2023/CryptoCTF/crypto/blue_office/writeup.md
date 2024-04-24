---
type: writeup
tags: crypto
---

# Blue Office

## 要約

## 考察

1文字ごとにxorを取った文字に置き換えるencrypt

seedは10**9通りくらいしかないので、全探索できる？
→ tqdmで計測したところ、11時間かかるみたい
→ 適当な枝刈りしたら40分で終わりそう（最悪時）

seedが分かったとして、decryptはできるだろうか → できそう、というか encrypt == decrypt だった

## 解法
