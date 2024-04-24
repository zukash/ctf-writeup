from Crypto.Util.number import *
from pwn import *

io = remote("morphing.chal.uiuc.tf", int(1337))
print(io.recvline())
print(io.recvline())
print(io.recvline())

g = int(io.recvline().split(b"=")[-1])
p = int(io.recvline().split(b"=")[-1])
A = int(io.recvline().split(b"=")[-1])
print(g, p, A)

print(io.recvline())
c1 = int(io.recvline().split(b"=")[-1])
c2 = int(io.recvline().split(b"=")[-1])
print(c1, c2)

io.sendline(str(c1).encode())
io.sendline(str(c2).encode())

print()
io.recvuntil(b"m = ")
m2 = int(io.recvline())
print(m2)
print(long_to_bytes(m2))
print()

Z.<x> = Zmod(p)[]
f = x * x - m2
for m, _ in f.roots():
    print(m)
    print(long_to_bytes(int(m)))

io.interactive()
