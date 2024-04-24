import os

from Crypto.Util.number import bytes_to_long, getStrongPrime

m = bytes_to_long(os.getenvb(b"FLAG", b"FAKEFLAG{THIS_IS_FAKE}"))
e = 0x10001
p = getStrongPrime(1024, e=e)
q = getStrongPrime(1024, e=e)
n = p * q
assert m < n
Q = QuaternionAlgebra(Zmod(n), -1, -1)
i, j, k = Q.gens()
enc = (
    1 * m
    + (3 * m + 1 * p + 337 * q) * i
    + (3 * m + 13 * p + 37 * q) * j
    + (7 * m + 133 * p + 7 * q) * k
) ** e
print(f"{n = }")
print(f"{e = }")
print(f"{enc = }")

#####################
phi = (p - 1) * (q - 1) // 2
d = pow(e, -1, phi)

# 4回に1回くらい通る
assert (
    1 * m
    + (3 * m + 1 * p + 337 * q) * i
    + (3 * m + 13 * p + 37 * q) * j
    + (7 * m + 133 * p + 7 * q) * k
) == (enc ** d)


a = 1 * m
b = 3 * m + 1 * p + 337 * q
c = 3 * m + 13 * p + 37 * q
d = 7 * m + 133 * p + 7 * q
Mp = matrix(Zmod(p), [[a, -b, -c, d], [b, a, -d, -c], [c, d, a, b], [-d, c, -b, a]])
# Me = M ** e
# # print(M.multiplicative_order())
# # print(Me.multiplicative_order())
# print(Me ** d == M)
