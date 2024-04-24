from Crypto.Util.number import getStrongPrime
from Pedersen_commitments import gen, commit, verify
from Crypto.Random.random import randint


def gen():
    q = getStrongPrime(1024)

    g = randint(int(1), int(q - 1))
    s = randint(int(1), int(q - 1))
    h = pow(g, s, q)

    return q, g, h, s


# Verifiable Dice roll
def roll_dice(pk):
    roll = randint(1, 6)
    comm, r = commit(pk, roll)
    return comm, roll, r


# verifies a dice roll
def check_dice(pk, comm, guess, r):
    res = verify(pk, comm, r, int(guess))
    return res


q, g, h, s = gen()
pk = q, g, h

print(q)
print(GF(q)(h).multiplicative_order())
print(GF(q)(1).multiplicative_order())

# roll = 1
# comm, r = commit(pk, roll)
# x = comm * pow(g, -roll, q) % q
# inv_r = pow(r, -1, q - 1)
# x = pow(x, inv_r, q)
# assert pow(g, s, q) == x
# F = GF(q)
# print(F(x).order())
# print(f"{q = }")
# print(f"{g = }")
# print(f"{h = }")
# print(f"{s = }")

# print(f"{x = }")


# q = 10**9 + 7
# g = 2
# s = 12345
# r = 6789
# # (g ** (1 + s * r))
# # (g ** ((1 + s * r) * inv(s)))


# t = pow(g, 1 + s * r, q)
# print(t)
# inv_r = pow(r, -1, q - 1)
# x = t * pow(g, -1, q) % q
# assert x == pow(g, s * r, q)
# x = pow(x, inv_r, q)
# assert x == pow(g, s, q)


# # (g ** (1 + s * r))
# # g * (g ** (s * r))
# # → g ** s

# # print(pow(g, inv_s + r, q))


# # print(pow(t, inv_s, q))
# # print(pow(g, (1 + s * r) * inv_s, q))
# # print(pow(g, inv_s + s * r * inv_s, q))
# # print(pow(g, inv_s + 1, q))
# # print(pow(g, inv_s, q))
# # print(pow(g, s * inv_s, q))
