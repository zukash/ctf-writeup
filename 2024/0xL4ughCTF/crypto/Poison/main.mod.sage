from random import *
from Crypto.Util.number import *

flag = b"X"
# DEFINITION
K = GF(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFF)
a = K(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFC)
b = K(0x64210519E59C80E70FA7E9AB72243049FEB8DEECC146B9B1)
E = EllipticCurve(K, (a, b))
G = E(
    0x188DA80EB03090F67CBF20EB43A18800F4FF0AFD82FF1012,
    0x07192B95FFC8DA78631011ED6B24CDD573F977A11E794811,
)


# DAMAGE
def poison(val, index):
    val = list(val)
    if val[index] == "1":
        val[index] = "0"
    else:
        val[index] = "1"
    return "".join(val)


my_priv = bin(bytes_to_long(flag))[2:]
Ms = []
Xs = []
Ys = []
Zs = []

count = 0

# my_priv = '1011000'
while count < len(my_priv):
    try:
        k = randint(2, G.order() - 2)
        Q = int(my_priv, 2) * G
        print(Q)
        M = randint(2, G.order() - 2)
        M = E.lift_x(Integer(M))
        Ms.append((M[0], M[1]))

        X = k * G
        Xs.append((X[0], X[1]))
        Y = M + k * Q
        Ys.append((Y[0], Y[1]))

        ind = len(my_priv) - 1 - count
        new_priv = poison(my_priv, ind)
        new_priv = int(new_priv, 2)
        Z = Y - (new_priv) * X
        Zs.append((Z[0], Z[1]))
        p = int(my_priv, 2)
        p_ = new_priv
        # めっちゃ重要
        # p - p_ の種類数は 2
        assert Z - M == (p - p_) * X

        count += 1
    except ValueError:
        pass

print(f"Ms={Ms}\n")
print(f"Xs={Xs}\n")
print(f"Ys={Ys}\n")
print(f"Zs={Zs}")
