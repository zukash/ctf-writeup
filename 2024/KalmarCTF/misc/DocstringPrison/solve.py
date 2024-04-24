from pwn import *

io = process(["python", "server.py"])
# io = remote()

io.sendlineafter(b">", chr(0x1A).encode())
io.interactive()
