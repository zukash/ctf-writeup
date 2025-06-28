from params import *

from Crypto.Util.number import long_to_bytes, inverse
import math

# Step 1: GCDでpを推定
diff = (cp - c) % n
p = math.gcd(diff, n)
assert n % p == 0
q = n // p

# Step 2: 秘密鍵 d を計算
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

# Step 3: 復号
m = pow(c, d, n)
flag = long_to_bytes(m)
print(flag.decode())
