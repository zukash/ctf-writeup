from sage.all import *
from flag import flag
from Crypto.Util.number import bytes_to_long
import random

# from ecpy import SSSA_Attack


rng = random.SystemRandom()
secret = bytes_to_long(flag + rng.randbytes(1024 // 8 - 1 - len(flag)))


a, b = [
    0x1C456BFC3FABBA99A737D7FD127EAA9661F7F02E9EB2D461D7398474A93A9B87,
    0x8B429F4B9D14ED4307EE460E9F8764A1F276C7E5CE3581D8ACD4604C2F0EE7CA,
]
X, Y, Z = (
    92512155407887452984968972936950900353410451673762367867085553821839087925110135228608997461366439417183638759117086992178461481890351767070817400228450804002809798219652013051455151430702918340448295871270728679921874136061004110590203462981486702691470087300050508138714919065755980123700315785502323688135,
    40665795291239108277438242660729881407764141249763854498178188650200250986699,
    1,
)

p = 0xD9D35163A870DC6DFB7F43911FF81C964DC8E1DD2481FDF6F0E653354B59C5E5
ec = EllipticCurve(Zmod(p**4), [a, b])
P = ec.point((X, Y, Z))
Q = P * secret
# print((secret * P).xy())

# EC = EllipticCurve(Zmod(p), [a, b])
# _P = EC.point((X, Y, Z))
# _Q = EC.point((*Q.xy(), 1))
# print(_P)
# print(_Q)

# assert _P * secret == _Q


# def SmartAttack(P, Q, p):
#     E = P.curve()
#     Eqp = EllipticCurve(Qp(p, 2), [ZZ(t) + randint(0, p) * p for t in E.a_invariants()])

#     P_Qps = Eqp.lift_x(ZZ(P.xy()[0]), all=True)
#     for P_Qp in P_Qps:
#         if GF(p)(P_Qp.xy()[1]) == P.xy()[1]:
#             break

#     Q_Qps = Eqp.lift_x(ZZ(Q.xy()[0]), all=True)
#     for Q_Qp in Q_Qps:
#         if GF(p)(Q_Qp.xy()[1]) == Q.xy()[1]:
#             break

#     p_times_P = p * P_Qp
#     p_times_Q = p * Q_Qp

#     x_P, y_P = p_times_P.xy()
#     x_Q, y_Q = p_times_Q.xy()


#     phi_P = -(x_P / y_P)
#     phi_Q = -(x_Q / y_Q)
#     k = phi_Q / phi_P
#     return ZZ(k)
def SmartAttack(P, Q, p):
    E = P.curve()
    Eqp = EllipticCurve(
        Qp(p, 5), [ZZ(t) + randint(0, p) * (p**4) for t in E.a_invariants()]
    )
    P_Qps = Eqp.lift_x(ZZ(P.xy()[0]), all=True)
    for P_Qp in P_Qps:
        if GF(p)(P_Qp.xy()[1]) == P.xy()[1]:
            break
    Q_Qps = Eqp.lift_x(ZZ(Q.xy()[0]), all=True)
    for Q_Qp in Q_Qps:
        if GF(p)(Q_Qp.xy()[1]) == Q.xy()[1]:
            break
    p_times_P = p * P_Qp
    p_times_Q = p * Q_Qp
    x_P, y_P = p_times_P.xy()
    x_Q, y_Q = p_times_Q.xy()
    phi_P = -(x_P / y_P)
    phi_Q = -(x_Q / y_Q)
    k = phi_Q / phi_P
    return ZZ(k)


# print(secret % p)
secret = SmartAttack(P, Q, p)
print(bytes.fromhex(f"{int(secret):x}")[:36])

# # _secret = SmartAttack(P, Q, p)
# _secret = SmartAttack(_P, _Q, p)
# print(_secret)
# assert _P * _secret == _Q
# assert P * secret == Q
# assert P * _secret == Q

# assert _secret == secret

# s = SSSA_Attack(GF(p), EC, P, Q)
# print(s)
