from os import urandom
from random import getrandbits

from Crypto.Util.number import *

# from secret import flag, seed

cipher = 38366804914662571886103192955255674055487701488717997084670307464411166461113108822142059


class LFSR:
    def __init__(self):
        self.bits = 128
        self.rr = seed
        self.switch = 0

    def next(self):
        r = self.rr
        if self.switch == 0:
            b = (
                ((r >> 0) & 1)
                ^ ((r >> 2) & 1)
                ^ ((r >> 4) & 1)
                ^ ((r >> 6) & 1)
                ^ ((r >> 9) & 1)
            )
        if self.switch == 1:
            b = ((r >> 1) & 1) ^ ((r >> 5) & 1) ^ ((r >> 7) & 1) ^ ((r >> 8) & 1)
        r = (r >> 1) + (b << (self.bits - 1))
        self.rr = r
        self.switch = 1 - self.switch
        return r & 1

    def gen_randbits(self, bits):
        key = 0
        for i in range(bits):
            key <<= 1
            key += self.next()
        return key


# neko = urandom(ord("🐈") * ord("🐈") * ord("🐈"))
# key = lfsr.gen_randbits(len(neko) * 8)
# cipher = bytes_to_long(neko) ^ key

#   📄🐈💨💨💨💨
# ╭─^────────╮
# │  cipher  │
# ╰──────────╯

# len(flag) で全探索
for i in range(5, 200):
    # nekoの後のseed
    seed = 29737358075939491758658879020535321832
    lfsr = LFSR()

    key = lfsr.gen_randbits(i * 8)
    flag = cipher ^ key
    flag = long_to_bytes(flag)
    if b"ctf" in flag:
        print(flag)
