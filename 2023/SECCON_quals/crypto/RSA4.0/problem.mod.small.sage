"""
関係ありそう
* https://ctftime.org/writeup/8676
"""

import os

from Crypto.Util.number import bytes_to_long, getStrongPrime
import tqdm

m = bytes_to_long(os.getenvb(b"FLAG", b"f"))
m = 30
e = 0x10001
# p = getStrongPrime(1024, e=e)
# q = getStrongPrime(1024, e=e)
p = next_prime(60)
q = next_prime(p)
n = p * q
print(n)
assert m < n
Q = QuaternionAlgebra(Zmod(n), -1, -1)
i, j, k = Q.gens()
M = (
    1 * m
    + (3 * m + 1 * p + 337 * q) * i
    + (3 * m + 13 * p + 37 * q) * j
    + (7 * m + 133 * p + 7 * q) * k
)
enc = M ** e
print(f"{n = }")
print(f"{e = }")
print(f"{enc = }")

#####################
print(f"{p = }")
print(f"{q = }")
print(f"{m = }")
print(f"{M = }")
print(f"{M**2 = }")
print(f"{M**3 = }")
print((p ** 2 - 1) * (q ** 2 - 1))

# for i in tqdm.trange(n, n * n):
#     if (M ** i)[0] == m and i % n == 0:
#         print(i)

for i in tqdm.trange(n):
    if (M ** (i * n))[0] == m:
        print(i)


# phi = (p - 1) * (q - 1) // 2
# d = pow(e, -1, phi)

a = 1 * m
b = 3 * m + 1 * p + 337 * q
c = 3 * m + 13 * p + 37 * q
d = 7 * m + 133 * p + 7 * q
# Mp = matrix(Zmod(p), [[a, -b, -c, d], [b, a, -d, -c], [c, d, a, b], [-d, c, -b, a]])
# op = Mp.multiplicative_order()

# Mq = matrix(Zmod(q), [[a, -b, -c, d], [b, a, -d, -c], [c, d, a, b], [-d, c, -b, a]])
# oq = Mq.multiplicative_order()

# print(p, op)
# print(q, oq)
# assert M ** (op * oq) == 1

assert M ** ((p ** 2 - 1) * (q ** 2 - 1)) == 1
assert (p ** 2 - 1) * (q ** 2 - 1) == (n + 1) ** 2 - (p + q) ** 2
d = pow(e, -1, (n + 1) ** 2 - (p + q) ** 2)
assert M == enc ** d

# Me = M ** e
# # print(Me.multiplicative_order())
# print(Me ** d == M)

print(factor(p - 1))
print(factor(p + 1))
