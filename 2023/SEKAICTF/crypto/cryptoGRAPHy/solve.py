import utils
from pwn import *

io = remote("chals.sekai.team", "3001")

io.recvuntil(b"[*] Key:")
keys = bytes.fromhex(io.recvline().decode())
key_SKE = keys[:16]
key_DES = keys[16:]

for _ in range(50):
    ans = []
    io.recvuntil(b"[+] Query")
    s = io.recvline().decode().split(":")[1].split()[0]
    ans.append(s)
    io.recvuntil(b"[*] Response:")
    values = bytes.fromhex(io.recvline().decode())
    assert len(values) % 32 == 0
    for i in range(0, len(values), 32):
        value = values[i : i + 32]
        v, r = utils.SymmetricDecrypt(key_SKE, value).decode().split(",")
        ans.append(v)
    io.sendline(" ".join(ans).encode())
io.interactive()


# SEKAI{GES_15_34sy_2_br34k_kn@w1ng_th3_k3y}
