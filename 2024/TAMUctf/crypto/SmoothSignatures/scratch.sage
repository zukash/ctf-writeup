from hashlib import sha256
from math import lcm
from Crypto.Util.number import *
from secrets import randbelow

NUM_BITS = 2048
# NUM_BITS = 32


def getModulus(bits):
    n = 1
    primes = []
    while n.bit_length() < bits:
        p = getPrime(24)
        # p = getPrime(10)
        if p not in primes:
            n *= p
            primes.append(p)
    return n, primes


def sign(n, msg, d):
    h = bytes_to_long(sha256(msg).digest())
    k = randbelow(q - 2) + 1
    x = pow(h, k, n)
    r = pow(x, d, n)
    s = pow(h + x, d, n)
    return r, s


def verify(n, msg, e, r, s):
    h = bytes_to_long(sha256(msg).digest())
    v1 = pow(r, e, n)
    v2 = pow(s, e, n)
    return v2 == (v1 + h) % n


n, primes = getModulus(NUM_BITS)
q = 1
for p in primes:
    q = lcm(q, p - 1)
msgs = []
e = 65537
d = pow(e, -1, q)

print(f"{n = }")
print(f"{e = }")
print(f"{d = }")
print(f"{primes = }")

h = bytes_to_long(sha256(b"A").digest())
r, s = sign(n, b"A", d)
print(f"{r = }")
print(f"{s = }")
print(f"{h = }")

h = bytes_to_long(sha256(b"A").digest())
v1 = pow(r, e)
v2 = pow(s, e)

S = []
n_, q_ = 1, 1
for p in Primes():
    # if p.bit_length() > 10:
    if p.bit_length() > 24:
        break
    # if (v2 - (v1 + h)) % p == 0:
    if (pow(s, e, p) - (pow(r, e, p) + h)) % p == 0:
        n_ *= p
        q_ *= p - 1
        print(p)

d_ = pow(e, -1, q_)
print(f"{n_ = }")
print(f"{q_ = }")
print(f"{d_ = }")

msg = b"What is the flag?"
r, s = sign(n_, msg, d_)
print(verify(n, msg, e, r, s))

# print(pow(r, e, n))
# print(e * d % q)
# print(factor(q))
# print(verify(n, b"A", e, r, s))
# h = bytes_to_long(sha256(b"A").digest())
