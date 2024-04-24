#!/usr/bin/env python3

from Crypto.Util.number import *
from secret import m, flag


def genPrime(m, nbit):
    assert m >= 2
    while True:
        a = getRandomNBitInteger(nbit // m)
        r = getRandomNBitInteger(m ** 2 - m + 2)
        p = a ** m + r
        if isPrime(p):
            return (p, r)


def genkey(m, nbit):
    p, r = genPrime(m, nbit // 2)
    q, s = genPrime(m, nbit // 2)
    n = p * q
    e = r * s
    return (e, n, r, s, p, q)


def encrypt(msg, pkey):
    e, n, r, s, p, q= pkey
    m = bytes_to_long(msg)
    c = pow(m, e, n)
    return c


pkey = genkey(m, 2048)
enc = encrypt(flag, pkey)

print(f"pkey = {pkey}")
print(f"enc = {enc}")

##########################################################
e, n, r, s, p, q = pkey
print(e.bit_length())
print(r, s)
assert r * s == e
assert ((p - r) ^ (1/4)).is_integer()
assert e.bit_length() == (m ** 2 - m + 2) * 2
print(n.bit_length())

print(f'{p=}')
print(f'{r=}')

z = (p - r) ^ (1/2)
assert z.is_integer()
assert z ** 2 + r == p
assert ((q - s) ^ (1/4)).is_integer()
w = (q - s) ^ (1/2)

P.<x> = Zmod(n)[]
f = x * x + s


# x0 = f.small_roots(X=2^kbits, beta=0.3)[0]  # find root < 2^kbits with factor >= n^0.3
# print(f.small_roots(X=2^(n.bit_length()//7), beta=0.3))
print(f.small_roots(X=q, beta=0.4))
print(f.small_roots(epsilon=1/30))
##########################################################
a = (p - r) ^ (1/4)
b = (q - s) ^ (1/4)

assert a * b == n^(1/4)