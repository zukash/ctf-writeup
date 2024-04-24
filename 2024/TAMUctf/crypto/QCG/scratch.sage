from secrets import randbelow
from math import gcd
from Crypto.Util.number import getPrime


def inverse(a, m):
    return pow(a, -1, m)


class MyQCG:
    def __init__(self, m, a, b, c, x):
        self.m = m
        self.a = a
        self.b = b
        self.c = c
        self.x = x

    def __call__(self):
        self.x = (self.a * self.x**2 + self.b * self.x + self.c) % self.m
        return self.x


class QCG:
    def __init__(self):
        # self.m = randbelow(pow(2, 256) - 1)
        self.m = getPrime(256)
        self.a = randbelow(self.m - 1)
        self.b = randbelow(self.m - 1)
        self.c = randbelow(self.m - 1)
        self.x = randbelow(self.m - 1)

    def __call__(self):
        self.x = (self.a * self.x**2 + self.b * self.x + self.c) % self.m
        return self.x


qcg = QCG()

m, a, b, c, x = qcg.m, qcg.a, qcg.b, qcg.c, qcg.x
print(f"m: {qcg.m}")
print(f"a: {qcg.a}")
print(f"b: {qcg.b}")
print(f"c: {qcg.c}")
print(f"x: {qcg.x}")

X = []
for i in range(10):
    X.append(qcg())

# a * (X[2] - X[1]) * (X[1] - X[0]) * (X[2] - X[0])
Y = [
    (X[i + 3] - X[i + 2]) * (X[i + 1] - X[i + 0])
    - (X[i + 2] - X[i + 1]) * (X[i + 2] - X[i + 1])
    for i in range(6)
]


# Y[1] = a * (X[3] - X[2]) * (X[2] - X[1]) * (X[3] - X[1])
# Y[0] = a * (X[2] - X[1]) * (X[1] - X[0]) * (X[2] - X[0])
# Y[1] * (X[1] - X[0]) * (X[2] - X[0]) - Y[0] * (X[3] - X[2]) * (X[3] - X[1]) == 0 (mod m)
Z = [
    Y[i + 1] * (X[i + 1] - X[i + 0]) * (X[i + 2] - X[i + 0])
    - Y[i + 0] * (X[i + 3] - X[i + 2]) * (X[i + 3] - X[i + 1])
    for i in range(5)
]
g = 0
for i in range(5):
    g = gcd(g, Z[i])

# assert g % m == 0
# そこそこの確率で g == m * 2 になる
assert g == m * 2
m = g // 2
a = Y[1] * inverse((X[3] - X[2]) * (X[2] - X[1]) * (X[3] - X[1]), m) % m
print(f"{a = }")

assert (X[1] - a * X[0] ** 2) % m == (b * X[0] + c) % m
assert (X[1] - X[0]) * c % m == (
    X[1] * (X[1] - a * X[0] ** 2) - X[0] * (X[2] - a * X[1] ** 2)
) % m

# X[1] - a * X[0] ** 2 = b * X[0] + c
# X[2] - a * X[1] ** 2 = b * X[1] + c
# (X[1] - X[0]) * c == X[1] * (X[1] - a * X[0] ** 2) - X[0] * (X[2] - a * X[1] ** 2)


c = (
    (X[1] * (X[1] - a * X[0] ** 2) - X[0] * (X[2] - a * X[1] ** 2))
    * inverse(X[1] - X[0], m)
    % m
)
b = (X[1] - a * X[0] ** 2 - c) * inverse(X[0], m) % m
print(f"{b = }")
print(f"{c = }")

qcg = MyQCG(m, a, b, c, X[0])
for i in range(1, 10):
    x = qcg()
    assert X[i] == x

# X = X[::-1]
# x = X.pop()
# MM = []
# V = []
# for _ in range(3):
#     M = [pow(x, i, m) for i in range(3)]
#     MM.append(M)
#     x = X.pop()
#     V.append(x)
# MM = matrix(GF(m), MM)
# V = vector(GF(m), V)
# C = MM.inverse() * V
# C = C[::-1]

# print(C)

# # correct = True
# # for i in range(5):
# #     guess = int(input())
# #     if guess != qcg():
# #         correct = False
# # if correct:
# #     print(open("flag.txt", "r").read())
# # else:
# #     print("You failed")
