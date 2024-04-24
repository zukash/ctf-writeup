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

# 無限に文字列を生成し、10個まで表示する
generator = generate_strings()
for _ in tqdm.tqdm(range(10 ** 9 + 1)):
    S = next(generator)
    cS = crc32(S.encode())
    if cS in D:
        print(S, cS)

# 21 hiligo
