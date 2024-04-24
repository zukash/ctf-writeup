---
tags: ['elliptic-curve']
createdAt: 2024/03/04
---

# Elliptic

## 概要

* 楕円曲線を自由に選べる

## 観察

* anomalous な曲線を選ぶと discrete_log が簡単
* anomalous な楕円曲線は ecgen で生成

## 解法

* SageMath の discrete_log は anomalous の場合に高速に動いてくれる
  * <https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_point.html#sage.schemes.elliptic_curves.ell_point.EllipticCurvePoint_finite_field.padic_elliptic_logarithm>
