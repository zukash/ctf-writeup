from pwn import *

from secrets import randbelow
from Crypto.Util.number import getPrime

SIZE = 256


class PCG:  # Polynomial Congruential Generator
    def __init__(self, m, coeff, x):
        self.m = m
        self.coeff = coeff
        self.x = x

    def __call__(self):
        newx = 0
        for c in self.coeff:
            newx *= self.x
            newx += c
            newx %= self.m
        self.x = newx
        return self.x

    def printm(self):
        print(self.m)
        return


SIZE = 256
io = remote("tamuctf.com", "443", ssl=True, sni="pcg")
# io = process(["python", "pcg.py"])
m = int(io.recvline())
X = []
for _ in range(SIZE * 3):
    X.append(int(io.recvline()))

X = X[::-1]
x = X.pop()
MM = []
V = []
for _ in range(SIZE):
    M = [pow(x, i, m) for i in range(SIZE)]
    MM.append(M)
    x = X.pop()
    V.append(x)
MM = matrix(GF(m), MM)
V = vector(GF(m), V)
C = MM.inverse() * V
C = C[::-1]

pcg = PCG(m, C, x)

while X:
    x = X.pop()
    assert x == pcg()

for i in range(SIZE // 2):
    io.sendline(str(pcg()).encode())

io.interactive(prompt="")
