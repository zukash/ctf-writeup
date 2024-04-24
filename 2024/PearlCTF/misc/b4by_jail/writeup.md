---
tags: pyjail
createdAt: 2024/03/09
---

# b4by_jail

## 概要

* pyjail
* 全角文字列で呼び出し可能

## 観察

* 全角文字が使えるので何かできないか
  * <https://satoooon1024.hatenablog.com/entry/2022/08/20/Python%E3%81%AE%E8%AD%98%E5%88%A5%E5%AD%90%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8BUnicode%E6%AD%A3%E8%A6%8F%E5%8C%96%28NFKC%29%E3%81%A8pyjail>
  * 全角英字で関数呼び出しができる
* `f"__ｉｍｐｏｒｔ__({os}).ｓｙｓｔｅｍ({cmd})"`
  * os と cmd の文字列を作れればよい
* 数字は 0 だけ使える
  * 1 が作れれば嬉しい
  * 0**0 == 1
* `ｃｈｒ(0**0+0**0+...)` で任意の文字が作れる

## 解法
