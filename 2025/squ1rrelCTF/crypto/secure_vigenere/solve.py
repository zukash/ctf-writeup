from pwn import *
from itertools import permutations
from vigenere import encrypt, decrypt
import random
from string import printable


def get_enc():
    io = remote("20.84.72.194", 5007)
    enc = io.recvline_contains(b"Flag: ").decode().split(":")[-1].strip()
    io.close()
    return enc


# enc = get_enc()
# X = [set() for _ in range(len(enc))]
# while True:
#     enc = get_enc()
#     done = True
#     for i, c in enumerate(enc):
#         X[i].add(c)
#         if len(X[i]) < 10:
#             done = False
#     if done:
#         break
# print(X)

X = [
    {"q", "b", "a", "k", "z", "y", "t", "n", "m", "c"},
    {"v", "b", "k", "x", "e", "j", "y", "n", "l", "m"},
    {"b", "a", "p", "x", "z", "y", "j", "l", "m", "s"},
    {"q", "g", "w", "z", "e", "t", "h", "i", "f", "s"},
    {"o", "k", "w", "z", "y", "n", "l", "m", "f", "c"},
    {"i", "a", "x", "k", "w", "z", "y", "r", "o", "l"},
    {"b", "a", "x", "p", "z", "j", "y", "l", "m", "s"},
    {"v", "b", "k", "x", "e", "y", "j", "n", "l", "m"},
    {"v", "k", "w", "z", "j", "h", "t", "i", "l", "c"},
    {"q", "e", "t", "c", "r", "i", "l", "f", "s", "u"},
    {"v", "f", "p", "e", "d", "y", "h", "r", "g", "s"},
    {"v", "i", "x", "w", "t", "h", "o", "l", "f", "u"},
    {"q", "g", "w", "z", "e", "t", "h", "i", "f", "s"},
    {"q", "g", "x", "e", "d", "r", "o", "c", "f", "u"},
    {"q", "b", "a", "k", "z", "t", "y", "n", "m", "c"},
    {"q", "b", "p", "k", "e", "d", "t", "h", "r", "s"},
    {"q", "u", "e", "t", "c", "r", "i", "l", "f", "s"},
    {"v", "b", "k", "x", "e", "j", "y", "n", "l", "m"},
    {"q", "b", "a", "k", "z", "t", "y", "n", "m", "c"},
    {"q", "g", "w", "z", "e", "t", "h", "i", "f", "s"},
    {"v", "f", "p", "e", "d", "y", "h", "r", "g", "s"},
    {"q", "b", "a", "p", "e", "y", "h", "o", "m", "n"},
    {"q", "u", "e", "t", "c", "r", "i", "l", "f", "s"},
    {"a", "k", "x", "w", "d", "j", "i", "l", "m", "u"},
    {"a", "k", "x", "w", "d", "j", "i", "l", "m", "u"},
    {"v", "p", "x", "w", "j", "y", "i", "m", "g", "u"},
    {"v", "k", "w", "e", "t", "h", "n", "g", "s", "u"},
    {"o", "k", "w", "z", "y", "n", "l", "m", "f", "c"},
    {"v", "k", "w", "z", "j", "t", "h", "i", "l", "c"},
    {"v", "p", "x", "w", "j", "y", "i", "m", "g", "u"},
]

alphabet = list("squirrelctf")

Y = defaultdict(set)
for x in printable:
    for a in alphabet:
        Y[x].add(encrypt(x, a).lower())

flag = ""
for x in X:
    for k, v in Y.items():
        if x == v:
            flag += k
            break

print(flag)

# K = []
# for k in range(1, 8):
#     for p in permutations(alphabet, k):
#         key = "".join(p)
#         K.append(key)

# key = random.choice(K)
# enc = encrypt(key, "squirrelctf")
# print(enc)

# print(len(K))
# enc = get_enc()
# C = set([decrypt(enc, k) for k in K])
# while len(C) > 1:
#     enc = get_enc()
#     nC = set([decrypt(enc, k) for k in K])
#     C = C.intersection(nC)
#     print(len(C))

# print(C)

# # 10C10 * 10! + 10C9 * 9!
# # 10P10 + 10P9 + 10P8 + 10P7 + 10P6 + 10P5 + 10P4 + 10P3 + 10P2 + 10P1
