from math import gcd
from Crypto.Util.number import *
from output import power1, power2, out2, eq1, c, n


def solve(e1, e2, r1, r2):
    # assert r1 == (pow(p, e1, n) + pow(5 * q, e1, n)) % n
    # assert r2 == (pow(2 * p, e2, n) + pow(-3 * q, e2, n)) % n

    h1 = pow(r1, e2, n) * pow(-2, e1 * e2, n)
    h2 = pow(r2, e1, n)

    q = gcd(h1 + h2, n)
    if q > 1 and n % q == 0:
        return n // q, q
    else:
        return None, None


e1, e2, r2 = power1, power2, out2
for r1 in range(eq1, -1, -1):
    p, q = solve(e1, e2, r1, r2)
    if p and q:
        phi = (p - 1) * (q - 1)
        d = pow(eq1, -1, phi)
        flag = pow(c, d, n)
        print(long_to_bytes(flag))
        break
