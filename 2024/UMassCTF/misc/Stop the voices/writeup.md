---
tags:
createdAt: 2024/04/24
---

# Stop the voices

## 概要

* FLAG.png にランダムノイズを入れた 400 枚の画像が配られる（容量大きいので消した）

## 観察

* 適当に画像を用意して同じようにプログラムを動かしてみる
  * うっすらと元画像が読めるくらいのノイズ強度だった
* 400枚もあるのだから、平均を取ったら元の画像がよりくっきり見えそう

## 解法

* 平均を取ったら元の画像がよりくっきり見えた
* まだぼんやりしていたので、境界をはっきりさせるフィルタをかけたらよく読めるようになった
* 画像操作系は GPT4 が大活躍
