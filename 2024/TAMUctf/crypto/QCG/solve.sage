from pwn import *
from secrets import randbelow
from math import gcd
from Crypto.Util.number import getPrime


class QCG:
    def __init__(self, m, a, b, c, x):
        self.m = m
        self.a = a
        self.b = b
        self.c = c
        self.x = x

    def __call__(self):
        self.x = (self.a * self.x**2 + self.b * self.x + self.c) % self.m
        return self.x


def inverse(a, m):
    return pow(a, -1, m)


def solve():
    # io = process(["python", "qcg.py"])
    io = remote("tamuctf.com", "443", ssl=True, sni="qcg")

    X = []
    for i in range(10):
        X.append(int(io.recvline().strip()))

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

    # print(X)
    # print(g)

    # assert g % m == 0
    # そこそこの確率で g == m * 2 になる
    # assert g == m * 2
    m = g // 2

    # そこそこの確率で inverse を持つ
    a = Y[1] * inverse((X[3] - X[2]) * (X[2] - X[1]) * (X[3] - X[1]), m) % m
    print(f"{a = }")

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

    qcg = QCG(m, a, b, c, X[0])

    for i in range(1, 10):
        x = qcg()
        print(X[i], x)
        assert X[i] == x

    for _ in range(5):
        guess = qcg()
        io.sendline(str(guess))

    io.interactive()
    io.close()
    return None


solve()
