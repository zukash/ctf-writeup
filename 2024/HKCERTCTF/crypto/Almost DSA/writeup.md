---
tags:
createdAt: 2024/11/09
---

# Almost DSA

## 概要

## 観察

> According to an external auditor, my code implementing the data signature algorithm (DSA) has a one-byte security fix on a critical issue.

```python
assert 0 < s < p

w = inverse(s, q)
```

s = q とすれば w = 0 となる。

## 解法
