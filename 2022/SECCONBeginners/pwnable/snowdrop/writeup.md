---
tags:
  - pwn/bof
  - pwn/shellcode
createdAt: 2024/11/22
---

# snowdrop

## 概要

* Buffer Overflow
* shellcode

## 観察

* stack 領域が実行可能
* stack 領域の一部が leak されている

## 解法

* stack 領域に shellcode を書き込む
* shellcode に向けて ret
