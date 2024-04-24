from Crypto.Util.number import long_to_bytes
from pwn import *

io = remote("choice.beginners.seccon.games", 1336)


def f(x):
    io.sendline(str(x).encode())
    io.recvline()
    return int(io.recvline().split(b":")[-1])


n = int(io.recvline().split(b"=")[-1])
e = int(io.recvline().split(b"=")[-1])
c = int(io.recvline().split(b"=")[-1])
s = int(io.recvline().split(b"=")[-1])

a = n + 1
fa = f(a)
fam1 = f(a - 1)
fap1 = f(a + 1)
fap2 = f(a + 2)

x = (fa * s - n * fam1 + fap2) * pow(fap1, -1, n) % n
phi = n - s + x - 1
d = pow(e, -1, phi)
m = pow(c, d, n)
print(long_to_bytes(m))
