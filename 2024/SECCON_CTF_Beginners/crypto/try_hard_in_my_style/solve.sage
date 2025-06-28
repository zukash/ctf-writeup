# ref. https://blog.y011d4.com/20220320-zer0pts-ctf-writeup

from Crypto.Util.number import *
from pwn import *

e, n, t1, t2, c1, c2, c3 = None, None, None, None, None, None, None

# context.log_level = "debug"

# CRT to get m
A, M = [], []
for _ in range(17):
    io = remote("try-hard-in-my-style.beginners.seccon.games", "5000")
    # io = process(["sage", "server.py"])
    exec(io.recvall())
    s, m = PolynomialRing(Zmod(n), "s,m").gens()
    f1 = (m + s) ^ e - c1
    f2 = (m + s * t1) ^ e - c2
    f3 = (m * t2 + s) ^ e - c3
    basis = Ideal([f1, f2, f3]).groebner_basis()
    m17 = -basis[0].constant_coefficient() % n
    A.append(int(m17))
    M.append(int(n))

m17 = CRT(A, M)
print(m17)
m = m17 ^ (1 / 17)
print(m)
print(long_to_bytes(int(m)))
