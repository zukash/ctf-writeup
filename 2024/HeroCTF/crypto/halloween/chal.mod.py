#!/usr/bin/env python3
from z3 import *
import gostcrypto
import os
from gostcrypto.gostcipher.gost_34_13_2015 import GOST34132015ctr

with open("flag.txt", "rb") as f:
    flag = f.read()

# key, iv = os.urandom(32), os.urandom(8)
key = b"\x1d\x92\x0ct`{\xa1\x92\xe5F\x94F\xba\xda\x1c\x9co\x9a\x12\xcc\xdf\xc7\x02\xbeU\x13\x11WL\xe0r\xbd"
iv = b"?K\x9cu\x08w\x89!"

cipher = gostcrypto.gostcipher.new(
    "kuznechik", key, gostcrypto.gostcipher.MODE_CTR, init_vect=iv
)

key = [BitVec(f"byte_{i}", 8) for i in range(32)]
iv = [BitVec(f"byte_{i}", 8) for i in range(8)]

cipher1 = GOST34132015ctr("kuznechik", key, init_vect=iv)


print(f"It's almost Halloween, time to get sp00{cipher.encrypt(flag).hex()}00ky 👻!")
cipher1.encrypt(flag)

while True:
    x = input()
    print(cipher.encrypt(bytes.fromhex(x)).hex())
    print(cipher1.encrypt(bytes.fromhex(x)).hex())
