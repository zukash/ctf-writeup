---
createdAt: 2024/11/14
tags:
- crypto/aes
- crypto/aes/cbc
---

# command

## 概要

* AES CBC 復号時の iv を自由に設定できる

## 観察

* CBC 復号時の iv を自由に設定できる
* 1ブロック目だけみると `CBC(x) = ECB(iv, x)` の関係

CBC の疑似コード

```pseudo
ct <- iv
loop:
  ct <- ECB(xor(ct, pt))
  pt <- next(pt)
```

## 解法

```plaintext
CBC(iv, x) = ECB(iv^x)
           = ECB((iv^x^y)^y)
           = CBC(iv^x^y, y)
```
