---
tags: heap
createdAt: 2024/03/10
---

# pWN_tO_gIVE

## 概要

* heap
  * malloc(0x28)
  * malloc(0x4b0)
  * free(any)
  * edit(0x64)
  * puts(any)
* use after free
* double free
* libc-2.31
  * __free_hook

## 観察

* use after free
  * free 後に参照を持ち続けている
* libc leak
  * unsorted bin に入った chunk を puts することで main_arena_address を leak
* __free_hook
  * libc-2.34 以下なので、__free_hook が生きている

## 解法

* libc leak
  * malloc(0x4b0) → free(any) → puts(any)
* `system(/bin/sh)`
  * double free
  * free(any) → free(any) → edit(0x64) → malloc(0x28)
  * 任意アドレスへの R/W を得る
  * __free_hook に system を書き込み
* heap buffer overflow を使っても解けるらしい
  * malloc size < edit size なので、隣接する chunk を壊せる
