#!/usr/bin/env python3

from collections import Counter
from random import shuffle
from Crypto.Util.number import getPrime


FLAG = b"dummy{flag}"

assert len(FLAG) < 100

encoded_flag = []

for i, b in enumerate(FLAG):
    encoded_flag.extend([i + 0x1337] * b)

shuffle(encoded_flag)

e = 65537
p, q = getPrime(1024), getPrime(1024)
n = p * q
c = sum(pow(m, e, n) for m in encoded_flag) % n

print(f"{n = }")
print(f"{e = }")
print(f"{c = }")

d = 0
for k, v in Counter(encoded_flag).items():
    d += pow(k, e, n) * v
assert c == d % n

# a0 * v0 + a1 * v1 + ... + an * vn == c (mod n)
# a0 * v0 + a1 * v1 + ... + an * vn + kn == c
# (a0, a1, ..., an, c, n) * (v0, v1, ..., vn, -1, k) == 0
