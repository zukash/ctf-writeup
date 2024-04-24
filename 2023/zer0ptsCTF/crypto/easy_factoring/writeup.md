---
type: writeup
tags: crypto
---

# easy_factoring

## 要約

2つの平方数の和

めっちゃ参考にした。
<https://nonagon.org/ExLibris/fermat-sum-two-squares-calculator>
実装がないので、再帰関数を自作。

素数のときがベースケースになるが、p mod 4 == 1 のときだけ考えれば回る？
p mod 4 == 1 のときは、p == a^2 + b^2 なる (a, b) が一意に定まるらしい。
それを高速に計算する方法も知られている。
<https://math.stackexchange.com/questions/5877/efficiently-finding-two-squares-which-sum-to-a-prime>

実装があるので貼り付け。理解していない。

## 考察

## 解法
