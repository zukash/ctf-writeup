from pwn import *

import os
from base64 import b64decode, b64encode
from hashlib import md5
from datetime import datetime
from Crypto.Cipher import AES


def register(username):
    io.sendlineafter(b'[1]register [2]login:', b'1')
    io.sendlineafter(b'username(base64):', b64encode(username))
    io.recvuntil(b'your cookie => ')
    return io.recvline()




# PREFIX の長さを特定 → 17
import sys
io = process(['python', 'server.mod.py'], stderr=sys.stderr)
# io = remote('crypto.2023.cakectf.com', '11111')

"""local
len(PREFIX) = 4
10 89
11 109
26 109
27 129
"""

"""remote
len(PREFIX) = 
13 109
14 129
"""

"""
以下が等しいので
cake|user=A * 27|2023-11-12 13:23:48.873192
XXXXXXXXX|user=A * 14|2023-11-12 13:23:48.873192
4 + 27 = len(XXXXXXXXX) + 14
len(XXXXXXXXX) = 17
"""

# for x in range(1, 30):
#     cookie = register(b'A' * x)
#     print(x, len(cookie))


# 任意文字列の埋め込み
def pad(data: bytes):
    l = 16 - len(data) % 16
    return data + bytes([l]*l)

def unpad(data: bytes):
    return data[:-data[-1]]

def encrypt(plain: bytes):
    debug(plain)
    plain = pad(plain)
    blocks = [plain[i:i+16] for i in range(0, len(plain), 16)]
    ciphers = [IV]
    for block in blocks:
        block = xor(block, md5(ciphers[-1]).digest())
        ciphers.append(aes.encrypt(block))
    debug(ciphers)
    return b"".join(ciphers)

def decrypt(cipher: bytes):
    blocks = [cipher[i:i+16] for i in range(0, len(cipher), 16)]
    h = md5(blocks[0]).digest() # IV
    plains = []
    for block in blocks[1:]:
        plains.append(xor(aes.decrypt(block), h))
        h = md5(block).digest()
    return unpad(b"".join(plains))  




io.interactive()