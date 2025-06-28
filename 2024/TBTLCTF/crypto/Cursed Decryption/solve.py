from typing import Counter
from Crypto.Util.number import *
from tqdm import trange
from pwn import *

io = process(["python", "server.py"])
# io = remote("0.cloud.chals.io", "18312")

"""
LSB Oracle Attack
ref. https://kmyk.github.io/blog/blog/2017/06/24/lsb-leak-attack/

requirement:
* p, q: prime
* p > 3, q > 3
* n = p * q

prop:
let m \in Zmod(n)
if (m * 2) & 1 == 0:
    assert m < n // 2
else:
    assert m >= n // 2

proof:
m < n // 2
=> m * 2 < n
=> (m * 2) & 1 == 0

n // 2 <= m < n
=> n <= m * 2 < n * 2
=> (m * 2) % n == m * 2 - n
=> (m * 2) & 1 == 1
"""


def decrypt_and_leak_lsb(c):
    """
    復号結果の最下位ビットを返す
    """
    C = Counter()
    for _ in range(50):
        io.sendlineafter(b":", bin(c)[2:].encode())
        io.recvuntil(b"Decrypted: ")
        res = io.recvline().strip().decode()
        C[res[-1]] += 1
    return int(C["0"] < C["1"])


def lsb_oracle_attack(c, e, n):
    l, r = 0, n
    for i in trange(1, n.bit_length() + 1):
        m = (l + r) // 2
        nc = c * pow(2, i * e, n) % n
        if decrypt_and_leak_lsb(nc):
            l = m
        else:
            r = m
    return l


def send(payload):
    io.sendlineafter(b":", bin(payload)[2:].encode())
    io.recvuntil(b"Decrypted: ")
    return len(io.recvline().strip())


# **************************************************
# パラメータ取得
# **************************************************
io.recvuntil(b"N = ")
n = int(io.recvline())
e = 65537
io.recvuntil(b"enc(flag) = ")
c = int(io.recvline(), 2)

# **************************************************
# 頻度分析
# **************************************************
# D = [Counter() for _ in range(512)]
# for _ in range(100):
#     io.sendlineafter(b":", bin(c)[2:].encode())
#     io.recvuntil(b"Decrypted: ")
#     res = io.recvline().strip()
#     for i, b in enumerate(list(res)):
#         D[i][b] += 1

# 偏りあり
# 366 Counter({49: 77, 48: 23})

# **************************************************
# LSB Oracle Attack
# **************************************************
flag = lsb_oracle_attack(c, e, n)
print(long_to_bytes(flag))
