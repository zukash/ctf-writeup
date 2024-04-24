from pwn import *

INF = 10**18
io = remote("krusty-katering.ctf.umasscybersec.org", 1337)


count = 0

for _ in range(1000):
    io.sendline(b"1")
    count += 1
    print(count)
io.interactive()
