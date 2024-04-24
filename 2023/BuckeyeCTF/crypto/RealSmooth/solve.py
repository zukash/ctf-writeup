from collections import defaultdict
from typing import Counter
from pwn import *


with open("database.txt", "r") as f:
    database = f.read().split()

database.pop()


def is_printable(text):
    for t in text:
        if not (32 <= t <= 126):
            return False
    return True


database = [bytes.fromhex(ct) for ct in database]
key = b""
V = set()
for i in range(18):
    C = Counter()
    for index, ct in enumerate(database):
        if index in V:
            continue
        C[ct[~i]] += 1

    if i == 0:
        c = C.most_common()[0][0]
        k = c ^ ord(" ")
        key = bytes.fromhex(f"{k:02x}") + key
    elif i in [11, 12, 17]:
        print(i, C)
        c = C.most_common()[0][0]
        k = c ^ ord("\n")
        key = bytes.fromhex(f"{k:02x}") + key
    else:
        print(i, C)
        c = C.most_common()[0][0]
        k = c ^ ord(" ")
        key = bytes.fromhex(f"{k:02x}") + key

    # 削除
    for index, ct in enumerate(database):
        if index in V:
            continue
        if k ^ ct[~i] != ord(" "):
            # if i > 0:
            #     assert k ^ ct[~i] == ord("\n")
            V.add(index)

print(key)
assert len(key) == 18

for i, ct in enumerate(database[:20]):
    pw = xor(ct, key)
    print(i, pw)

ct = database[6]
# pw = b"{aaaawn_pl41n73x7}"
pw = b"cristianoronaldo\n "
key = xor(ct, pw)
print(len(key), len(ct), len(pw))


for i, ct in enumerate(database):
    pw = xor(ct, key)
    print(i, pw)

# print(key)
# ct = database[10880]
# # pw = b"{aaaawn_pl41n73x7}"
# pw = b"{aaaawn_pl41n73x7}"
# key = xor(ct, pw)
# print(len(key), len(ct), len(pw))

# ct = database[11220]
# pw = b"thankyousomuch\n   "
# key = xor(ct, pw)
# print(len(key), len(ct), len(pw))


# for i, ct in enumerate(database):
#     print(i, xor(ct, key))


# ct = database[10880]
# pw = xor(ct, key)
# print(pw)

# # pl41n73x7}


# # bctf{awn_pl41n73x7}

# # btcf{0wn_pl41n73x7}

# btcf{w3_d0_4_l177l3_kn0wn_pl41n73x7}
