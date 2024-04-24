from collections import defaultdict
import itertools
from typing import Counter

import tqdm

with open("out.txt", "r") as f:
    # with open("out.mod.txt", "r") as f:
    enc = f.read()

print(Counter(enc))
emojis = set(enc)
# enc = enc[: enc.index("🎁🐶")]
# enc = enc[: enc.index("🎈🍦")]

D = defaultdict()
########prod#########
D["🎈"] = "6"
D["🍕"] = "7"
D["🎁"] = "2"
D["🐶"] = "0"
##########
D["🌼"] = "3"
D["🌸"] = "5"
D["🎉"] = "4"
########local#########
# Counter({'6': 1139, '7': 543, '2': 489, '0': 355, '5': 262, '4': 223, '3': 148, 'e': 140, '9': 130, '1': 127, 'f': 102, 'c': 100, '8': 79, 'd': 37, 'a': 8, 'b': 6})
# Counter({'🐳': 1139, '🎁': 543, '🎈': 489, '🍦': 355, '⚡': 262, '🌸': 223, '🌼': 148, '🎉': 140, '🌞': 130, '️': 127, '🦋': 102, '🍔': 100, '🎸': 79, '🚀': 37, '🌺': 8, '🍕': 6})
# D["🐳"] = "6"
# D["🎁"] = "7"
# D["🎈"] = "2"
# D["🍦"] = "0"
# D["⚡"] = "5"
# D["🌸"] = "4"
# D["🌼"] = "3"
# D["🎉"] = "e"
# D["🌞"] = "9"
# D["️"] = "1"
# D["🦋"] = "f"
# D["🍔"] = "c"
# D["🎸"] = "8"
# D["🚀"] = "d"
# D["🌺"] = "a"
# D["🍕"] = "b"
print(D)

RC = [c for c in "0123456789abcdef" if c not in D.values()]
RE = [e for e in emojis if e not in D.keys()]
print(RC, len(RC))
print(RE, len(RE))


def to_string(enc, D):
    ans = []
    if len(enc) & 1:
        return False
    for i in range(0, len(enc), 2):
        c = D[enc[i]] + D[enc[i + 1]]
        c = chr(int(c, 16))
        if not (c.isprintable() or ord(c) == 10):
            return False
        ans.append(c)
    return "".join(ans)


for order in tqdm.tqdm(list(itertools.permutations(RE))):
    ans = ""
    nD = D.copy()
    for c, e in zip(RC, order):
        nD[e] = c
    flag = to_string(enc, nD)
    if flag:
        print(flag)

print(D)
