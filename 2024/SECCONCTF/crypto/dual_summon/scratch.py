from sage.all import *
from Crypto.Cipher import AES
import secrets
from pwn import xor

key = b"A" * 16
nonce = b"B" * 16

R = PolynomialRing(GF(2), "x")
x = R.gen()
F = GF(2**128, "a", modulus=x**128 + x**7 + x**2 + x + 1)
a = F.gen()
PR = PolynomialRing(F, "x")
x = PR.gen()


# def bytes_to_poly(b):
#     v = int.from_bytes(b, "big")
#     v = int(f"{v:0128b}"[::-1], 2)
#     return F.fetch_int(v)


# def poly_to_bytes(p):
#     v = p.integer_representation()
#     v = int(f"{v:0128b}"[::-1], 2)
#     return v.to_bytes(16, "big")


def to_poly(x):
    bs = Integer(int.from_bytes(x, "big")).bits()[::-1]
    return F([0] * (128 - len(bs)) + bs)


def to_bytes(poly):
    return int(bin(poly.integer_representation())[2:].zfill(128)[::-1], 2).to_bytes(
        16, "big"
    )


assert to_bytes(to_poly(b"asdfasdfasdfasdf")) == b"asdfasdfasdfasdf"


keys = [secrets.token_bytes(16) for _ in range(2)]
nonce = secrets.token_bytes(16)


def summon(number, plaintext):
    assert len(plaintext) == 16
    aes = AES.new(key=keys[number - 1], mode=AES.MODE_GCM, nonce=nonce)
    _, tag = aes.encrypt_and_digest(plaintext)
    return tag


P0 = b"X" * 16
P1 = b"Y" * 16
P2 = b"Z" * 16
P01 = xor(P0, P1)
P02 = xor(P0, P2)

tag0 = summon(1, P0)
tag1 = summon(1, P1)
tag2 = summon(1, P2)
tag01 = summon(1, P01)
tag02 = summon(1, P02)

assert xor(tag01, tag1) == xor(tag02, tag2)
assert xor(tag01, xor(tag0, tag1)) == xor(tag02, xor(tag0, tag2))

diff_a = xor(tag01, xor(tag0, tag1))
ha = to_poly(xor(tag0, diff_a)) / to_poly(P0)


# p0 = to_poly(P0)
# f = p0 * x**3 + p0 * x**2 + to_poly(xor(tag0, tag1))
# print(f.roots())
# h = f.roots()[0][0]

# p1 = to_poly(P1)
# assert to_poly(xor(tag01, tag0)) == p1 * h**3 + p1 * h**2


# # tag0 = summon(1, b"X" * 16)
# tag0 = summon(1, b"\x00" * 16)

# print(tag0)


# tag1 = summon(2, tag0)
# tag2 = summon(1, tag1)
# print(tag1)

# assert summon(1, tag2) == summon(2, tag2)

# tag2 = summon(1, b"Z" * 16)
# tag3 = summon(2, b"Z" * 16)

# t0 = bytes_to_poly(tag0)
# t1 = bytes_to_poly(tag1)

# t2 = bytes_to_poly(tag2)
# t3 = bytes_to_poly(tag3)

# S = set()
# for x in range(256):
#     tag0 = summon(1, bytes([x] * 16))
#     tag1 = summon(2, bytes([x] * 16))
#     t0 = bytes_to_poly(tag0)
#     t1 = bytes_to_poly(tag1)
#     S.add(t0 * t1)

# print(len(S))

# # assert t0 + t1 == t2 + t3
