---
tags:
createdAt: 2024/02/23
---

# programming

## 概要

## 観察

* No.1
  * `mod 1<<16` で考える
* No.2
  * 誤差の問題
* No.3
  * めっちゃ小さいやつとめっちゃでかいやつ入れて相殺
  * 絶対値の小さい値は情報落ちするはず

## 解法

```python
from pwn import *

io = remote("0.cloud.chals.io", 30531)

io.sendlineafter(b":", str((1 << 16) + 2).encode())
io.sendlineafter(b":", str(0.0999999).encode())
io.sendlineafter(b":", str(3.40282e38).encode())
io.sendlineafter(b":", str(-3.40282e38).encode())
io.interactive()
```
