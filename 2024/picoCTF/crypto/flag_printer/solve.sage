n = int(input())
X = [*map(int, input().split())]
Y = [*map(int, input().split())]
points = [(x, y) for x, y in zip(X, Y)]

n = 50000
points = points[:n]

Fp = GF(7514777789)
# Fp = GF(998244353)
R = PolynomialRing(Fp, "x")
f = R.lagrange_polynomial(points)

# print(points)
print(*list(f))
