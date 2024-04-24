"""
X = [x, y, z, w, v]
x * y * z * w * v  == ? mod 31
(x + 1) * y * z * w * v  == ? mod 31
x * (y + 1) * z * w * v  == ? mod 31
x * y * (z + 1) * w * v  == ? mod 31
x * y * z * (w + 1) * v  == ? mod 31

x / (x + 1)
"""

from pwn import *

Fp = GF(31)
D = {}
for c in "acdefghijklmnopqrstuvwxyz":
    b = ord(c) - ord("a")
    D[Fp(0 - b) / Fp(1 - b)] = c
print(len(D))

io = remote("betta.utctf.live", "7496")
# io = process(["python", "main.py"])


for _ in range(3):
    io.sendlineafter(b"?", b"aaaaa")
    io.recvline()
    r0 = int(io.recvline())

    io.sendlineafter(b"?", b"baaaa")
    io.recvline()
    r1 = int(io.recvline())

    io.sendlineafter(b"?", b"abaaa")
    io.recvline()
    r2 = int(io.recvline())

    io.sendlineafter(b"?", b"aabaa")
    io.recvline()
    r3 = int(io.recvline())

    io.sendlineafter(b"?", b"aaaba")
    io.recvline()
    r4 = int(io.recvline())

    r0, r1, r2, r3, r4 = map(lambda t: Fp(-t), (r0, r1, r2, r3, r4))

    x = D[r0 / r1]
    y = D[r0 / r2]
    z = D[r0 / r3]
    w = D[r0 / r4]
    v = (
        Fp(r0)
        / Fp(ord("a") - ord(x))
        / Fp(ord("a") - ord(y))
        / Fp(ord("a") - ord(z))
        / Fp(ord("a") - ord(w))
    )
    v = chr(int(v) + ord("a"))

    io.sendlineafter(b"?", x + y + z + w + v)


io.interactive()
