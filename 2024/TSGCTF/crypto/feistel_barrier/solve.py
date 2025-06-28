from pwn import *
from hashlib import sha256

k = 1024 // 8
h_len = 32


def mgf(seed, mask_len):
    if mask_len > 2**32:
        raise ValueError("mask too long")
    t = b""
    for i in range(mask_len // h_len + 1):
        t += sha256(seed + i.to_bytes(4, "little")).digest()
    return t[:mask_len]


def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def decrypt_feistel(EM):
    maskedSeed = EM[1 : 1 + h_len]
    maskedDB = EM[1 + h_len :]
    seedMask = mgf(maskedDB, h_len)
    seed = xor(maskedSeed, seedMask)
    dbMask = mgf(seed, k - h_len - 1)
    db = xor(maskedDB, dbMask)
    data = db.split(b"\x01", 1)[1]
    return data


# nc 34.146.145.253 10961
io = remote("34.146.145.253", 10961)

io.recvuntil("chal = ")
chal = io.recvline().strip()
io.sendlineafter("ciphertext:", chal)

io.recvline()
EM = bytes.fromhex(io.recvline().strip().decode())
print(decrypt_feistel(EM))
