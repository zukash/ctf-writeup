import os

from Crypto.Util.number import bytes_to_long, getPrime

flag = os.getenvb(b"FLAG", b"SECCON{THIS_IS_FAKE}")
assert flag.startswith(b"SECCON{")
m = bytes_to_long(flag)
e = 0x10001
p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 65537
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
hint = p + q
c = pow(m, e, n)

print(f"e={e}")
print(f"d={d}")
print(f"hint={hint}")
print(f"c={c}")

print(e * d)
print(n)
print((e * d - 1) // phi)
print((e * d - 1) % phi)

assert e * d % phi == 1
assert (e * d - 1) % phi == 0
assert (e * d - 1) in [k * phi for k in range(e)]  # d < phi
assert (e * d - 1) in [k * (p - 1) * (q - 1) for k in range(e)]
assert (e * d - 1) in [k * (n - hint + 1) for k in range(e)]
assert [(e * d - 1) == k * (n - hint + 1) for k in range(e)].count(True)
