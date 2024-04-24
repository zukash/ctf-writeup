---
tags: [primality-test, carmichael]
createdAt: 2024/01/04
---

# Prime

## 概要

* 素数判定
  * [AKS素数判定](https://ja.wikipedia.org/wiki/AKS%E7%B4%A0%E6%95%B0%E5%88%A4%E5%AE%9A%E6%B3%95)
* 多項式環
  * <http://dopal.cs.uec.ac.jp/okamotoy/lect/2015/dme/lect06.pdf>
* 中国剰余定理
* カーマイケル数 $n$ の性質
  * $\forall a \in Z, a^n \equiv a \pmod n$
* カーマイケル数の生成

## 観察

100 以下の素数の集合を $P_{100}$ とおきます。
以下を満たすような平方因子を持たない合成数 $n$ を見つければ十分です。
$\forall r \in P_{100}, \forall a \in \mathbb{Z}, (x + a) ^ n \equiv x ^ n + a \pmod {x^r-1, n}$

上式は剰余環 $\mathbb{Z_n}[x]/(x^r - 1)$ 上の等式です。
$n$ の素因数集合を $P$ として、中国剰余定理より、以下が成り立ちます。

$$
\mathbb{Z_n}[x]/(x^r - 1) \simeq \prod_{p \in P} \mathbb{Z_p}[x]/(x^r - 1)
$$

また、素数 $p$ と 正整数 $r$ が $r \mid \phi(p)$ の関係を満たすとき、1 の原始 $r$ 乗根 $z$ は $\mathbb{Z_p}$ 上に存在します。
（具体的には、 $p$ の原始根を $\alpha$ として、 $z = \alpha ^ {\phi(p) / r}$ と取ればよいです。）
したがって、 $\forall p \in P, r \mid \phi(p)$ のもとで、中国剰余定理より、以下が成り立ちます。

$$
\prod_{p \in P} \mathbb{Z_p}[x]/(x^r - 1) \simeq \prod_{p \in P} \prod_{i=1}^{r} \mathbb{Z_p}[x]/(x - z^i)
$$

また、さらに以下のように変形できます。

$$
\prod_{p \in P} \prod_{i=1}^{r} \mathbb{Z_p}[x]/(x - z^i)
\simeq
\prod_{p \in P} \prod_{i=1}^{r} \mathbb{Z_p}
\simeq
\prod_{i=1}^{r} \mathbb{Z_n}
$$

したがって、 $\mathbb{Z_n}$ 上で $(x + a) ^ n = x ^ n + a$ を満たす $n$ を求める問題に帰着されました。
この問題は $n$ をカーマイケル数とすれば十分です。
カーマイケル数の性質 $\forall a \in \mathbb{Z}, a^n \equiv a \pmod n$ を繰り返し用いて、等式の成立が示せます。

まとめると、以下を満たす $n$ を答えればよいです。

* $n$ はカーマイケル数である
* $n$ の素因数集合を $P$ として、 $\forall p \in P, \forall r \in P_{100}, r \mid \phi(p)$ である

## 解法

カーマイケル数であるための十分条件が知られているので、これを用いて $n$ を見つけるコードを書きます。

<https://math.stackexchange.com/questions/2295095/what-is-the-fastest-way-to-get-the-next-carmichael-number>
