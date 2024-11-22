from params import r, n, e, c
from Crypto.Util.number import long_to_bytes
from ctftools.crypto.equation import bit_extension_search

mask0 = int("55" * 128, 16)
mask1 = mask0 << 1

f0 = lambda p, q: p * q - n
f1 = lambda p, q: (p & mask0) + (q & mask1) - r

p, q = bit_extension_search([f0, f1], 1024)[0]
print(f"{p = }")
print(f"{q = }")
assert p * q == n

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)

print(long_to_bytes(m))
