#!/usr/bin/env python3

from Crypto.Util.number import getPrime, bytes_to_long

with open("flag.txt", "rb") as f:
    flag = f.read()


n1 = getPrime(512) * getPrime(512)
n2 = getPrime(512) * getPrime(512)
n3 = getPrime(512) * getPrime(512)

e = 3

m = bytes_to_long(flag)

c1 = pow(m, e, n1)
c2 = pow(m, e, n2)
c3 = pow(m, e, n3)

print(f"n1: {n1}")
print(f"e: {e}")
print(f"c1: {c1}")
print(f"n2: {n2}")
print(f"e: {e}")
print(f"c2: {c2}")
print(f"n3: {n3}")
print(f"e: {e}")
print(f"c3: {c3}")
