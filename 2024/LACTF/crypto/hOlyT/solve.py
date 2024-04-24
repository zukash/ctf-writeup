from math import gcd
from pwn import *
from Crypto.Util.number import long_to_bytes

io = remote("chall.lac.tf", "31171")

io.recvuntil(b"ct = ")
ct = int(io.recvline())
io.recvuntil(b"N = ")
n = int(io.recvline())
io.recvuntil(b"e = ")
e = int(io.recvline())

while True:
    io.sendlineafter(b">", b"1")
    h = int(io.recvline())
    print(f"{h = }")
    if gcd(n, h - 1) != 1:
        p = gcd(n, h - 1)
        q = n // p
        break

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(ct, d, n)
print(long_to_bytes(m))

io.interactive()
# int(io.recvline())
