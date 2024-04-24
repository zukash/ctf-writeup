import numpy as np
import random

# **************************************************
# 多項式との対応
# **************************************************
n = 200
MM = [[0] * n for _ in range(n)]
Fp = GF(7514777789)
# 998244353
# 7514777789
V = vector([Fp.random_element() for _ in range(n)])
points = []
for i in range(n):
    for j in range(n):
        MM[i][j] = Fp(i) ** j
    points.append((i, V[i]))

MM = matrix(MM)
C = MM.inverse() * V

# R = PolynomialRing(Fp, "x")
# f = R.lagrange_polynomial(points)
# assert list(C) == list(f.coefficients())

# print(points)
# print(f)

print(len(points))
print(*[x for x, y in points])
print(*[y for x, y in points])
print(*C)

# **************************************************
# points を全て通る多項式を高速に計算する
# **************************************************

# x座標が等差になっていることを利用
# https://37zigen.com/lagrange-interpolation/
