from Crypto.Util.number import *
from sympy import nextprime


# from decimal import *

# getcontext().prec = int(200)


p1 = bin(getPrime(1024))[2:]
p2 = p1[:605]
p2 = p2 + ("0" * (len(p1) - len(p2)))

# print(p1)
# print(p2)

p1 = int(p1, 2)
p2 = nextprime(int(p2, 2))
n = p1 * p2

q1 = getPrime(300)
q2 = getPrime(300)

# n = p1 * p2 = (m + a) * (m - a)

n1 = p1 * p1 * q1
n2 = p2 * p2 * q2

print(n1 / n2)

print(q1)
print(q2)

cf = continued_fraction(Integer(n1) / Integer(n2))
print(cf.convergent(100))
for conv in cf.convergents():
    k = conv.numerator()
    d = conv.denominator()
    if set([k, d]) == set([q1, q2]):
        print("Found")
        break


# exponent = Decimal(1024) / Decimal(4696)
# # exponent = Decimal(1) / Decimal(4)
# print(exponent)
# print((n1 * n2).bit_length())
# p = Decimal(n1 * n2) ** exponent
# print(int(p))

# # 1024 + 1024 + 300
# # (1024 + 1024 + 300) * 2 = 4696


# # n1 * n2 = p1*p1*p2*p2*q1*q2 = (m + a) * (m + a) * (m - a) * (m - a) * q1 * q2 = (m^2 - a^2) ^ 2 * q1 * q2
# # = m^4 * q1 * q2 - 2 * m^2 * a^2 * q1 * q2 + a^4 * q1 * q2

# m = (p1 + p2) // 2
# a = (p1 - p2) // 2
# assert m + a == p1
# assert m - a == p2
# assert n1 * n2 % ((m - a) * (m + a)) ** 2 == 0
# print(m)

# import sys


# def isqrt(n):
#     x = n
#     y = (x + 1) // 2
#     while y < x:
#         x = y
#         y = (x + n // x) // 2
#     return x


# def is_square(n):
#     if not n % 48 in (0, 1, 4, 9, 16, 25, 33, 36):
#         return False

#     x = isqrt(n)
#     return x * x == n


# def fermat(n):
#     a = isqrt(n)
#     b2 = a * a - n
#     while not is_square(b2):
#         a += 1
#         b2 = a * a - n
#     return a - isqrt(b2)


# p = fermat(n)
# q = n // p
# assert set([p1, p2]) == set([p, q])
