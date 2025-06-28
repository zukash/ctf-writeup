import numpy as np
from Crypto.Cipher import AES
from hashlib import sha256
from random import SystemRandom
import random
import sys

p = 65537
rand = SystemRandom()


def interpolate(xs: list[int], ys: list[int], x: int):
    n = len(xs)
    assert n == len(ys)
    res = 0
    for i in range(n):
        numer, denom = 1, 1
        for j in range(n):
            if i == j:
                continue
            numer *= x - xs[j]
            denom *= xs[i] - xs[j]
        res += ys[i] * numer * pow(denom, -1, p)
    return res % p


def recover(ct: bytes, shares: list, t: int):
    xs, ys = zip(*shares[:t])
    ks = [interpolate(xs, ys, x) for x in range(t)]
    key = sha256(repr(ks).encode()).digest()
    cipher = AES.new(key, AES.MODE_CTR, nonce=ct[:8])
    return cipher.decrypt(ct[8:])


# *******************************************
# sanity
# *******************************************
ct = b"*\x18\x11\x9c\xc9\x8d\x1e\xf1|S\x86P|\xab\n\\\xb1\x88\xd1"
shares = [
    (55287, 27494),
    (4995, 59677),
    (49424, 28404),
    (29968, 33207),
    (46413, 57547),
    (32025, 11762),
    (46988, 8446),
    (5128, 53096),
    (21613, 62420),
    (4010, 62697),
    (59979, 49382),
    (55786, 56618),
    (20475, 48034),
    (46241, 37053),
    (12481, 49367),
    (59833, 42764),
]
print(recover(ct, shares, 4))

xs, ys = zip(*shares[:4])
M = [[0] * 4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        M[i][j] += pow(xs[i], 3 - j, p)ko
print(M)

# *******************************************
# Broken
# *******************************************
ct = b"\xee\xaeS\xcc>\x1c\x8b\xc6\x88\xc6k5\xad\x16\xdf\xb1?wr"
shares = [
    (10662, 61322),
    (25751, 58512),
    (62801, 48740),
    (40498, 65252),
    (54686, 55642),
    (43107, 48014),
    (20506, 28810),
    (26032, 27439),
    (51803, 52670),
    (57818, 13108),
    (65386, 54732),
    (5991, 46176),
    (7542, 48602),
    (21166, 29884),
    (14429, 4843),
    (47076, 9122),
]
# print(recover(ct, shares, 4))
