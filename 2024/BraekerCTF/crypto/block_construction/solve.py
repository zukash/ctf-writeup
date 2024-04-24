import binascii
from Crypto.Cipher import AES
from os import urandom
from string import printable
import random
from time import time
from tqdm import trange


flag = "brck{not_a_flag}"
key = urandom(32)


def encrypt(raw):
    cipher = AES.new(key, AES.MODE_ECB)
    return binascii.hexlify(cipher.encrypt(raw.encode()))


ciphertext = open("ciphertext").read()

print(len(ciphertext))
I = []
for i in range(0, len(ciphertext), 64):
    ct = ciphertext[i : i + 64]
    if ct[:32] == ct[32:]:
        # I.append(i // 64)
        I.append((i // 64) % len(printable))

rand_printable = [x for x in printable]
flag = "".join([rand_printable[i] for i in I])

for t in trange(int(time()), -1, -1):
    random.seed(t)
    rand_printable = [x for x in printable]
    random.shuffle(rand_printable)

    flag = "".join([rand_printable[i] for i in I])
    if "brck" in flag:
        print(flag)
        break
