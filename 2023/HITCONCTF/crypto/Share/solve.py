from pwn import *
from sage.all import *


def get_shares(p, n):
    io.sendlineafter(b"p = ", str(p).encode())
    io.sendlineafter(b"n = ", str(n).encode())
    return eval(io.recvline().strip().split(b" = ")[1])


n = 14
io = process(["python", "server.py"])

A, P = [], []
p = next_prime(n + 1)
while prod(P) < 2**256:
    print(p)
    F = GF(p)["x"]
    S = set(range(p))
    while len(S) > 1:
        shares = get_shares(p, n)
        for s in list(S):
            poly = F.lagrange_polynomial(enumerate([s] + shares))
            if p - 1 in poly.coefficients()[1:]:
                S.remove(s)
    if not S:
        continue
    A.append(S.pop())
    P.append(p)
    p = next_prime(p)

print(A)
print(P)

secret = crt(A, P)
print(secret)
io.sendline(b"0")
io.sendline(b"0")
io.sendline(str(secret).encode())
io.interactive()
