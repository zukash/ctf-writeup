from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import random


seed = random.randint(0, 10**6)


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


def sample(s, k):
    global seed
    seed = s
    return tuple(encrypt(b"A")[1] for _ in range(k))


with open("db.txt", "w") as f:
    for s in range(10**6):
        f.write(str(sample(s, 3)) + "\n")
