#!/usr/bin/sage
import hashlib
import re

# with open("flag.txt", "rb") as f:
#     FLAG = f.read()
#     assert re.match(rb"Hero{[0-9a-zA-Z_]{90}}", FLAG)
FLAG = b"Hero{0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890}"
# FLAG = b"Hero{012312345678901234567890123456789012345678901234567890123456789012345678901234567890}"

F = FiniteField(2**256 - 189)
R = PolynomialRing(F, "x")
H = lambda n: int(hashlib.sha256(n).hexdigest(), 16)
C = lambda x: [H(x[i : i + 4]) for i in range(0, len(FLAG), 4)]

f = R(C(FLAG))

points = []
for _ in range(f.degree()):
    r = F.random_element()
    points.append([r, f(r)])

points.append([0, f(0)])

g = R.lagrange_polynomial(points)

print(f)
print(g)

assert f == g


# flag = input(">").encode().ljust(len(FLAG))

# g = R(C(flag))

# for p in points:
#     if g(p[0]) != p[1]:
#         print("Wrong flag!")
#         break
# else:
#     print("Congrats!")
