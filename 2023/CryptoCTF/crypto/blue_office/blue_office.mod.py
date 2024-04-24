#!/usr/bin/enc python3

import binascii
from secret import seed, flag


def gen_seed(s):
    i, j, k = 0, len(s), 0
    while i < j:
        k = k + ord(s[i])
        i += 1
    i = 0
    while i < j:
        if (i % 2) != 0:
            k = k - (ord(s[i]) * (j - i + 1))
        else:
            k = k + (ord(s[i]) * (j - i + 1))

        k = k % 2147483647
        i += 1

    k = (k * j) % 2147483647
    return k


def reseed(s):
    return s * 214013 + 2531011


def encrypt(s, msg):
    assert s <= 2 ** 32
    c, d = 0, s
    enc, l = b"", len(msg)
    while c < l:
        d = reseed(d)
        print(d)
        enc += (msg[c] ^ ((d >> 16) & 0xFF)).to_bytes(1, "big")
        c += 1
    return enc


enc = encrypt(seed, flag)
print(enc)
print(f"enc = {binascii.hexlify(enc)}")

msg = encrypt(seed, enc)
print(msg)

# enc = b"\x0e\xbf\x0c:mB\xe6\x8b\xa0\x1a\x8a\xa0T\xd8\x02\x97"
enc = b"0ebf0c3a6d42e68ba01a8aa054d80297"
enc = bytes.fromhex(enc.decode())
print(encrypt(12, enc))
