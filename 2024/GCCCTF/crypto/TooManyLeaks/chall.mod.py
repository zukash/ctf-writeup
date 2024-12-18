#!/usr/bin/env python3

from Crypto.Util.number import getStrongPrime
import hashlib
from secret import flag
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def encrypt_flag(secret_key):
    sha1 = hashlib.sha1()
    sha1.update(str(secret_key).encode("ascii"))
    key = sha1.digest()[:16]
    iv = os.urandom(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(flag, 16))
    print("{ ciphertext : " + ciphertext.hex() + ", iv : " + iv.hex() + "}")

    return ciphertext, iv


# Generate parameters

p = getStrongPrime(512)
print(f"{p=}")
g = 2

# Alice calculates the public key A
a = getStrongPrime(512)
A = pow(g, a, p)
print(f"{A=}")

# Bob calculates the public key B
b = getStrongPrime(512)
B = pow(g, b, p)
print(f"{B=}")

# Calculate the secret key
s = pow(B, a, p)

# What ?!
mask = ((1 << 256) - 1 << 256) + (1 << 255)
assert bin(mask)[2:] == "1" * 257 + "0" * 255
r1 = s & mask
print(f"{r1=}")

# Charlie arrives and sync with Alice and Bob
c = getStrongPrime(512)
print(f"{c=}")
AC = pow(g, a + c, p)
s2 = pow(AC, b, p)
print(f"{AC=}")
r2 = s2 & mask
print(f"{r2=}")

encrypt_flag(s)

# ***************************************************

# B**c は完全に分かっている
assert s * pow(B, c, p) % p == s2

# print((s * pow(B, c, p)).bit_length())

# ***************************************************

from z3 import *
from Crypto.Util.number import long_to_bytes

solver = Solver()
h0 = BitVec("h0", 512)
h1 = BitVec("h1", 512)
solver.add(h0 * pow(B, c, p) == h1)
for i in range(255):
    solver.add(Extract(i + 255, i + 255, h0) == ((s >> (i + 255)) & 1))
for i in range(255):
    solver.add(Extract(i + 255, i + 255, h1) == ((s2 >> (i + 255)) & 1))
print(solver)
print(bin(s))

if solver.check():
    print("SAT")
    m = solver.model()
    print(m)
else:
    print("UNSAT")
