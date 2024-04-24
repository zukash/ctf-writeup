from collections import defaultdict

import tqdm
import utils
from pwn import *

FLAG1 = b"SEKAI{GES_15_34sy_2_br34k_kn@w1ng_th3_k3y}"
NODE_COUNT = 130
io = remote("chals.sekai.team", "3062")
io.sendline(FLAG1)
# io = process(["python", "server2.py"])

for _ in range(30):
    ans = []
    io.recvuntil(b"[*] Destination:")
    dest = int(io.recvline())
    G = defaultdict(set)
    for s in tqdm.trange(NODE_COUNT):
        if s == dest:
            continue
        io.recvuntil(b"> Query u,v:")
        # io.sendline(f"{s},{dest}".encode())
        io.sendline(f"{s},{dest}".encode())
        io.recvuntil(b"[*] Token:")
        s = bytes.fromhex(io.recvline().decode())
        io.recvuntil(b"[*] Query Response:")
        nodes = bytes.fromhex(io.recvline().decode())
        nodes = s + nodes[: len(nodes) // 2]
        assert len(nodes) % len(s) == 0
        for i in range(0, len(nodes) - len(s), len(s)):
            u = nodes[i : i + len(s)]
            v = nodes[i + len(s) : i + len(s) * 2]
            G[u].add(v)
            G[v].add(u)
    # 数合わせ
    io.recvuntil(b"> Query u,v:")
    io.sendline(b"0,1")

    ans = sorted([len(V) for V in G.values()])
    ans = " ".join([str(v) for v in ans])
    io.sendline(ans.encode())
io.interactive()
