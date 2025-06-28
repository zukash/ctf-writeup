import numpy as np
from Crypto.Cipher import AES
from hashlib import sha256
from random import SystemRandom
import sys
import random

p = 65537
rand = SystemRandom()


def share(secret: bytes, n: int, t: int):
    # (t, n) secret sharing
    poly = np.array([rand.randrange(0, p) for _ in range(t)])
    f = lambda x: int(np.polyval(poly, x) % p)

    xs = rand.sample(range(t, p), n)
    ys = [f(x) for x in xs]
    shares = [(int(x), int(y)) for x, y in zip(xs, ys)]

    ks = [f(x) for x in range(t)]
    key = sha256(repr(ks).encode()).digest()
    cipher = AES.new(key, AES.MODE_CTR)
    ct = cipher.nonce + cipher.encrypt(secret)
    return ct, shares, poly


def share_mod(secret: bytes, n: int, t: int):
    # (t, n) secret sharing
    poly = np.array([rand.randrange(0, p) for _ in range(t)])

    def f(x):
        y = 0
        for pv in poly:
            y = y * x + pv
            y %= p
        return y

    xs = rand.sample(range(t, p), n)
    ys = [f(x) for x in xs]
    shares = [(int(x), int(y)) for x, y in zip(xs, ys)]

    ks = [f(x) for x in range(t)]
    key = sha256(repr(ks).encode()).digest()
    cipher = AES.new(key, AES.MODE_CTR)
    ct = cipher.nonce + cipher.encrypt(secret)
    return ct, shares, poly


def calc(poly, xs):
    def f(x):
        y = 0
        for pv in poly:
            y = y * x + pv
            y %= p
        return y

    ys = [f(x) for x in xs]
    shares = [(int(x), int(y)) for x, y in zip(xs, ys)]

    return ys, shares


def interpolate(xs: list[int], ys: list[int], x: int):
    n = len(xs)
    assert n == len(ys)
    res = 0
    for i in range(n):
        numer, denom = 1, 1
        for j in range(n):
            if i == j:
                continue
            numer *= x - xs[j]
            denom *= xs[i] - xs[j]
        res += ys[i] * numer * pow(denom, -1, p)
    return res % p


def recover(ct: bytes, shares: list, t: int):
    xs, ys = zip(*shares[:t])
    ks = [interpolate(xs, ys, x) for x in range(t)]
    key = sha256(repr(ks).encode()).digest()
    cipher = AES.new(key, AES.MODE_CTR, nonce=ct[:8])
    return cipher.decrypt(ct[8:])


def sanity_check():
    message = b"hello world"
    ct, shares = share(message, 16, 4)
    assert recover(ct, shares, 4) == message


# **************************************
# 何が起こっているか調べる
# **************************************
message = b"hello world"
# while True:
#     ct, shares = share_mod(message, 4, 4)
#     print(ct)
#     print(shares)
#     assert recover(ct, shares, 4) == message
# この関数で overflow するときに壊れる
# f = lambda x: int(np.polyval(poly, x) % p)
# 真の値とのズレはどれくらいだろうか

# **************************************
# np.polyval は何者か
# **************************************
assert np.polyval([1, 2, 3], 4) == 1 * 4**2 + 2 * 4 + 3
# overflow の再現
x = np.polyval(np.array([1, 0, 0]), 10**9)
print(x)  # 1000000000000000000
x = np.polyval(np.array([1, 0, 0]), 10**10)
print(x)  # 7766279631452241920
assert x == 10**20 % (1 << 64)

# **************************************
# x % (1 << 64) % 65537 の計算
# **************************************
# x = (1 << 64) * q + r
#   = q' * 65537 + (q + r)
# x -> (x // (1 << 64)) + (x % 65537)
#   -> (x // (1 << 128)) + (x // (1 << 64) % 65537) + (x % 65537)
# ざっくり言うと*、64 bit 区切りで mod 65537 の和を取っている
# *: 今回の制約下では成立する（最終的な和が 1 << 64 を超えないので）


# つまり、1 << 64 進数で考えて、桁ごとの mod 65537 の和を取れば十分
def int2base(n, base):
    res = []
    while n:
        res.append(n % base)
        n //= base
    return res[::-1]


# **************************************
# やりなおし：x % (1 << 64) % 65537 の計算
# **************************************
# なんかそれっぽいこと言っているけれど、今回の話とは関係なかったのでやりなおし
# f(x) = (sum c_i * x^i) % (1 << 64) % 65537
# に対して、xs と f(xs) が与えられているとき、c_i を計算したい
# f(xi) = (sum c_i * xi^i) % (1 << 64) % 65537
# xi^i % (1 << 64) を事前に計算しておく
# 今回の制約では f(xi) の bit 数は 85 くらいなので
# f'(x) = (sum c_i * (x^i % (1 << 64)) % 65537
# との差が

x = random.randint(0, 1 << 64)
y = random.randint(0, 1 << 16)
expected = (x * y) % (1 << 64) % 65537
# expected = (x) % (1 << 64) % 65537
base8 = int2base(x, 1 << 16)
print(f"{x = }")
print(f"{base8 = }")
print(f"{y = }")
print(f"{expected = }")
a, b, c, d = base8
print(y * (d - c + b - a) % 65537)
print((x * y) // (1 << 64))
