from json import dump as json_dump
from random import randint
from mpmath import mp
from Crypto.Util.number import bytes_to_long, getPrime, GCD, long_to_bytes
from sympy import symbols, solve


size = 768 // 8
eps = 1e-20


def pad(data, length):
    if len(data) >= length:
        raise ValueError("length of data is too large.")
    pad_data = bytes([randint(1, 255) for _ in range(length - len(data) - 1)])
    return pad_data + b"\x00" + data


mp.dps = 8 * size * 16

p = getPrime(8 * size)
q = getPrime(8 * size)
e = 3
while GCD(q - 1, e) != 1 or GCD(p - 1, e) != 1:
    p = getPrime(8 * size)
    q = getPrime(8 * size)

if p > q:
    p, q = q, p

p_n = mp.fdiv(mp.mpf(str(1)), mp.mpf(p))
q_n = mp.mpf(q)
n = mp.fmul(p_n, q_n)
assert mp.almosteq(p_n * p, 1, eps)
assert mp.almosteq(q_n, q, eps)
assert mp.almosteq(n * p, q, eps)

flag = open("flag.txt", "rb").read().strip()
flag = bytes_to_long(pad(flag, size - 1))

assert flag < q

ciphertext = pow(flag, e) % n

########################################################
# p, q が既知のとき、flagを復元できるか
########################################################

# print(f"{str(n)=}")
# print(f"{str(e)=}")
# print(f"{str(ciphertext)=}")

# pm3 = p * pow(flag, 3)
pc = int(mp.nint(ciphertext * p))
qc = int(mp.nint(ciphertext * q))
# assert mp.almosteq(pm3 % q, pc, eps)

assert pow(flag, 3) % q == mp.nint(pc * pow(p, -1, q) % q)
# assert pow(flag, 3) % p == mp.nint(qc * pow(q, -1, p) % p)

# print(pow(flag, 3) % p)
# print(qc * pow(q, -1, p) % p)

# x = symbols("x")

# # 連立合同式を定義
# eq1 = x % 3 - 2
# eq2 = x % 5 - 2

# # 連立合同式を解く
# solutions = solve((eq1, eq2), x)
# print(solutions)


f3 = int(mp.nint(pc * pow(p, -1, q) % q))
print(f3)
print(q)
assert f3 == pow(flag, 3, q)
d = pow(e, -1, q - 1)
assert flag == pow(f3, d, q)
print(long_to_bytes(pow(f3, d, q)))
# d = pow(e, -1, (p - 1) * (q - 1))

# print(f3)
# print(d)
# assert flag == pow(f3, d, p * q)

# # assert predict == flag
# # p, q が分かれば、p * c * pow(p, -1, q) で m ** 3 が得られる
# # あとは普通のRSA暗号のように復号できる


# # json_dump(
# #     {
# #         'n': str(n),
# #         'e': str(e),
# #         'c': str(ciphertext),
# #     },
# #     open('output.txt', 'w')
# # )
