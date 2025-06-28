from sage.all import *


def babai_cvp(B, w):
    n = B.nrows()
    BB, _ = B.gram_schmidt()
    e = w
    for i in range(n)[::-1]:
        c = (e.dot_product(BB[i]) / BB[i].dot_product(BB[i])).round()
        e -= c * B[i]
    return w - e


def kannan_cvp(B, w):
    n = B.nrows()
    M = 1
    BB = block_matrix([[B, matrix(ZZ, n, 1)], [w, M]])
    BB = BB.LLL()
    e = matrix(BB[0][0:n])
    return w - e


def solve_LWE(A, b):
    m = A.nrows()
    n = A.ncols()
    q = A.base_ring().order()
    BB = block_matrix([[A.change_ring(ZZ).transpose()], [q * matrix.identity(m)]])
    BB = BB.LLL()[n:]
    v = babai_cvp(BB, b.change_ring(ZZ))
    s = v[:n] * A[:n].transpose() ** (-1)
    return s


q = 29
A = matrix(
    GF(q),
    [
        [1, 5, 21, 3, 14],
        [17, 0, 12, 12, 13],
        [12, 21, 15, 6, 6],
        [4, 13, 24, 7, 16],
        [20, 9, 22, 27, 8],
        [19, 8, 19, 3, 1],
        [18, 22, 4, 8, 18],
        [6, 28, 9, 5, 18],
        [10, 11, 19, 18, 21],
        [28, 18, 24, 27, 20],
    ],
)
e = vector(GF(q), [0, 0, 0, 0, 0, 1, 0, 0, 0, 1])
s = vector(GF(q), [7, 27, 14, 23, 26])
b = A * s + e

del s, e

s = solve_LWE(A, b)
e = b - A * s

print(s)
print(e)
assert A * s + e == b
