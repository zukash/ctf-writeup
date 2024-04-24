---
type: writeup
tags: forensics foremost
---

# whats-happening

## 要約

* 壊れたバイナリファイルを渡される
* <https://qiita.com/knqyf263/items/6ebf06e27be7c48aab2e>
  * ディスクイメージが渡された場合
* foremost

## 考察

```bash
❯ file updog
updog: ISO 9660 CD-ROM filesystem data 'ISO Label'
```

ISO と書いてあるので、<https://qiita.com/knqyf263/items/6ebf06e27be7c48aab2e>の「ディスクイメージが渡された場合」を読む。

foremostを使ってみる。

## 解法

```bash
❯ foremost updog 
```
