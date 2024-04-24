#!/usr/bin/env python3

from Crypto.Util.number import *
from flag import flag

from decimal import *


def keygen(nbit, r):
    while True:
        p, q = [getPrime(nbit) for _ in "__"]
        d, n = getPrime(64), p * q
        phi = (p - 1) * (q - 1)
        if GCD(d, phi) == 1:
            e = inverse(d, phi)
            N = bin(n)[2:-r]
            E = bin(e)[2:-r]
            PKEY = N + E
            pkey = (n, e)
            print(f"{d=}")
            return PKEY, pkey


def encrypt(msg, pkey, r):
    m = bytes_to_long(msg)
    n, e = pkey
    c = pow(m, e, n)
    C = bin(c)[2:-r]
    return C


r, nbit = 8, 1024
PKEY, pkey = keygen(nbit, r)
print(f"PKEY = {int(PKEY, 2)}")
n, e = pkey
print(f"{n.bit_length()=}")
assert n.bit_length() == nbit * 2
PKEY = int(PKEY, 2)
assert f"{PKEY:b}"[: nbit * 2 - r] == bin(n)[2:-r]
assert f"{PKEY:b}"[nbit * 2 - r :] == bin(e)[2:-r]
FLAG = flag.lstrip(b"CCTF{").rstrip(b"}")
enc = encrypt(FLAG, pkey, r)
print(f"enc = {int(enc, 2)}")


##############################################################


def solve(e, n):
    cf = continued_fraction(e / n)
    cand = []
    for conv in cf.convergents():
        k = conv.numerator()
        d = conv.denominator()
        if k == 0:
            continue
        # d * e = k * (n - p - q + 1) + 1
        # p + q = n - (d * e - 1) / k + 1
        pq = n - (d * e - 1) / k + 1
        if not pq.is_integer():
            continue
        # (x - p) * (x - q) = 0 の解が p,q
        # x^2 - (p + q) * x + n = 0 の解が p,q
        cand.append(d)

        # x = var("x")
        # f = x ^ 2 - pq * x + n
        # sol = f.roots()
        # if len(sol) != 2:
        #     continue
        # p, q = sol[0][0], sol[1][0]
        # if not (p.is_integer() and q.is_integer()):
        #     continue
        # if not (is_prime(p) and is_prime(q)):
        #     continue
        # return p, q, d
    return cand


enc = int(enc, 2)
cand = solve(e, n)
for d in cand:
    print(d)
    flag = long_to_bytes(pow(enc, d, n))
    try:
        flag = flag.decode()
        print(f"{flag=}")
    except:
        pass
