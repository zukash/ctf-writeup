from collections import defaultdict
import itertools
from binascii import crc32

import tqdm


def generate_strings():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    length = 1
    while True:
        for s in itertools.product(alphabet, repeat=length):
            yield "".join(s)
        length += 1


import random
import string

# ランダムな文字列を生成する関数
def generate_random_string(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(letters) for _ in range(length))


# 10文字のランダムな文字列を生成


D = set(
    [
        1,
        3,
        7,
        21,
        12517,
        13477,
        37551,
        40431,
        87619,
        94339,
        262857,
        283017,
        168691609,
        506074827,
        1180841263,
        3542523789,
    ]
)

for _ in tqdm.tqdm(itertools.count(0)):
    r = generate_random_string(10)
    cr = crc32(r.encode())
    if cr in D:
        print(cr, r)

# # 無限に文字列を生成し、10個まで表示する
# C = defaultdict()
# generator = generate_strings()
# for _ in tqdm.tqdm(range(10 ** 9 + 1)):
#     S = next(generator)
#     cS = crc32(S.encode())
#     # if cS in C:
#     #     print("collision!")
#     C[cS] = S
#     # if crc32(S.encode()) in D:
#     #     print(S)

# for d in D:
#     if d in C:
#         print(d, C[d])
# # print(C)

# # 21 hiligo
