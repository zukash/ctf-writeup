from Crypto.Util.number import *
from Crypto.Cipher import AES
from hashlib import sha256
from itertools import combinations, product
import secrets
import random


from pwn import *

io = remote("chals.sekai.team", "3005")
# io = process(["python", "chall.mod.py"])


def send_poly(p):
    io.recvuntil(b"Give me your generator polynomial:")
    io.sendline(str(poly2bin(p)).encode())
    return eval(io.recvline())


def bin2poly(b):
    p = 0
    for i in range(b.bit_length()):
        if b >> i & 1:
            p += x ** i
    return p


def poly2bin(p):
    b = 0
    for i, x in enumerate(p.list()):
        if x:
            b += 1 << i
    return b

def getCRC16(msg, gen_poly):
    assert (1 << 16) <= gen_poly < (1 << 17)  # check if deg = 16
    msglen = msg.bit_length()
    msg <<= 16
    for i in range(msglen - 1, -1, -1):
        if (msg >> (i + 16)) & 1:
            msg ^^= gen_poly << i

    return msg



x = polygen(Zmod(2), "x")
target = bin2poly(secrets.randbits(512))
io.recvuntil(b"Encrypted flag:")
enc_flag = bytes.fromhex(io.recvline().strip().decode())

# M8 = []
# for bit in range(1 << 8, 1 << 9):
#     if bin2poly(bit).is_irreducible():
#         M8.append(bin2poly(bit))

M8 = []
for bit in range(1 << 8, 1 << 9):
    M8.append(bin2poly(bit))

S = set()
T = set()
A16, M16 = [], []
while len(M16) < 246:
    m0, m1, m2 = random.sample(M8, 3)
    if m0 in S or m1 in S or m2 in S:
        continue
    S.add(m0)
    S.add(m1)
    S.add(m2)
    if m0 * m1 in T or m1 * m2 in T or m2 * m0 in T:
        continue
    T.add(m0 * m1)
    T.add(m1 * m2)
    T.add(m2 * m0)

    # r0 = target % (m0 * m1)
    # r1 = target % (m1 * m2)
    # r2 = target % (m2 * m0)

    # res0 = [secrets.randbits(16) for _ in range(3)]
    # res0[secrets.randbelow(3)] = poly2bin(r0)
    # res1 = [secrets.randbits(16) for _ in range(3)]
    # res1[secrets.randbelow(3)] = poly2bin(r1)
    # res2 = [secrets.randbits(16) for _ in range(3)]
    # res2[secrets.randbelow(3)] = poly2bin(r2)
    res0 = send_poly(m0 * m1)
    res1 = send_poly(m1 * m2)
    res2 = send_poly(m2 * m0)

    A, M = [], []
    for r0, r1, r2 in product(res0, res1, res2):
        r0, r1, r2 = map(bin2poly, [r0, r1, r2])

        c0 = r0 % m1 == r1 % m1
        c1 = r1 % m2 == r2 % m2
        c2 = r2 % m0 == r0 % m0

        if c0 and c1 and c2:
            A16 += [r0, r1, r2]
            M16 += [m0 * m1, m1 * m2, m2 * m0]
    print(len(A16))


key = CRT(A16, M16)
print(key)
key = poly2bin(key)
key >>= 16
print(key)

cipher = AES.new(
    sha256(long_to_bytes(key)).digest()[:16], AES.MODE_CTR, nonce=b"12345678"
)
flag = cipher.decrypt(enc_flag)
print(enc_flag)
print(flag)
# for a, m in zip(A16, M16):
#     print(target % m)
#     print(a)
#     assert target % m == a
# print(A16)
# print(M16)

# A = []
# for m in M16:
#     assert m.is_irreducible()
#     a = target % m
#     A.append(a)
# A.pop()
# A.append(bin2poly(secrets.randbits(16)))

# print(len(M16))
# print(target)
# print(CRT(A16, M16))
# assert target == CRT(A16, M16)
