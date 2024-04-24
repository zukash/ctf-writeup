import binascii
from os import urandom
from Crypto.Cipher import AES

key = urandom(32)


def encrypt(raw):
    cipher = AES.new(key, AES.MODE_ECB)
    return binascii.hexlify(cipher.encrypt(raw.encode()))


# 16 bytes 区切り
# b"b1bf9debb57f983e810792ca647653db"
print(encrypt("A" * 16))
# b"b1bf9debb57f983e810792ca647653dbb1bf9debb57f983e810792ca647653db"
print(encrypt("A" * 32))
