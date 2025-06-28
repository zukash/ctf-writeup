import random

from z3 import *

set_param(verbose=10)
set_param("parallel.enable", True)


N = 624
M = 397
MATRIX_A = 0x9908B0DF
UPPER_MASK = 0x80000000
LOWER_MASK = 0x7FFFFFFF


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


# check
for i in range(100):
    random.seed(i)
    assert random_seed(i) == list(random.getstate()[1][:N])
i = 2**64 + 2**32 + 2**16
random.seed(i)
assert random_seed(i) == list(random.getstate()[1][:N])


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


def rand_int_0_2(n, seed):
    mt = random_seed(seed)
    update_mt(mt)
    my_rands = []
    i = 0
    while True:
        if len(my_rands) == n:
            break
        while True:
            tmp_rand = temper(mt[i]) >> 30
            if tmp_rand <= 2:
                break
            i += 1
            if i >= N:
                i -= N
                update_mt(mt)
        my_rands.append(tmp_rand)
        i += 1
        if i >= N:
            i -= N
            update_mt(mt)
    return my_rands


def getrandbits_32(n, seed):
    mt = random_seed(seed)
    update_mt(mt)
    i = 0
    my_rands = []
    while True:
        if len(my_rands) == n:
            break
        tmp_rand = temper(mt[i])
        i += 1
        if i >= N:
            i -= N
            update_mt(mt)
        my_rands.append(tmp_rand)
    return my_rands


def getrandbits_1(n, seed):
    mt = random_seed(seed)
    update_mt(mt)
    i = 0
    my_rands = []
    while True:
        if len(my_rands) == n:
            break
        tmp_rand = temper(mt[i]) >> 31
        i += 1
        if i >= N:
            i -= N
            update_mt(mt)
        my_rands.append(tmp_rand)
    return my_rands


# *******************************************
# 動作確認
# *******************************************
random.seed(1337)
rands = [random.randint(0, 2) for _ in range(N)]
my_rands = rand_int_0_2(N, 1337)
assert my_rands == rands


random.seed(1337)
rands = [random.getrandbits(32) for _ in range(N)]
my_rands = getrandbits_32(N, 1337)
assert my_rands == rands


random.seed(1337)
rands = [random.getrandbits(1) for _ in range(N)]
my_rands = getrandbits_1(N, 1337)
assert my_rands == rands

# *******************************************
# 内部状態 復元
# *******************************************
random.seed(1337)
print(random.getstate())
rands = [random.getrandbits(32) for _ in range(N)]

state = [BitVec(f"state_{i}", 32) for i in range(N)]
_state = state.copy()

update_mt(state)

s = Solver()
my_rands = []
i = 0
while True:
    if len(my_rands) == N:
        break
    tmp_rand = temper(state[i])
    i += 1
    if i >= N:
        i -= N
        update_mt(state)
    my_rands.append(tmp_rand)

for i in range(N):
    s.add(my_rands[i] == rands[i])
s.add(_state[0] == 0x80000000)
s.check()
m = s.model()
print([m[s].as_long() for s in _state])

random.seed(1337)
print(random.getstate())
rands = [random.getrandbits(1) for _ in range(N * 32)]

# state = [BitVec(f"state_{i}", 32) for i in range(N)]
# _state = state.copy()

# update_mt(state)

# s = Solver()
# my_rands = []
# i = 0
# while True:
#     if len(my_rands) == N * 32:
#         break
#     tmp_rand = LShR(temper(state[i]), 31)
#     i += 1
#     if i >= N:
#         i -= N
#         update_mt(state)
#     my_rands.append(tmp_rand)

# for i in range(N * 32):
#     s.add(my_rands[i] == rands[i])
# s.check()
# m = s.model()

# mt_state = [m[s].as_long() for s in _state]
# print(mt_state)

# random.setstate((3, tuple(mt_state + [624]), None))
# predict_rands = [random.getrandbits(1) for _ in range(N * 32)]
# assert predict_rands == rands


# *******************************************
# seed 復元
# *******************************************
