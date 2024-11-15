

# This file was *autogenerated* from the file /Users/zukash/ghq/github.com/zukash/ctf-problems/DownUnderCTF_2023/crypto/fnv/solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_0xCBF29CE484222325 = Integer(0xCBF29CE484222325); _sage_const_0xFFFFFFFFFFFFFFFF = Integer(0xFFFFFFFFFFFFFFFF); _sage_const_1 = Integer(1); _sage_const_0x00000100000001B3 = Integer(0x00000100000001B3); _sage_const_0x1337133713371337 = Integer(0x1337133713371337); _sage_const_10 = Integer(10); _sage_const_100 = Integer(100); _sage_const_2 = Integer(2); _sage_const_0 = Integer(0)
s = _sage_const_0xCBF29CE484222325 
m = _sage_const_0xFFFFFFFFFFFFFFFF  + _sage_const_1 
b = _sage_const_0x00000100000001B3 
t = TARGET = _sage_const_0x1337133713371337 
print([s * pow(b, i, m) % m for i in range(_sage_const_10 )])
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

mx = _sage_const_100 
S = [pow(b, i, m) for i in range(_sage_const_1 , mx + _sage_const_2 )]
M = []
M.append([_sage_const_1 , _sage_const_0 , _sage_const_0 , S[_sage_const_0 ]])
M.append([_sage_const_0 , _sage_const_1 , _sage_const_0 , S[_sage_const_1 ]])
M.append([_sage_const_0 , _sage_const_0 , _sage_const_1 , S[_sage_const_2 ]])
M.append([_sage_const_0 , _sage_const_0 , _sage_const_0 , t])
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

