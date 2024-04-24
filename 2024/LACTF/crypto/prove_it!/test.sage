import random


def lattice_algorithm(A, k):
    n = len(A)
    M = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        M[i][i] = 1
    for i in range(n):
        M[i][-1] = A[i]
    M[-1][-1] = -k

    L = matrix(M).LLL()[0]
    return L


g = random.getrandbits(10)
a = random.getrandbits(10)
s = random.getrandbits(10)
p = 10**9 + 7


T = [1, 2, 3, 4, 5, 6, 7, 8]
GS = [pow(g, s**i, p) for i in range(1, 8)]
GAS = [pow(g, a * s**i, p) for i in range(1, 8)]

ST = [(pow(s, 7 - i, p) * T[i]) % p for i in range(8)]
sumST = sum(ST) % p

lattice_algorithm(T + [sumST, 1], 0)


# f, fa = 1, 1
# for gs, gas, t in zip(GS, GAS, T[-2::-1]):
#     print(gs, gas, t)
#     f *= pow(gs, t, p)
#     fa *= pow(gas, t, p)
# f %= p
# fa %= p


# assert f == pow(g, sumST - T[-1], p)


# e = (sumST - T[-1]) % (p - 1)
# assert pow(g, e, p) == f
# d = pow(sumST - T[-1], -1, p - 1)
# assert pow(g, (sumST - T[-1]) * d, p) == g
# assert g == pow(f, d, p)

# assert pow(f, a, p) == fa
# assert f == pow(g, sumST - T[-1], p)
