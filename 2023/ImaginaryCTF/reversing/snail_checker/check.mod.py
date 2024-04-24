#!/usr/bin/env python3


# def f(A):
#     c, i = 0, 0
#     while len([n for n in A if n != 0]) > 1:
#         i %= len(A)
#         if A[i] != 0 and c == 1:
#             A[i], c = 0, 0
#         if A[i] != 0:
#             c += 1
#         i += 1
#         # print([f"{a:05b}" for a in A])
#     return sum(A)


from itertools import product

import tqdm


def f(n):
    bl = n.bit_length()
    i = n - (1 << (bl - 1))
    return 2 * i


"""
観察結果：
f(2 ** n) == 1
f(2 ** n + i) == 1 + 2 * i
"""


# for i in range(1, 1000):
#     print(f"OK: {i}")
#     assert f(list(range(1, i + 1))) == f_(i)
# → OK

# def enc(b):
#     a = [n for n in range(b[0] * 2 ** 24 + b[1] * 2 ** 16 + b[2] * 2 ** 8 + b[3] + 1)][
#         1:
#     ]
#     c, i = 0, 0
#     while len([n for n in a if n != 0]) > 1:
#         i %= len(a)
#         if a[i] != 0 and c == 1:
#             a[i], c = 0, 0
#         if a[i] != 0:
#             c += 1
#         i += 1
#     return sum(a)


def enc(b):
    v = b[0] * 2 ** 24 + b[1] * 2 ** 16 + b[2] * 2 ** 8 + b[3]
    # print(v.bit_length())
    # # → 31
    # print(hex(f(v))[2:].zfill(8))
    return f(v)


# print(
#     r"""
#     .----.   @   @
#    / .-"-.`.  \v/
#    | | '\ \ \_/ )
#  ,-\ `-.' /.'  /
# '---`----'----'
# """
# )
# flag = input("Enter flag here: ").encode()
# out = b""
# for n in [flag[i : i + 4] for i in range(0, len(flag), 4)]:
#     out += bytes.fromhex(hex(enc(n[::-1]))[2:].zfill(8))

# if (
#     out
#     == b"L\xe8\xc6\xd2f\xde\xd4\xf6j\xd0\xe0\xcad\xe0\xbe\xe6J\xd8\xc4\xde`\xe6\xbe\xda>\xc8\xca\xca^\xde\xde\xc4^\xde\xde\xdez\xe8\xe6\xde"
# ):
#     print("[*] Flag correct!")
# else:
#     print("[*] Flag incorrect.")


##################
# enc(b) の逆変換テーブルを作成する
# b は 2
D = {}

fenc = b"L\xe8\xc6\xd2f\xde\xd4\xf6j\xd0\xe0\xcad\xe0\xbe\xe6J\xd8\xc4\xde`\xe6\xbe\xda>\xc8\xca\xca^\xde\xde\xc4^\xde\xde\xdez\xe8\xe6\xde"
print([fenc[i : i + 4] for i in range(0, len(fenc), 4)])

print(enc(b"ictf"))
print(enc(b"ictf"[::-1]))
print(bytes.fromhex(hex(enc(b"ictf"))[2:].zfill(8)))
print(bytes.fromhex(hex(enc(b"ictf"[::-1]))[2:].zfill(8)))

S = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!_{}"
for B in tqdm.tqdm(product(S, repeat=4)):
    B = "".join(B).encode()
    if B == b"ictf":
        print("OKOK")
        print(bytes.fromhex(hex(enc(B[::-1]))[2:].zfill(8)))
    D[bytes.fromhex(hex(enc(B[::-1]))[2:].zfill(8))] = B

flag = b""
for n in [fenc[i : i + 4] for i in range(0, len(fenc), 4)]:
    print(n, n in D)
    if n in D:
        flag += D[n]
        print(D[n])
print(flag)
