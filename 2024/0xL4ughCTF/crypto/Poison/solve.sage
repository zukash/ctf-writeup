from Crypto.Util.number import *
from params import Ms, Xs, Ys, Zs

K = GF(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFF)
a = K(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFC)
b = K(0x64210519E59C80E70FA7E9AB72243049FEB8DEECC146B9B1)
E = EllipticCurve(K, (a, b))
G = E(
    0x188DA80EB03090F67CBF20EB43A18800F4FF0AFD82FF1012,
    0x07192B95FFC8DA78631011ED6B24CDD573F977A11E794811,
)

D = []
for i, (M, X, Y, Z) in enumerate(zip(Ms, Xs, Ys, Zs)):
    M, X, Y, Z = E(M), E(X), E(Y), E(Z)
    # p - p_
    diff = 1 << i
    for d in [diff, -diff]:
        if Z == M + d * X:
            D.append(d)

flag = 0
for i, d in enumerate(D):
    flag += (int(d > 0)) << i

print(long_to_bytes(flag))
# f4u1ty_3CC_EG_CR4CK3r!!!
