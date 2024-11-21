from params import h0, h1, n, ct
from ctftools.crypto.equation import bit_extension_search
from Crypto.Util.number import long_to_bytes

f0 = lambda p, q: p * q - n
f1 = lambda p, q: (q & p) - h0
f2 = lambda p, q: (q & (p << 1)) - h1

p, q = bit_extension_search([f0, f1, f2], 2048)[0]
print(f"{p = }")
print(f"{q = }")
assert p * q == n

e = 65537
d = pow(e, -1, (p - 1) * (q - 1))
m = pow(ct, d, n)
print(long_to_bytes(m))
