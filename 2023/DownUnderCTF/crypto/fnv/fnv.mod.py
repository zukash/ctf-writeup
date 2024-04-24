#!/usr/bin/env python3

import os
from math import gcd

from Crypto.Util.number import *


def fnv1(s):
    h = 0xCBF29CE484222325
    for b in s:
        h *= 0x00000100000001B3
        h &= 0xFFFFFFFFFFFFFFFF
        h ^= b
        print(hex(h))
    return h


def invfnv1(h, s):
    print(s)
    for b in s[::-1]:
        h ^= b
        h &= 0xFFFFFFFFFFFFFFFF
        h *= pow(0x00000100000001B3, -1, 0xFFFFFFFFFFFFFFFF + 1)
        h &= 0xFFFFFFFFFFFFFFFF
        print(hex(h))
    assert h == 0xCBF29CE484222325
    return h


TARGET = 0x1337133713371337

print("Welcome to FNV!")
print(f"Please enter a string in hex that hashes to 0x{TARGET:016x}:")
s = bytearray.fromhex(input())
if fnv1(s) == TARGET:
    print("Well done!")
    print(os.getenv("FLAG"))
else:
    print("Try again... :(")

print()
fs = fnv1(s)
print()
invfnv1(fs, s)

print()
print(fnv1(long_to_bytes(fnv1(s))))


def fnv1_mod(s):
    h = 0xCBF29CE484222325
    res = []
    for b in s:
        h *= 0x00000100000001B3
        h &= 0xFFFFFFFFFFFFFFFF
        h ^= b
        if h == TARGET:
            print("OK")
        res.append(h)
    return res


print(fnv1_mod(b"\x00" * 3))

s = 0xCBF29CE484222325
m = 0xFFFFFFFFFFFFFFFF + 1
b = 0x00000100000001B3
print([s * pow(b, i, m) % m for i in range(10)])

