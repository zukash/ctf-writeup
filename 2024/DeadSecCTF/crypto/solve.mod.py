from collections import Counter
from itertools import combinations
from string import digits, ascii_letters, punctuation
import math
from tqdm import tqdm

counts = [
    5,
    4,
    7,
    5,
    5,
    8,
    9,
    4,
    5,
    7,
    4,
    4,
    7,
    5,
    7,
    8,
    4,
    2,
    5,
    5,
    4,
    3,
    10,
    4,
    5,
    7,
    4,
    4,
    4,
    6,
    5,
    12,
    5,
    5,
    5,
    8,
    7,
    9,
    2,
    3,
    2,
    5,
    8,
    6,
    4,
    4,
    7,
    2,
    4,
    5,
    7,
    9,
    4,
    9,
    7,
    4,
    7,
    8,
    4,
    2,
    4,
    4,
    4,
    4,
    3,
    3,
    7,
    4,
    6,
    9,
    4,
    4,
    4,
    6,
    7,
    4,
    4,
    4,
    1,
    3,
    5,
    8,
    4,
    9,
    11,
    7,
    4,
    2,
    4,
]

alphabet = digits + ascii_letters + punctuation
alphabet = set(alphabet) - set({"4", "A"})
print(len(alphabet))  # 94
P = 13**37
# 取り除かれる 5 文字の探索
for X in tqdm(list(combinations(alphabet, 3))):
    password = b""
    sub = sorted("".join(set(alphabet) - set(X)))
    assert len(sub) == len(counts)
    p, s = 1, 0
    for k, v in zip(Counter(sub).keys(), counts):
        password += k.encode() * v
        # p *= pow(ord(k), v, P)
        # s += ord(k) * v
        # p %= P
        # s %= P
    pl = list(password)
    pl = sorted(pl)
    # print(math.prod(pl), sum(pl))
    if math.prod(pl) % P == sum(pl) % P:
        print("Found")
        print(password)
