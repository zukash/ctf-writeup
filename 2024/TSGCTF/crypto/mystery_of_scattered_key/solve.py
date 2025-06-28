from params import *
from itertools import product
from Crypto.Util.number import long_to_bytes

chunk_size = len(p_splitted)

stack = [(0, 0)]
for k in range(chunk_size):
    nstack = []
    for cp, cq in stack:
        for p, q in product(p_splitted, q_splitted):
            np = cp + p * (256 ** (2 * k))
            nq = cq + q * (256 ** (2 * k))
            if (N - np * nq) % (256 ** (2 * k + 2)) == 0:
                nstack.append((np, nq))
    stack = nstack

p, q = stack.pop()
assert p * q == N
phi = (p - 1) * (q - 1)
e = 0x10001
d = pow(e, -1, phi)
m = pow(c, d, N)
print(long_to_bytes(m))
