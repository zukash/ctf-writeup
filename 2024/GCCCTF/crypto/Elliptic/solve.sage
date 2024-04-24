import json
from pwn import *
from tqdm import trange
from sage.modules.free_module_integer import IntegerLattice
from Crypto.Util.number import *
from flag import flag


# def solve_knapsack_problem(A, k, m):
#     n = len(A)
#     M = [[0] * (n + 1) for _ in range(n + 1)]
#     for i in range(n):
#         M[i][i] = 2
#     for i in range(n):
#         M[i][-1] = A[i] * m
#     for i in range(n):
#         M[-1][i] = -1
#     M[-1][-1] = -k * m
#     print(*M, sep="\n")

#     return matrix(M).LLL()
#     # return IntegerLattice(M).shortest_vector()


def solve_knapsack_problem(A, k):
    n = len(A)
    M = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        M[i][i] = 1
    for i in range(n):
        M[i][-1] = A[i]
    M[-1][-1] = -k

    return matrix(M).LLL()[0]


# ref. https://zenn.dev/anko/articles/ctf-crypto-ellipticcurve

# ******************************************
# Anomalous な楕円曲線を ecgen で生成
# https://github.com/J08nY/ecgen
# ******************************************
p = 0x9E811B62DBB14FA5CCD4C4549C04E1505DABD9D50EE78DCE7537EBF6223A89592628E806203020543127C38C73C8CF17B606B9318F730DAE8C10FF1DDFCFD809
a = 0x0A43F286202517F905C285C6C764A27806FAAC314BA5A7D6D885A928292F3BED181C6BDD60F1C99AB7228364E53557FB4A9450F976727A58548BC56562A7CD13
b = 0x815CF08AB70C9E4FCEB5BD81D45637EB0C525EEB9AE92B8CA1C131BAB0C3353F7A559B8E6892016F70225D8BABD5A2EB7AF4F5D8134604D8D1662CD42BF98651
E = EllipticCurve(GF(p), [a, b])
G = E.gens()[0]

# ******************************************
# test
# ******************************************
x = random_prime(p)
X = G * x
print(X)
# 高速に計算できること
assert x == G.discrete_log(X)
print(x)

# ******************************************
# test
# ******************************************
io = process(["sage", "chall.sage"])
# io = remote("challenges1.gcc-ctf.com", "4000")

io.sendlineafter(b"p = ", str(p).encode())
io.sendlineafter(b"a = ", str(a).encode())
io.sendlineafter(b"bl = ", str(b).encode())

# ******************************************
# F_p に持ってくる
# ******************************************
points = json.loads(io.recvline())["values"]
points = [E(point) for point in points]
S = E(eval(io.recvline()))
points = [G.discrete_log(X) % p for X in points]
s = G.discrete_log(S) % p
print(len(points))

# flag = solve_knapsack_problem(points + [p], s, int(len(points) ** 0.5))


flag_int = bytes_to_long(flag.lstrip(b"GCC{").rstrip(b"}"))

bin_flag = [int(val) for val in bin(flag_int)[2:]]
t = 0
for i, val in enumerate(bin_flag):
    if val == 1:
        t += points[i]
print(t)
print(divmod(t, p))
print(s)

while True:
    flag = solve_knapsack_problem(points, s)
    if all(x in [0, 1] for x in flag[:-1]):
        print("found!")
        print(flag)
        flag = long_to_bytes(int("".join(map(str, flag[:-1])), 2))
        print(flag)
        exit()

    # for flag in flags:
    #     if all(x in [-1, 1] for x in flag[:-1]):
    #         print("found!")
    #         print(flag)
    #         exit()
    s += p
    print(s // p, s)


print(flag)
io.interactive()
