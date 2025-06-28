from sage.all import *
from params import n, e, c, cp, cq
from Crypto.Util.number import long_to_bytes, inverse
import math


n, e, c, cp, cq = map(int, (n, e, c, cp, cq))
PR = PolynomialRing(Zmod(n), names=("x"))
x = PR.gen()
f = (x - cp + c) * (x - cq + c)

r = int(f.small_roots()[0])
print(r.bit_length())

cr = c + r

# Step 1: GCDでpを推定
diff = (cp - cr) % n
p = math.gcd(diff, n)
assert n % p == 0
q = n // p

# Step 2: 秘密鍵 d を計算
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

# Step 3: 復号
m = pow(cr, d, n)
flag = long_to_bytes(m)
print(flag.decode())
