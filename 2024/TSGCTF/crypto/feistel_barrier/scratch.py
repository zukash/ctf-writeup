from hashlib import sha256
from Crypto.Util.number import getStrongPrime
import os

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


def encrypt_feistel(data):
    L = b""
    IHash = sha256(L).digest()
    PS = b"\x00" * (k - len(data) - 2 * h_len - 2)
    DB = IHash + PS + b"\x01" + data
    seed = os.urandom(h_len)
    dbMask = mgf(seed, k - h_len - 1)
    maskedDB = xor(DB, dbMask)
    seedMask = mgf(maskedDB, h_len)
    maskedSeed = xor(seed, seedMask)
    EM = b"\x00" + maskedSeed + maskedDB
    print(f"{maskedSeed.hex() = }")
    print(f"{maskedDB.hex() = }")
    return EM


def decrypt_feistel(EM):
    maskedSeed = EM[1 : 1 + h_len]
    maskedDB = EM[1 + h_len :]
    seedMask = mgf(maskedDB, h_len)
    seed = xor(maskedSeed, seedMask)
    dbMask = mgf(seed, k - h_len - 1)
    db = xor(maskedDB, dbMask)
    data = db.split(b"\x01", 1)[1]
    return data


em = encrypt_feistel(b"FAKECTF{THIS_IS_FAKE}")
m = decrypt_feistel(em)
print(m)

# # ************************************************
# # encrypt
# # ************************************************
# data = b"FAKECTF{THIS_IS_FAKE}"
# L = b""
# IHash = sha256(L).digest()
# PS = b"\x00" * (k - len(data) - 2 * h_len - 2)
# DB = IHash + PS + b"\x01" + data
# seed = os.urandom(h_len)
# dbMask = mgf(seed, k - h_len - 1)
# maskedDB = xor(DB, dbMask)
# seedMask = mgf(maskedDB, h_len)
# maskedSeed = xor(seed, seedMask)
# EM = b"\x00" + maskedSeed + maskedDB
# print(f"{maskedSeed.hex() = }")
# print(f"{maskedDB.hex() = }")

# # ************************************************
# # decrypt
# # ************************************************
# masked_seed = EM[1 : 1 + h_len]
# masked_db = EM[1 + h_len :]
# assert maskedSeed == masked_seed
# assert maskedDB == masked_db
# seed_mask = mgf(masked_db, h_len)
# seed = xor(masked_seed, seed_mask)
# assert seedMask == seed_mask
# db_mask = mgf(seed, k - h_len - 1)
# db = xor(masked_db, db_mask)
# assert DB == db
# data = db.split(b"\x01", 1)[1]
# print(data)
