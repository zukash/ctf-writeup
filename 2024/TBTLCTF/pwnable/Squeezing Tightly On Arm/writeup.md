---
tags:
createdAt: 2024/05/13
---

# Squeezing Tightly On Arm

## 概要

* pyjail
* walrus operator `:=`
  * python 3.8 から導入された
* <https://www.youtube.com/watch?v=dyD2IgN8_Mk&t=2175s>
* <https://github.com/ryanking13/ctf-cheatsheet/blob/master/Pwnable/jail/pyjail.md>

## 観察

* os.system 呼び出し
  * `scratch.py` 参照
  * object から os.system を辿って呼び出すまでの流れ
* `.` を一回しか使えない
  * object から辿る方法が取れないのでは？
* eval は式しか実行できない
  * `:=` は代入式
  * 代入できるなら解けそう

## 解法

* `solve.py` 参照
