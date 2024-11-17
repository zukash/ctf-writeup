from params import *
from ctftools.crypto.equation import bit_extension_search
from Crypto.Util.number import long_to_bytes
from tqdm import trange


def get_q():
    for k in trange(e + 1):
        f = lambda x: e * s - 1 - k * ((x - 1) * (rq + x - 1))
        for (q,) in bit_extension_search([f], 470):
            if n % q == 0:
                return q


q = get_q()
r = q + rq
p = n // (q * r)
phi = (p - 1) * (q - 1) * (r - 1)
d = pow(e, -1, phi)
flag = pow(cipher, d, n)
print(long_to_bytes(flag))
