"""
ref. https://blog.y011d4.com/20221113-seccon-ctf-writeup#janken-vs-kurenaif
ref. https://github.com/idekctf/idekctf-2024/tree/main/crypto/seedy
ref. https://github.com/tna0y/Python-random-module-cracker
ref. https://inaz2.hatenablog.com/entry/2016/03/07/194147

TODO:
* randbits(32) x 624 → seed
"""

from z3 import *

N = 624


def random_seed(seed):
    init_key = []
    if isinstance(seed, int):
        while seed != 0:
            init_key.append(seed % 2**32)
            seed //= 2**32
    else:
        init_key = seed
    key = init_key if len(init_key) > 0 else [0]
    keyused = len(init_key) if len(init_key) > 0 else 1
    return init_by_array(key, keyused)


def init_by_array(init_key, key_length):
    s = 19650218
    mt = [0] * N
    mt[0] = s
    for mti in range(1, N):
        if isinstance(mt[mti - 1], int):
            mt[mti] = (1812433253 * (mt[mti - 1] ^ (mt[mti - 1] >> 30)) + mti) % 2**32
        else:
            mt[mti] = 1812433253 * (mt[mti - 1] ^ LShR(mt[mti - 1], 30)) + mti
    i = 1
    j = 0
    k = N if N > key_length else key_length
    while k > 0:
        if isinstance(mt[i - 1], int):
            mt[i] = (
                (mt[i] ^ ((mt[i - 1] ^ (mt[i - 1] >> 30)) * 1664525)) + init_key[j] + j
            ) % 2**32
        else:
            mt[i] = (
                (mt[i] ^ ((mt[i - 1] ^ LShR(mt[i - 1], 30)) * 1664525))
                + init_key[j]
                + j
            )
        i += 1
        j += 1
        if i >= N:
            mt[0] = mt[N - 1]
            i = 1
        if j >= key_length:
            j = 0
        k -= 1
    for k in range(1, N)[::-1]:
        if isinstance(mt[i - 1], int):
            mt[i] = (
                (mt[i] ^ ((mt[i - 1] ^ (mt[i - 1] >> 30)) * 1566083941)) - i
            ) % 2**32
        else:
            mt[i] = (mt[i] ^ ((mt[i - 1] ^ LShR(mt[i - 1], 30)) * 1566083941)) - i
        i += 1
        if i >= N:
            mt[0] = mt[N - 1]
            i = 1
    mt[0] = 0x80000000
    return mt


def update_mt(mt):
    N = 624
    M = 397
    MATRIX_A = 0x9908B0DF
    UPPER_MASK = 0x80000000
    LOWER_MASK = 0x7FFFFFFF
    for kk in range(N - M):
        y = (mt[kk] & UPPER_MASK) | (mt[kk + 1] & LOWER_MASK)
        if isinstance(y, int):
            mt[kk] = mt[kk + M] ^ (y >> 1) ^ (y % 2) * MATRIX_A
        else:
            mt[kk] = mt[kk + M] ^ LShR(y, 1) ^ (y % 2) * MATRIX_A
    for kk in range(N - M, N - 1):
        y = (mt[kk] & UPPER_MASK) | (mt[kk + 1] & LOWER_MASK)
        if isinstance(y, int):
            mt[kk] = mt[kk + (M - N)] ^ (y >> 1) ^ (y % 2) * MATRIX_A
        else:
            mt[kk] = mt[kk + (M - N)] ^ LShR(y, 1) ^ (y % 2) * MATRIX_A
    y = (mt[N - 1] & UPPER_MASK) | (mt[0] & LOWER_MASK)
    if isinstance(y, int):
        mt[N - 1] = mt[M - 1] ^ (y >> 1) ^ (y % 2) * MATRIX_A
    else:
        mt[N - 1] = mt[M - 1] ^ LShR(y, 1) ^ (y % 2) * MATRIX_A


def temper(state):
    y = state
    if isinstance(y, int):
        y ^= y >> 11
    else:
        y ^= LShR(y, 11)
    y ^= (y << 7) & 0x9D2C5680
    y ^= (y << 15) & 0xEFC60000
    if isinstance(y, int):
        y ^= y >> 18
    else:
        y ^= LShR(y, 18)
    return y


def getrandbits32(mt):
    mt = mt.copy()
    update_mt(mt)
    i = 0
    while True:
        yield temper(mt[i])
        i += 1
        if i >= N:
            i -= N
            update_mt(mt)


# ======

from random import getrandbits
from Crypto.Cipher import AES
from hashlib import sha256

danger = 624 * 32  # i hear you need this much.
given = []
key = ""
# for _ in range(danger // 20 - 16):  # should be fine if im only giving u this much :3
#     x = getrandbits(32)
#     # we share <3
#     key += str(x % 2**12)
#     given.append(x >> 12)

for _ in range(danger // 32):  # should be fine if im only giving u this much :3
    x = getrandbits(32)
    given.append(x)

my_seed = [BitVec(f"seed_{i}", 32) for i in range(danger // 32)]
mt = random_seed(my_seed)
s = Solver()
for i in range(danger // 32):  # should be fine if im only giving u this much :3
    x = next(getrandbits32(mt))
    s.add(x == given[i])

# print(s)
print(s.check())

m = s.model()
my_seed = [m[s].as_long() for s in my_seed]

my_seed_int = 0
for s in my_seed[::-1]:
    my_seed_int *= 2**32
    my_seed_int += s
