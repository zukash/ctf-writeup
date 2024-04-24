from collections import defaultdict

import tqdm
from pwn import *

FLAG2 = b"SEKAI{3ff1c13nt_GES_4_Shortest-Path-Queries-_-}"
NODE_COUNT = 60
# io = remote("chals.sekai.team", "3023")
# io.sendline(FLAG2)
io = process(["python", "server3.py"])


io.recvuntil(b"> Option:")
io.sendline(b"1")
io.recvuntil(b"[*] Edges:")
edges = eval(io.recvline())

io.clean()
io.sendline(b"2")
io.recvline()

for i in range(NODE_COUNT ** 2):
    print(i, io.recvline())
io.interactive()


# for _ in range(10):
#     ans = []
#     io.recvuntil(b"[*] Destination:")
#     dest = int(io.recvline())
#     G = defaultdict(set)
#     for s in tqdm.trange(NODE_COUNT):
#         if s == dest:
#             continue
#         io.recvuntil(b"> Query u,v:")
#         # io.sendline(f"{s},{dest}".encode())
#         io.sendline(f"{s},{dest}".encode())
#         io.recvuntil(b"[*] Token:")
#         s = bytes.fromhex(io.recvline().decode())
#         io.recvuntil(b"[*] Query Response:")
#         nodes = bytes.fromhex(io.recvline().decode())
#         nodes = s + nodes[: len(nodes) // 2]
#         assert len(nodes) % len(s) == 0
#         for i in range(0, len(nodes) - len(s), len(s)):
#             u = nodes[i : i + len(s)]
#             v = nodes[i + len(s) : i + len(s) * 2]
#             G[u].add(v)
#             G[v].add(u)
#     # 数合わせ
#     io.recvuntil(b"> Query u,v:")
#     io.sendline(b"0,1")

#     ans = sorted([len(V) for V in G.values()])
#     ans = " ".join([str(v) for v in ans])
#     io.sendline(ans.encode())
# io.interactive()
