from sage.all import *
import secrets


q = 2**20
# n = 512
n = 64
m = 4 * n
c = 8

with open("flag.txt", "rb") as f:
    FLAG = f.read().strip()


def trunc_matrix(M, c):
    F = M.base_ring()
    modulus = 2**c
    return matrix(
        F,
        M.nrows(),
        M.ncols(),
        [F(Integer(x) - (Integer(x) % modulus)) for x in M.list()],
    )


def keygen():
    U = random_matrix(Integers(q), m, n)
    A = trunc_matrix(U, c)
    s = vector(Zmod(q), [secrets.randbelow(q) for _ in range(n)])
    e = vector(Zmod(q), [ZZ(secrets.randbelow(400)) for _ in range(m)])
    # NOTE: debug
    return A, A * s + e, s, e


def encrypt_bit(x, A, b):
    S = [i for i in range(A.nrows()) if secrets.randbits(1)]
    if len(S) == 0:
        S = [secrets.randbelow(A.nrows())]
    a_sum = sum([A[i] for i in S])
    b_sum = sum([b[i] for i in S])
    encoded_bit = (x * (q // 2)) % q
    # NOTE: debug
    return (a_sum, (encoded_bit + b_sum) % q, S)


def encrypt_message(message, A, b):
    bits = []
    for byte in message:
        for i in range(8):
            bits.append((byte >> i) & 2)
    ciphertext = [encrypt_bit(bit, A, b) for bit in bits]
    return ciphertext


A, b, s, e = keygen()

a_sum, b_sum, S = encrypt_bit(0, A, b)
diff = b_sum - a_sum
print(diff)
print(diff >> 8)

# for i in range(n):
#     if b_sum == a_sum + 256 * i:
#         print(f"i = {i}, b_sum = {b_sum}, a_sum = {a_sum}")
#         break


# assert A * s == b - e
# assert all(aij % 128 == 0 for aij in A.list())
# assert all(aij % 128 == 0 for aij in (A * s).list())
# # assert all(bi % 128 == 0 for bi in b)
# A_ = matrix([[aij >> 8 for aij in row] for row in A])
# b_ = vector([b[i] >> 8 for i in range(m)])


# # assert all(aij % 128 == 0 for aij in (A_ * s).list())
# # assert all(bi % 128 == 0 for bi in b_)

# X = vector([x * 256 for x in A_ * s])
# Y = vector([y * 256 for y in b_])

# assert all(x % 256 == 0 for x in X)
# assert all(y % 256 == 0 for y in Y)


# print(Y - X)


# # A * s == (A >> 8 << 8) * s
# assert A * s == A_ * s

# # A * s == ((A >> 8) * s) << 8
# A_ = matrix([[aij >> 8 for aij in row] for row in A])
# B = vector(bi << 8 for bi in A_ * s)
# assert A * s == B


# a_sum, b_sum, S = encrypt_bit(0, A, b)

# b = list(map(int, b))
# b_sum = int(b_sum)
# div, mod = divmod(sum([b[i] for i in S]), q)
# print(f"div: {div}, mod: {mod}")
# assert mod == b_sum
# T = subset_sum_problem(b, q * div + mod, verbose=False)


# print(S)
# print(T)
