from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import time

from pwn import *


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
    return ciphertext.hex()


def decrypt(enc):
    key = b""
    for i in range(8):
        key += (get_random_number() % (2**16)).to_bytes(2, "big")
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(enc)
    return plaintext


# io = process(["python3", "main.py"])
io = remote("betta.utctf.live", "7356")

io.sendlineafter(b"?", b"2")
io.sendlineafter(b"?", b"A")
io.recvuntil(b"message: ")
enc = io.recvline().strip().decode()
io.sendlineafter(b"?", b"1")
io.recvuntil(b"flag: ")
flag_enc = io.recvline().strip().decode()


for t in range(int(time.time() * 1000) % (10**6), -1, -1):
    seed = t
    predict = encrypt(b"A")
    if predict == enc:
        print(f"seed={t}")
        break

seed = t
encrypt(b"A")  # Skip one
flag = decrypt(bytes.fromhex(flag_enc))
print(flag)
