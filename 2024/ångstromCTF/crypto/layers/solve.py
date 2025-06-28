from pwn import *

io = remote("challs.actf.co", 31398)
io.sendlineafter(b">", b"2")
io.sendlineafter(b">", b"00" * 38)
key = bytes.fromhex(io.recvline().strip().decode())

io = remote("challs.actf.co", 31398)
io.sendlineafter(b">", b"3")
enc = bytes.fromhex(io.recvline().strip().decode())

flag = xor(key, enc)
print(flag)

io.interactive()
