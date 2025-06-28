#!/usr/bin/env python3
from lib import *

A = str_to_point("O")
B = str_to_point("O")
C = str_to_point("O")


def e(X, Y):
    return X.weil_pairing(Y, field_size)


# 性質の整理
assert e(str_to_point("O"), CRSTrap1[0]) == 1
assert e(3 * CRSTrap1[0], 2 * CRSTrap2[0]) == e(CRSTrap1[0], CRSTrap2[0]) ** 6
assert e(CRSTrap1[0], CRSTrap2[0]) != e(CRSTrap2[0], CRSTrap1[0])

# commit の整理
assert CRS1[0] == tau**0 * G1 == G1
assert CRS1[1] == tau**1 * G1
assert CRS1[2] == tau**2 * G1
assert CRS1[3] == tau**3 * G1

Rng = PolynomialRing(Fp, "x")
P = Rng.random_element(degree=3)
assert (
    commit(P, CRS1) == P[0] * CRS1[0] + P[1] * CRS1[1] + P[2] * CRS1[2] + P[3] * CRS1[3]
)
assert commit(P, CRS1) == sum(P[i] * tau**i for i in range(4)) * G1

Q = Rng.random_element(degree=3)
assert commit(Q, CRS2) == sum(Q[i] * tau**i for i in range(4)) * G2

assert e(commit(P, CRS1), commit(Q, CRS2)) == e(G1, G2) ** (
    sum(P[i] * tau**i for i in range(4)) * sum(Q[i] * tau**i for i in range(4))
)
assert e(commit(P, CRS1), commit(Q, CRS2)) == e(G1, G2) ** (P * Q)(tau)

# verify の整理


A = alpha * G1
B = beta * G2
C = str_to_point("O")
assert verify_proof(None, None, None, A, B, C)
assert e(A, B) == e(CRSTrap1[0], CRSTrap2[0]) * e(C, CRSTrap2[2])

assert e(CRSTrap1[0], CRSTrap2[0]) == e(alpha * G1, beta * G2)
assert e(alpha * G1, beta * G2) == e(G1, G2) ** (alpha * beta)

assert e(A, B) == e(alpha * G1, beta * G2) * e(C, delta * G2)
assert e(A, B) == e(G1, G2) ** (alpha * beta) * e(C, delta * G2)

print(e(G1, G2))

print(A)
X = str_to_point("(2555, 306)")
print(X)
# str_to_point("")

# left_pairing = A.weil_pairing(B, field_size)
# right_pairing = CRSTrap1[0].weil_pairing(CRSTrap2[0], field_size) * C.weil_pairing(
#     CRSTrap2[2], field_size
# )


# def generate_challenge():
#     Rng = PolynomialRing(Fp, "x")

#     # create L/R polynomials
#     L_poly = Rng.random_element(degree=3)
#     R_poly = Rng.random_element(degree=3)

#     # ensure L*R != Q
#     true_Q_poly = L_poly * R_poly

#     # commitments
#     L_commit = commit(L_poly, CRS1)
#     R_commit = commit(R_poly, CRS2)
#     Q_commit = commit(true_Q_poly, CRS1)

#     return L_commit, R_commit, Q_commit


# L, R, Q = generate_challenge()

# print(verify_proof(None, None, None, L, R, Q))
