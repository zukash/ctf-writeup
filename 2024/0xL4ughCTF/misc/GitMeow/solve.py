from pwn import *

io = remote("172.190.120.133", "50001")

io.sendlineafter(b"?", b"show")
io.interactive()
