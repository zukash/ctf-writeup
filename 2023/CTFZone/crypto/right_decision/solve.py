"""
MD5 や SHA-1 を衝突させるツール
https://github.com/cr-marcstevens/hashclash
---
Proof of work の突破

Prefix: fqgLJqcohF
Target hash starts with:f373a3a

md5("fqgLJqcohF" + m).startWith("f373a3a") を満たす m を見つける
---
"""
from pwn import *
import string
from hashlib import md5
import itertools
import random


import tqdm


def generate_strings():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    length = 1
    while True:
        for s in itertools.product(alphabet, repeat=length):
            yield "".join(s)
        length += 1


# ランダムな文字列を生成する関数
def generate_random_string(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(letters) for _ in range(length))


# prefix = "VWwFewoYBW"
# target = "a4c5139"

# io = remote("0.0.0.0", "31339")
io = remote("right-decision.ctfz.one", "31339")
io.recvuntil(b"Prefix:")
prefix = io.recvline().decode().strip()
io.recvuntil(b"with:")
target = io.recvline().decode().strip()

print(prefix, target)

# calc hash
S = set()
for s in tqdm.tqdm(itertools.count(0)):
    # for s in tqdm.tqdm(generate_strings()):
    s = str(s)
    h = md5((prefix + s).encode("utf-8")).hexdigest()
    # S.add(h[:7])
    # print(len(S))
    # print(h)
    if h.startswith(target):
        print(s)
        break

io.sendline(s.encode())
io.sendline(b'{"vote": true, "i":0, "value": 0}')
io.interactive()
# 以下を送信
# {"vote": true, "i":0, "value": 0}

"""
479935872it [06:32, 1223111.31it/s]anjgfpj
479952313it [06:32, 1224019.32it/s]
"""
