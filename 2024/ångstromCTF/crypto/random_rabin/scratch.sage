import random
from Crypto.Util.number import getPrime


def primegen():
    while True:
        p = getPrime(512)
        if p % 4 == 3:
            return p


def keygen():
    p = primegen()
    q = primegen()
    n = p * q
    return n, (n, p, q)


def encrypt(pk, m):
    n = pk
    return pow(m, 2, n)


def decrypt(sk, c):
    n, p, q = sk
    # yp, yq, _ = xgcd(p, q)
    _, yp, yq = xgcd(p, q)
    mp = pow(c, (p + 1) // 4, p)
    mq = pow(c, (q + 1) // 4, q)
    assert (yp * p + yq * q) % n == 1
    print(f"{yp=}, {yq=}, {mp=}, {mq=}")
    s = yp * p * mq % n
    t = yq * q * mp % n
    rs = [(s + t) % n, (-s - t) % n, (s - t) % n, (-s + t) % n]
    r = random.choice(rs)
    return r


# *************************************************
# test
# *************************************************
p, q = 7, 11
n = p * q
m = 20

pk, sk = n, (n, p, q)
c = encrypt(pk, m)
print(decrypt(sk, c))

# *************************************************
# test
# *************************************************
pk, sk = keygen()
print(f"pubkey: {pk}")
secret = random.randbytes(16)
m = int.from_bytes(secret, "big")
pt = decrypt(sk, encrypt(pk, m))
print(f"m: {m}")
print(f"plaintext: {pt}")
# guess = bytes.fromhex(input("gimme the secret: "))
print(encrypt(pk, m))
x = decrypt(sk, encrypt(pk, m))
print(x**2 % pk)

print(encrypt(pk, m) ^ (1 / 2))
