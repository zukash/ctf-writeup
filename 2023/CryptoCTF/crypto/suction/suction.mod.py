#!/usr/bin/env python3

from Crypto.Util.number import *
from flag import flag


def keygen(nbit, r):
    while True:
        p, q = [getPrime(nbit) for _ in "__"]
        e, n = getPrime(16), p * q
        phi = (p - 1) * (q - 1)
        if GCD(e, phi) == 1:
            N = bin(n)[2:-r]
            E = bin(e)[2:-r]
            PKEY = N + E
            pkey = (n, e)
            return PKEY, pkey, p, q


def encrypt(msg, pkey, r):
    m = bytes_to_long(msg)
    n, e = pkey
    c = pow(m, e, n)
    C = bin(c)[2:-r]
    return C, c


def decrypt(c, p, q, e):
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    m = pow(c, d, p * q)
    return long_to_bytes(m)


r, nbit = 8, 128
PKEY, pkey, p, q = keygen(nbit, r)
assert p * q == pkey[0]
print(f"PKEY = {int(PKEY, 2)}")
FLAG = flag.lstrip(b"CCTF{").rstrip(b"}")
enc, c = encrypt(FLAG, pkey, r)
print(decrypt(c, p, q, pkey[1]))
print(f"enc = {int(enc, 2)}")

n, e = pkey
print(f"{n=}")
print(f"{e=}")
N = bin(n)[2:-r]
E = bin(e)[2:-r]
print(PKEY)
print(f"{N=}")
print(f"{E=}")
