from itertools import cycle
from pwn import *
import random
from typing import Counter
from Crypto.Cipher import AES
import time
import os
from flag import flag

m = 288493873028852398739253829029106548736

a = int(time.time())

b = a % 16

s = random.randint(1, m - 1)

index = 0


class LCG:
    def __init__(self, a, b, m, seed):
        self.a = a
        self.b = b
        self.m = m
        self.state = seed
        self.counter = 0

    def next_state(self):
        ret = self.state
        self.state = (self.a * self.state + self.b) % self.m
        return ret


class SuperAES:
    def __init__(self, key, lcg):
        self.aes = AES.new(key, AES.MODE_ECB)
        self.lcg = lcg

    def encrypt(self, plaintext):
        ciphertext = b""
        for i in range(0, len(plaintext), 16):
            ciphertext += self.encrypt_block(plaintext[i : i + 16])

        return ciphertext

    def encrypt_block(self, block):
        global index
        index += 1
        keystream = self.aes.encrypt(int(self.lcg.next_state()).to_bytes(16, "big"))
        print(index)
        print(f"{keystream.hex() = }")
        print(f"{block = }")
        print(f"cipher = {bytes([k ^ b for k, b in zip(keystream, block)])}")
        print()
        return bytes([k ^ b for k, b in zip(keystream, block)])


assert len(flag) == 33
assert flag.startswith(b"GCC{")

# key = os.urandom(32)

# cipher = SuperAES(key, LCG(a, b, m, s))

# times = int(input("how many times do you want the flag ?"))

# assert times < 50

# print(cipher.encrypt(flag * times).hex())

# ************************************************************************

print(f"{m = }")
print(f"{a = }")
print(f"{b = }")
print(f"{s = }")
# print(f"{key = }")
# print(f"encrypted = {cipher.encrypt(flag * times)}")

# NOTE: 16回に一回くらいLCG周期が非常に小さいものがある
# for a in range(1709344090, 1709344090 + 160):
#     b = a % 16

#     s = random.randint(1, m - 1)

#     lcg = LCG(a, b, m, s)
#     S = [lcg.next_state()]
#     while True:
#         x = lcg.next_state()
#         if len(S) > 300:
#             break
#         if x in S:
#             S = S[S.index(x) :]
#             break
#         S.append(x)

#     print(a, b, len(set(S)))


# ************************************************************************


a = 1709344224
b = a % 16
s = random.randint(1, m - 1)

lcg = LCG(a, b, m, s)
S = [lcg.next_state() for _ in range(100)]

key = os.urandom(32)
cipher = SuperAES(key, LCG(a, b, m, s))
times = 49
ct = cipher.encrypt(flag * times)
print(len(ct))

# keystream = b""
# for i in range(49):
#     left = (i - 1) % 32 + 32 * i
#     # left = i - 1 + 32 * i
#     chunk = xor(ct[left : left + 5], b"}GCC{")
#     keystream += chr(chunk[0]).encode()

# loop = 33 * 16
# first = ct[:loop]
# second = ct[loop : loop * 2]
# third = ct[loop * 2 : loop * 3]
# print(first)
# print(second)
# print(third)
# print(len(first))
# print(len(second))
# print(len(third))

# keystream = xor(third[:4], b"GCC{")[:3]
# print(keystream)
# for i in range(0, len(third), 32):
#     left = i + i // 32
#     print(left)
#     print(third[left : left + 4])
#     chunk = xor(third[left : left + 4], b"GCC{")
#     # assert keystream[-3:] == chunk[:3]
#     keystream += chunk[3:]
#     print(chunk.hex())
# keystream = keystream[:16]
# print(keystream.hex())

# # keystream = xor(ct[32 : 32 + 5], b"}GCC{") + b"\x00" * 11
# # print(keystream)
# # pt = bytes([k ^ b for k, b in zip(ct, cycle(keystream))])
# # for i in range(0, len(pt), 32):
# #     print(pt[i : i + 32].hex())
# # print(len(set(S)))


# for i in range(0, len(pt), 32):
#     print(ct[i : i + 32].hex())
