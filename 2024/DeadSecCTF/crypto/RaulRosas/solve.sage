from Crypto.Util.number import long_to_bytes
from params import n1, n2, c1, c2

n1, n2 = map(Integer, [n1, n2])

cf = continued_fraction(n1 / n2)
for conv in cf.convergents():
    k = conv.numerator()
    d = conv.denominator()
    if k.bit_length() == d.bit_length() == 300:
        q1, q2 = k, d
        break

p1 = (n1 // q1) ^ (1 / 2)
p2 = (n2 // q2) ^ (1 / 2)

assert p1 * p1 * q1 == n1
assert p2 * p2 * q2 == n2

e = 65537
d1 = pow(e, -1, p1 * (p1 - 1) * (q1 - 1))
m1 = pow(c1, d1, n1)

print(long_to_bytes(m1))
