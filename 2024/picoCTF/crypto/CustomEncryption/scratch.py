from random import randint
import sys
from pwn import xor


def generator(g, x, p):
    return pow(g, x) % p


def encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        cipher.append(((ord(char) * key * 311)))
    return cipher


def decrypt(cipher, key):
    pt = []
    for char in cipher:
        pt.append((char // key // 311))
    return pt


def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True


def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text


def dynamic_xor_decrypt(ct, text_key):
    return xor(ct.encode(), text_key.encode())[::-1].decode()


# x = dynamic_xor_encrypt("abcdefg", "trudeau")
# print(xor(x.encode(), "trudeau".encode()))
# print(dynamic_xor_decrypt(x, "trudeau"))

p = 97
g = 31
a = 94
b = 29
print(f"a = {a}")
print(f"b = {b}")
u = generator(g, a, p)
v = generator(g, b, p)
key = generator(v, a, p)
b_key = generator(u, b, p)
shared_key = key
print(shared_key)
ct = dynamic_xor_encrypt("abcdefghijk", "trudeau")
print(ct)
ct = dynamic_xor_encrypt(ct, "trudeau")
print(ct)


ct = [
    260307,
    491691,
    491691,
    2487378,
    2516301,
    0,
    1966764,
    1879995,
    1995687,
    1214766,
    0,
    2400609,
    607383,
    144615,
    1966764,
    0,
    636306,
    2487378,
    28923,
    1793226,
    694152,
    780921,
    173538,
    173538,
    491691,
    173538,
    751998,
    1475073,
    925536,
    1417227,
    751998,
    202461,
    347076,
    491691,
]

pt = [chr(c) for c in decrypt(ct, shared_key)]
print(dynamic_xor_decrypt("".join(pt), "trudeau"))
