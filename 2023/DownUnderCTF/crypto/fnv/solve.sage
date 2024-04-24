s = 0xCBF29CE484222325
m = 0xFFFFFFFFFFFFFFFF + 1
b = 0x00000100000001B3
t = TARGET = 0x1337133713371337
print([s * pow(b, i, m) % m for i in range(10)])
# s * pow(b, i, m) % m == TARGET

# t = TARGET
# g, u, v = xgcd(s, t)
# assert g == 1
# for k in range(100):
#     x = -t * k + u
#     y = -(s * k + v)
#     print(x, y)
#     assert s * x - t * y == 1
#     if gcd(y, m) == 1:
#         assert (s * x * pow(y, -1, m) - pow(y, -1, m)) % m == t % m
#         print("OK")

"""
'01' + '00' * i を送った時の
"""

mx = 100
S = [pow(b, i, m) for i in range(1, mx + 2)]
M = []
M.append([1, 0, 0, S[0]])
M.append([0, 1, 0, S[1]])
M.append([0, 0, 1, S[2]])
M.append([0, 0, 0, t])
print(M)
M = matrix(Zmod(m), M)
print(M.LLL())
# print(S[mx])
# for a in range(256):
#     for b in range(256):
#         for d0 in S:
#             for d1 in S:
#                 if (S[mx] + a * d0 + b * d1) % m == t:
#                     print(a, b, d0, d1)


# for k in range(10000):
#     x = -t * k + u
#     y = -(s * k + v)
#     print(x % m)
#     if (x % m) in S:
#         print("YES")

# for x in range(256):
#     t = s ^^ x
#     if gcd(t, m) != 1:
#         continue
#     try:
#         ans = discrete_log(Zmod(m)(TARGET * pow(t, -1, m)), Zmod(m)(b))
#         print(ans)
#         assert t * pow(b, ans, m) % m == TARGET
#     except ValueError:
#         pass
