from pwn import *

io = remote("c21-almost-dsa.hkcert24.pwnable.hk", 1337, ssl=True)

q = 113298192013516195145250438847099037276290008150762924677454979772524099733149
r = 1
s = q

io.sendlineafter("r = ", str(r).encode())
io.sendlineafter("s = ", str(s).encode())

io.interactive()
