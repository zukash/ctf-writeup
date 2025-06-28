from sage.all import *
from itertools import product
from Crypto.Util.number import *
import codecs
import string
import random

key = "".join(random.sample(string.ascii_lowercase, 10))
rot13_key = codecs.encode(key, "rot13")
key = key.encode()
rot13_key = rot13_key.encode()
key_m = bytes_to_long(key)
rot13_key_m = bytes_to_long(rot13_key)


def list2int(L):
    return sum([L[~i] * 256**i for i in range(len(L))])


for D in product([13, -13], repeat=10):
    if key_m + list2int(D) == rot13_key_m:
        break

d = list2int(D)
assert key_m + d == rot13_key_m

p = getStrongPrime(512)
q = getStrongPrime(512)
n = p * q
e = 137
c1 = pow(bytes_to_long(key), e, n)
c2 = pow(bytes_to_long(rot13_key), e, n)
assert c1 == pow(key_m, e, n)
assert c2 == pow(key_m + d, e, n)

PR = PolynomialRing(Zmod(n), "x")
x = PR.gen()

f1 = x**e - c1
f2 = (x + d) ** e - c2
k = PR(f1._pari_with_name("x").gcd(f2._pari_with_name("x")))
print(k.degree())
print(-k.monic()[0])
