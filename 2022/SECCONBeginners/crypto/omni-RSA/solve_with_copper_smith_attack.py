from ctftools.crypto.rsa import small_roots_mod_p
from sage.all import *
from params import *
from Crypto.Util.number import long_to_bytes
from tqdm import trange


for k in trange(e + 1):
    x = PolynomialRing(Zmod(n), "x").gen()
    f = e * (x * 2**470 + s) - 1 - k * (1 - rq)
    roots = small_roots_mod_p(f, x_bit=512 - 470, n_bit=1024, p_bit=256)
    if roots:
        x0 = roots[0]
        break


d_qr = int(x0 * 2**470 + s)
q = PolynomialRing(ZZ, "q").gen()
f = e * d_qr - 1 - k * ((q - 1) * (q + rq - 1))
for q, _ in f.roots():
    if n % q == 0:
        break
r = q + rq
p = n // (q * r)
assert p * q * r == n

phi = (p - 1) * (q - 1) * (r - 1)
d = inverse_mod(e, phi)
print(long_to_bytes(pow(cipher, d, n)))
