from secrets import randbelow
from Crypto.Util.number import getPrime
import sys

SIZE = 256


class PCG:  # Polynomial Congruential Generator
    def __init__(self):
        self.m = getPrime(256)
        self.coeff = [randbelow(self.m - 1) for _ in range(SIZE)]
        self.x = randbelow(self.m - 1)

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


pcg = PCG()
print(f"{pcg.m = }")
print(f"{pcg.coeff = }")
print(f"{pcg.x = }")


m = pcg.m
x = pcg()

MM = []
V = []
for _ in range(SIZE):
    M = [pow(x, i, m) for i in range(SIZE)]
    MM.append(M)
    x = pcg()
    V.append(x)
MM = matrix(GF(m), MM)
V = vector(GF(m), V)
C = MM.inverse() * V
C = C[::-1]
assert list(C) == list(pcg.coeff)
