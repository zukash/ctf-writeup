from itertools import product
from pwn import *

from hashlib import sha256
from tqdm import trange, tqdm
from string import printable

context.log_level = "error"


def xor(data1, data2):
    return bytes([data1[i] ^ data2[i] for i in range(len(data1))])


# key: 2 bytes
def do_round(data, key):
    m = sha256()
    m.update(xor(data[2:4], key))
    return bytes(data[2:4]) + xor(m.digest()[0:2], data[0:2])


def do_round_inv(data, key):
    m = sha256()
    m.update(xor(data[0:2], key))
    return xor(m.digest()[0:2], data[2:4]) + bytes(data[0:2])


def pad(data):
    padding_length = 4 - (len(data) % 4)
    return data + bytes([padding_length] * padding_length)


def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]


# XOR every character with bytes generated from the PRNG
# key: 2 bytes
def encrypt_block(data, key):
    for i in range(10):
        data = do_round(data, key)
    return data


def decrypt_block(data, key):
    for i in range(10):
        data = do_round_inv(data, key)
    return data


# key: 2 bytes
def encrypt_data(data, key):
    cipher = b""
    while data:
        cipher += encrypt_block(data[:4], key)
        data = data[4:]
    return cipher


def decrypt_data(cipher, key):
    data = b""
    while cipher:
        data += decrypt_block(cipher[:4], key)
        cipher = cipher[4:]
    return data


# key: 4 bytes
def encrypt(data, key):
    data = pad(data)
    return encrypt_data(encrypt_data(data, key[0:2]), key[2:4])


def decrypt(data, key):
    plain = decrypt_data(decrypt_data(data, key[2:4]), key[0:2])
    return unpad(plain)


def check(data):
    # io = remote("brutalmogging.ctf.umasscybersec.org", "1337")
    io = process(["python", "main.py"])
    io.recvuntil(b"flag is:")
    enc = io.recvline().strip()
    io.sendlineafter(b"0:", data.encode())
    io.recvuntil(b":")
    res = io.recvline().strip()
    io.close()
    return enc.startswith(res[:16])


# key = bytes.fromhex("db0674d8")

with open("enc.txt", "r") as f:
    E = f.read().strip().split("\n")


E.append(encrypt(b"UMASS{dummy_flag}", b"\x00\x00\x01\x00").hex())

E8 = [e[:8] for e in E]
D = set(E8)
print(len(D))

data = b"UMAS"
for k in trange(256**4):
    key = k.to_bytes(4, "big")
    enc = encrypt(data, key)[:4]
    if enc.hex() in D:
        print(f"Found: {key.hex()}")
        i = E8.index(enc.hex())
        enc = bytes.fromhex(E[i])
        pt = decrypt(enc, key)
        print(pt)
        # exit()

# b'UMASS{1_h4ve_b33n_m3w1ng_f0r_my_l1f3_733061741}'
