from random import randint


def sequence_from_parameters(n, b, c, a0, a1, p, parameters):
    poly = parameters[0:2]
    phi = parameters[2:4]
    psi = parameters[4:6]
    const_phi = parameters[6:8]
    const_psi = parameters[8:10]

    Fp = GF(p)
    RFp = PolynomialRing(Fp, ["t"])
    F = GF(p**2, name="t", modulus=RFp(poly + [1]))
    phi = F(phi)
    psi = F(psi)
    const_phi = F(const_phi)
    const_psi = F(const_psi)

    answer = list(phi**n * const_phi - psi**n * const_psi)
    # print(phi**n * const_phi - psi**n * const_psi)
    if answer[1] != 0:
        print("That can't be right...")
        sys.exit(1)
    return int(answer[0])


def sequence_slow(n, b, c, a0, a1, p):
    if n == 0:
        return a0
    elif n == 1:
        return a1
    else:
        return (
            b * sequence_slow(n - 1, b, c, a0, a1, p)
            + c * sequence_slow(n - 2, b, c, a0, a1, p)
        ) % p


# *******************************************
# sequence_slow の理解
# *******************************************
# フィボナッチ数列みたいなやつを計算している
a0, a1 = 1, 1
b, c = 1, 1
p = 17
S = []
for i in range(10):
    S.append(sequence_slow(i, b, c, a0, a1, p))

T = [a0, a1]
while len(T) < 10:
    T.append((b * T[-1] + c * T[-2]) % p)

assert S == T

# *******************************************
# 形式的冪級数を使ったフィボナッチ数列の一般項の計算
# *******************************************
"""
https://maspypy.com/%e5%a4%9a%e9%a0%85%e5%bc%8f%e3%83%bb%e5%bd%a2%e5%bc%8f%e7%9a%84%e3%81%b9%e3%81%8d%e7%b4%9a%e6%95%b0%ef%bc%88%ef%bc%93%ef%bc%89%e7%b7%9a%e5%bd%a2%e6%bc%b8%e5%8c%96%e5%bc%8f%e3%81%a8%e5%bd%a2%e5%bc%8f#toc5
x_{n} = b * x_{n-1} + c * x_{n-2}
=> X - b * x * X - c * x^2 * X = d * x + e
=> X = (d * x + e) / (x^2 - b * x - c)
=> X = const_phi / (x - phi) + const_psi / (x - psi)
=> x_{n} = phi^n * const_phi - psi^n * const_psi
"""

# *******************************************
# √D not in F_p の場合
# *******************************************

"""
具体的にサーバーから与えられたパラメータ設定で解いてみる
"""
b = 0x948BAD202517323B
c = 0x65284069FF01680C
a0 = 0x3419EC98556CE484
a1 = 0x995FF7A98A146569
p = 0xACE3BE5919DD41C5

# 期待値
S = []
for i in range(10):
    S.append(sequence_slow(i, b, c, a0, a1, p))
    # S.append(sequence_slow(i, b, c, 1, 10703839292948951611, p))
print(S)

Fp = GF(p)
RFp = PolynomialRing(Fp, ["t"])
poly = [-(b**2 + 4 * c) % p, 0]
# 平方剰余を持たない
assert kronecker_symbol(poly[0], p) == -1
F = GF(p**2, name="t", modulus=RFp(poly + [1]))
assert F([0, 1]) ** 2 == -poly[0]

# t**2 - b * t - c == 0 の解
phi = F([b, 1]) / 2
psi = F([b, -1]) / 2
assert phi**2 - b * phi - c == 0
assert psi**2 - b * psi - c == 0

const_phi = (-a0 * psi + a1) / (phi - psi)
const_psi = (a0 * phi - a1) / (phi - psi)

T = []
for i in range(10):
    x = const_phi * phi**i + const_psi * psi**i
    T.append(list(x)[0])

print(T)
assert S == T

# *******************************************
# √D in F_p の場合
# *******************************************

"""
F_p 上に根が見つかる場合は、maspy さんの記事の通りに F_p 上で計算すればいい
"""
b = 6799208576352466067
c = 13035039845583016992
a0 = 4923220470979387349
a1 = 9598513012301594440
p = 13645872945611411381

# 期待値
S = []
for i in range(10):
    S.append(sequence_slow(i, b, c, a0, a1, p))
print(S)

Fp = GF(p)
RFp = PolynomialRing(Fp, ["t"])
poly = [-(b**2 + 4 * c) % p, 0]
roots = RFp(poly + [1]).roots()
print(roots)
assert len(roots) == 2

# irreducible な多項式を適当に一つ選ぶ
while True:
    poly = [randint(0, p - 1) for _ in range(2)]
    if RFp(poly + [1]).is_irreducible():
        break
F = GF(p**2, name="t", modulus=RFp(poly + [1]))

# t**2 - b * t - c == 0 の解
phi, psi = RFp([-c, -b, 1]).roots()
phi, psi = F([phi[0]]), F([psi[0]])
assert phi**2 - b * phi - c == 0
assert psi**2 - b * psi - c == 0

const_phi = (-a0 * psi + a1) / (phi - psi)
const_psi = (a0 * phi - a1) / (phi - psi)

T = []
for i in range(10):
    x = const_phi * phi**i + const_psi * psi**i
    T.append(list(x)[0])

print(T)
assert S == T
