import requests
import random
from Crypto.Util.number import bytes_to_long, isPrime
import math
import hashlib
import base64


def generate_key(username):

    length = lambda x: len(bin(x)[2:])

    s = bytes_to_long(username.encode())

    random.seed(s)

    e = 0x1001
    phi = 0

    while math.gcd(phi, e) != 1:
        n = 1
        factors = []

        while length(n) < 2048:
            temp_n = random.getrandbits(48)
            if isPrime(temp_n):
                n *= temp_n
                factors.append(temp_n)
        phi = 1
        for f in factors:
            phi *= f - 1

    d = pow(e, -1, phi)

    return (n, e), (n, d)


def hash_string_sha256(message):
    message_bytes = message.encode("utf-8")
    sha256_hash = hashlib.sha256()
    sha256_hash.update(message_bytes)
    hashed_message = sha256_hash.digest()

    return int.from_bytes(hashed_message, byteorder="big")


def generate_signature(message, private_key):
    n, d = private_key
    hashed_message = hash_string_sha256(message)
    signature = pow(hashed_message, d, n)

    return signature


def verify_signature(msg, public_key, signature):
    initial_hash = hash_string_sha256(msg)

    n, e = public_key

    recoved_hash = pow(int(signature), e, n)

    return initial_hash == recoved_hash


username = "GCC"
password = "securePassword"
message = str({username: [True]})
message_b64 = base64.b64encode(message.encode()).decode()

public_key, private_key = generate_key(username)
signature = generate_signature(message, private_key)

assert verify_signature(message, public_key, signature)

url = f"http://worker01.gcc-ctf.com:13691/news?token={signature}&message={message_b64}"
print(url)

res = requests.get(url)
print(res.text)
# <p>Wouah!! You're a big boss. Here is your flag : GCC{f1x3d_533d_d154bl3_r4nd0mn355}</p>
