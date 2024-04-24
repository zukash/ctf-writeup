# ctf-writeup-template

CTF の問題を解く際のテンプレート

## 事前準備

* .devcontainer 設定（Docker 利用時）
  * image を指定する
  * ex) <https://github.com/zukash/ctf-env>

## フォルダ構成

```bash
❯ tree .                
.
├── 2024  # 開催年
│   └── SampleCTF  # コンテスト名
│       ├── crypto  # ジャンル名
│       │   └── sample-crypto-problem  # 問題名
│       │       ├── main.py
│       │       └── writeup.md  # 解けたら writeup を書く
│       ├── forensics
│       │   └── sample-forensics-problem
│       │       └── main.py   # 解けなかったら writeup を書かない
│       ├── misc
│       │   └── sample-misc-problem
│       │       ├── main.py
│       │       └── writeup.md
│       ├── pwnable
│       │   └── sample-pwnable-problem
│       │       ├── main.py
│       │       └── writeup.md
│       ├── reversing
│       │   └── sample-reversing-problem
│       │       ├── main.py
│       │       └── writeup.md
│       └── web
│           └── sample-web-problem
│               ├── main.py
│               └── writeup.md
├── README.md
└── tools
```

## 機能

* generate_template
  * コンテスト名を入力すると雛形が作成される
  * Build Task から実行する
* writeup_template
  * writeup の雛形が作成される
  * タイトル、日付などが自動入力される
  * snippet から実行する
* generate_summary_table
  * 解答状況などをまとめた表が作成される
    * ex) [2024/README.md](2024/README.md)
  * main への PR 作成時に GitHub Actions から実行される
