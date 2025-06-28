---
tags:
createdAt: 2024/05/06
---

# VentBot

## 概要

* 書式文字列攻撃
* GOT Overwrite

## 観察

* 書式文字列攻撃の脆弱性があるので、任意アドレスの読み書きが可能

## 解法

* GOT を読んで libc version を特定する
  * https://libc.blukat.me/
* printf を system に書き換える
