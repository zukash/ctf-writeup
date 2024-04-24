# めっちゃわかりやすい解説
# https://discord.com/channels/721605871414542377/886184185864273930/1148103292283523152

import itertools
from Crypto.Util.number import long_to_bytes

# n, c, hints
exec(open("output.txt", "r").read())

h1, h2, h3 = hints
mat = matrix(
    ZZ, [[h1 << 10000, 1, 0, 0], [h2 << 10000, 0, 1, 0], [h3 << 10000, 0, 0, 1]]
).LLL()
s1, s2, s3 = mat[0][1:]
mat = matrix(
    ZZ, [[s1 << 10000, 1, 0, 0], [s2 << 10000, 0, 1, 0], [s3 << 10000, 0, 0, 1]]
).LLL()
a1, a2, a3 = mat[0][1:]
p = gcd(n, a2 * h1 - a1 * h2)
q = n // p
e = 0x10001
phi = (p - 1) * (q - 1)
d = int(pow(e, -1, phi))
pt = pow(c, d, n)
print(int(pt).to_bytes(2048 // 8, "big").replace(b"\0", b"").decode())

#########################################################

V = hints
k = 2 ^ 800
M = Matrix.column([k * v for v in V]).augment(Matrix.identity(len(V)))
print(M)
B = [b[1:] for b in M.LLL()]
M = (k * Matrix(B[: len(V) - 2])).T.augment(Matrix.identity(len(V)))
B = [b[-len(V) :] for b in M.LLL() if set(b[: len(V) - 2]) == {0}]

for s, t in itertools.product(range(4), repeat=2):
    T = s * B[0] + t * B[1]
    a1, a2, a3 = T
    kq = gcd(a1 * hints[1] - a2 * hints[0], n)
    if 1 < kq < n:
        print("find!", kq, s, t)
        break
for i in range(2 ** 16, 1, -1):
    if kq % i == 0:
        kq //= i
q = int(kq)
p = int(n // kq)
d = pow(0x10001, -1, (p - 1) * (q - 1))
m = pow(c, d, n)
flag = long_to_bytes(m).decode()
print(flag)
