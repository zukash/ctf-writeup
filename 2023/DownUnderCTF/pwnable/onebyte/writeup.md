# onebyte

## 概要

1 バイト分の buffer overflow

## 観察

* return_addr の参照先の下位 1 バイトを書き換えられる
* return_addr の参照先を payload にできれば勝ち
* payload の開始位置の下位 1 バイトが 0x00 である場合に動作するプログラムを簡単に作成可能
  * そのような状況は 1/16 の確率で発生する

## 解法

```python
pack(win_addr) * 4 + b'0x00'
```

を送ると 1/16 の確率で shell を奪える。
