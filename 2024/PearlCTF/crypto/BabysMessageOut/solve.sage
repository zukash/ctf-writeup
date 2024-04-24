from Crypto.Util.number import *
from message import n, c
from chall import nextPrime


# **************************************
# next_prime を外して大体の p を見積もる
# **************************************
p = var("p")
q = 17 * p + 1 + 3
r = 29 * p * q
s = q * r + p
t = r * s * q
f = p * q * r * s * t

ok = 0
ng = 1 << 3000
while ng - ok > 1:
    x = (ok + ng) // 2
    if f.subs(p=x) <= n:
        ok = x
    else:
        ng = x

# **************************************
# 正確な p の値を得る
# **************************************
p = x - 10000
while n % p != 0:
    p = next_prime(p)


# **************************************
# flag の復元
# **************************************

q = nextPrime(nextPrime(17 * p + 1) + 3)
r = nextPrime(29 * p * q)
s = nextPrime(q * r + p)
t = nextPrime(r * s * q)

assert n == p * q * r * s * t
e = 65537
phi = (p - 1) * (q - 1) * (r - 1) * (s - 1) * (t - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)

print(long_to_bytes(m))
