#!/usr/bin/env python3
from os import getenv as getenv
from hashlib import md5 as md5


def my_func(arg):
    my_md5 = md5()
    res = bytes([0] * 16)
    for c in arg:
        my_md5.update(bytes([c]))
        res = bytes([a ^ b for a, b in zip(res, my_md5.digest())])
        print(res)
    return res


print("hhh hhh hhhh hhh hhhhh hhhh hhhh hhhhh hhhh hh hhhhhh hhhh?")

inp = bytes.fromhex(input("inp: "))

if my_func(inp) == b"hhhhhhhhhhhhhhhh":
    print("[OK] hhhh hhhh, hhhh hh hhhh hhhh:", getenv("FLAG"))
else:
    print("[NG] hhhhh, hhh hhhhh!")
