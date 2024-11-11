from sage.all import *
from Crypto.Util.number import *
from params import n, e, c

p = gcd(c[0][0], n)
q = n // p
assert p * q == n

d = pow(e, -1, (p - 1) * (q - 1))
c = matrix(Zmod(n), c)
mr = c**d
mr = matrix(ZZ, mr)

m1 = gcd(mr[1][1], mr[1][2])
m2 = gcd(mr[2][2], mr[2][3])

flag = long_to_bytes(m1) + long_to_bytes(m2)
print(flag)
