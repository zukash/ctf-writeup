---
tags: rop
createdAt: 2024/03/09
---

# Adventure

## 概要

* no-libc
* bof
* rop

## 観察

* no-source
  * <https://dogbolt.org/>
  * これに入れてコードを読む
* buffer overflow の脆弱性を発見
* `pop rdi; ret` が存在するのでやりたい放題
* no-libc
  * <https://libc.blukat.me/>
  * リモートの GOT をいくつか leak させてバージョンを特定する
* `system('/bin/sh')` を呼ぶ

## 解法
