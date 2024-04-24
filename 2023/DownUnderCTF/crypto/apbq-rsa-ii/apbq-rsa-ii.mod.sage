from itertools import combinations
from Crypto.Util.number import getPrime, bytes_to_long
from random import randint
from math import gcd

p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 0x10001

hints = []
A = []
B = []
X = []
for _ in range(3):
    a, b = randint(0, 2 ** 312), randint(0, 2 ** 312)
    A.append(a)
    B.append(b)
    hints.append(a * p + b * q)
    X.append(a * p + b * q)

for x, y in combinations(X, 2):
    g = gcd(x, y)
    print(g)


FLAG = open("flag.txt", "rb").read().strip()
c = pow(bytes_to_long(FLAG), e, n)
print(f"{n = }")
print(f"{c = }")
print(f"{hints = }")

h0, h1, h2 = hints
g01, s01, t01 = xgcd(h0, h1)
g02, s02, t02 = xgcd(h0, h2)
# たまたまそうなってた、そうでなくてもできる。
assert g01 == g02 == 1
assert s01 * h0 + t01 * h1 == 1

# (sa + ta)p + (sb + tb)q == 1
# (s01 * a0 + t01 * a1)p + (s01 * b0 + t01 * b1)q == 1
# (s02 * a0 + t02 * a2)p + (s02 * b0 + t02 * b2)q == 1
# ->
# (s01 * a0 + t01 * a1) - (s02 * a0 + t02 * a2) == 0 (mod q)
# (s01 * b0 + t01 * b1) - (s02 * b0 + t02 * b2) == 0 (mod p)
# ->
# (s01 - s02) * a0 + t01 * a1 - t02 * a2 == 0 (mod q)
# (s01 - s02) * b0 + t01 * b1 - t02 * b2 == 0 (mod p)

print(gcd(n, (s01 + t01) - (s02 + t02)))

print(f"{p=}")
print(f"{q=}")
print(f"{A=}")
print(f"{B=}")

a0, a1, a2 = A
b0, b1, b2 = B
assert ((s01 - s02) * a0 + t01 * a1 - t02 * a2) % q == 0
assert ((s01 - s02) * b0 + t01 * b1 - t02 * b2) % p == 0

# ------------------------------------------

M = Matrix([[1, 0, 0, s01 - s02], [0, 1, 0, t01], [0, 0, 1, t02]])
print(M.LLL())
