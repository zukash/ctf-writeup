import re
from pwn import *

io = remote("05.cr.yp.toc.tf", "11137")


class Oracle:
    def read(self):
        io.recvuntil(b"almost")
        problem = io.recvline()
        l, r = re.findall(rb"\((\d+), (\d+)\)-bits.", problem)[0]
        return int(l), int(r)

    def submit(self, ans):
        io.sendline(",".join(map(str, ans)))


oracle = Oracle()
l, r = oracle.read()
print(l, r)

p = next_prime(1 << l)
while True:
    print(p)
    q = var("q")
    f = 3 * q * q + 3 * q + 2 - p ** 3
    roots = f.roots()
    if roots[0][0].is_integer():
        q = roots[0][0]
        r = -(q + 1)
        print(q, r)
    p = next_prime(p)


# p = next_prime(1 << l)
# while True:
#     for d in divisors(p ^ 3 - 1):
#         x = var("x")
#         f = 3 * x * x + 3 * d * x + d * d
#         q, r = f.roots()
#         q, r = q[0], r[0]
#         if q.is_integer() and r.is_integer():
#             print(q, r)
#     p = next_prime(p)

# l, r = 6, 26

# p = next_prime(1 << l)
# while True:
#     for d in range(1, 100):
#         q = -(p + d)
#         # p^3 + q^3 + r^3 = 1
#         r3 = 1 - p ^ 3 - q ^ 3
#         r = int(r3 ^ (1 / 3))
#         if r ^ 3 == r3:
#             assert p ^ 3 + q ^ 3 + r ^ 3 == 1
#             print(p, q, r)
#             exit()
#     p = next_prime(p)
