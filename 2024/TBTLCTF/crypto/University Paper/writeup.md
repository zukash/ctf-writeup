---
tags:
createdAt: 2024/05/13
---

# University Paper

## 概要

* `School Essay` の続き
* 以下が与えられる
  * 合成数 $n$
  * $m^2 \bmod n$
  * $\lfloor m^{2/3} \rfloor$
* $m$ を計算したい

## 観察

* $\lfloor m^{2/3} \rfloor^{3/2}$ は $m$ に近い値になるはず
* 欠損している下位ビットの大きさは $n^{1/2}$ 以下なので、CopperSmith で復元できそう

## 解法

* CopperSmith には SageMath の small_roots を使う
  * <https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/polynomial_modn_dense_ntl.html#sage.rings.polynomial.polynomial_modn_dense_ntl.small_roots>
  * 精度が足りずに解が出ない時は epsilon の値を小さくする
    * `f.small_roots(epsilon=0.03)` みたいに
    * 実行時間とトレードオフになっている
