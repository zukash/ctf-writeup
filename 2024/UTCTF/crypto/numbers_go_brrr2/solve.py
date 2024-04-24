#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import random

from pwn import *


# io = process(["python", "main.py"])
# nc betta.utctf.live 2435
io = remote("betta.utctf.live", 2435)


def get_random_number():
    global seed
    seed = int(str(seed * seed).zfill(12)[3:9])
    return seed


def encrypt(message):
    key = b""
    for i in range(8):
        key += (get_random_number() % (2**16)).to_bytes(2, "big")
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return key.hex(), ciphertext.hex()


def io_encrypt(message):
    io.sendlineafter(b"?", b"2")
    io.sendlineafter(b"?", message)
    io.recvuntil(b"message:")
    return io.recvline().strip().decode()


def io_guess(key):
    io.sendlineafter(b"?", b"1")
    io.sendlineafter(b"?", key)


with open("db.txt", "r") as f:
    D = list(map(eval, f.readlines()))

for _ in range(3):
    X = tuple(io_encrypt(b"A") for _ in range(3))
    seed = D.index(X)
    key, ciphertext = encrypt(b"A")
    key, ciphertext = encrypt(b"A")
    key, ciphertext = encrypt(b"A")
    io_guess(key)

io.interactive()
