---
tags: [seccomp, shellcode]
createdAt: 2024/03/10
---

# flag-finder

## 概要

* seccomp
* shellcode

## 観察

* 0x1000 の連続した領域のどこかに flag が書き込まれている
* 0x100 以下の shellcode を送りつけて実行できる
* seccomp が設定されている
  * [seccomp-tools](https://github.com/david942j/seccomp-tools) を install
  * WRITE 以外の syscall が呼べない状態になっている
* flag を領域に書き込む際の痕跡が stack 領域に残っている

## 解法

* stack 領域に残っている flag を stdout に書き込む
* call puts を呼べばいい
