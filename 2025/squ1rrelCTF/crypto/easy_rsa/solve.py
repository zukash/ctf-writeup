import math


def fermat_factor(n):
    """
    n = p * q where p and q are close.
    Tries to find p and q using Fermat's factorization.
    """
    a = math.isqrt(n)
    if a * a < n:
        a += 1

    b2 = a * a - n
    while not is_perfect_square(b2):
        a += 1
        b2 = a * a - n

    b = math.isqrt(b2)
    p = a - b
    q = a + b

    assert p * q == n
    return p, q


def is_perfect_square(n):
    root = math.isqrt(n)
    return root * root == n


from sympy import mod_inverse


def decrypt(ciphertext, n, e):
    p, q = fermat_factor(n)
    return p, q
    print(p, q)
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    message_int = pow(ciphertext, d, n)
    message_bytes = message_int.to_bytes((message_int.bit_length() + 7) // 8, "big")
    return message_bytes.decode()


from params import n, e, c
from Crypto.Util.number import long_to_bytes

# print(decrypt(c, n, e))

p, q = (
    162844969802793369991428601458295181570536706599609454664094976374150994306422002904013120826461924570049490132847808181540893008813305140934077173993221511741114503090171789361722157385749936254368680979467760601708231528381466644171627681117469122398345322805274888367547624418417938030736404407437613225877,
    162844969802793369991428601458295181570536706599609454664094976374150994306422002904013120826461924570049490132847808181540893008813305140934077173993327436461912048726815700038563854363515704550897541580442036450232099126331779281555115480827104127689657088570096620633332930485612118325060906186228586482019,
)

phi = (p - 1) * (q - 1)
d = mod_inverse(e, phi)
m = pow(c, d, n)
print(m)
print(long_to_bytes(m))

# message_int = int.from_bytes(message.encode(), "big") の逆演算
# message = long_to_bytes(message_int)

# message_int = int.from_bytes(message.encode(), "big")
# ciphertext = pow(message_int, e, n)
