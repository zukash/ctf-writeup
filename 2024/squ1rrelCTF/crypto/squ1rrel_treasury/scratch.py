from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Util.strxor import strxor
from Crypto.Cipher import AES
import os
from secrets import KEY, FLAG
import random


def blockify(text: str, block_size: int):
    return [text[i : i + block_size] for i in range(0, len(text), block_size)]


def load(key):
    key_split = key.split(":")
    iv = bytes.fromhex(key_split[0])
    ct = bytes.fromhex(key_split[1])
    cipher = AES.new(KEY, AES.MODE_ECB)
    pt = blockify(cipher.decrypt(ct), AES.block_size)
    ct = blockify(ct, AES.block_size)
    for i, p in enumerate(pt):
        if i == 0:
            pt[i] = strxor(p, iv)
        else:
            pt[i] = strxor(strxor(ct[i - 1], pt[i - 1]), p)
    pt = b"".join(pt)
    pt_split = pt.split(b":")
    try:
        name = pt_split[0].decode()
    except Exception:
        name = "ERROR"
    balance = int(pt_split[1].strip(b"\x00").decode())
    return iv, name, balance


key = "2b89c326b98b9fa4e2b5411b7fe4f217:de1efb1be183baba66b2a90e1c1cb081"
iv = bytes.fromhex(key.split(":")[0])
nb = bytes.fromhex(key.split(":")[1])
iv = strxor(iv, bytes.fromhex("00" + "00" + "09" + "39" * 13))
key = iv.hex() + ":" + nb.hex()

print(load(key))
