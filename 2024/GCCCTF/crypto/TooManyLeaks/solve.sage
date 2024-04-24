from Crypto.Util.number import *

p = getStrongPrime(512)
q = getStrongPrime(512)
n = p * q
e = 0x10001
m = bytes_to_long(b"flag{dummydummy}")
c = pow(m, e, n)

mask = (1 << (256 + 44)) - 1
h = p & mask

print(f"{n = }")
print(f"{e = }")
print(f"{c = }")
print(f"{h = }")

# ********************************************

p = None
q = None
m = None

# ********************************************

x = PolynomialRing(Zmod(n), "x").gen()
f = x * (1 << 300) + h
r = f.monic().small_roots(X=1 << (256 - 44), beta=0.4)[0]
p = int(r) * (1 << 300) + h
q = n // p
assert p * q == n
d = pow(e, -1, (p - 1) * (q - 1))
m = pow(c, d, n)
print(long_to_bytes(m))
