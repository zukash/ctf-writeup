from params import n1, n2, n3, e, c1, c2, c3
from Crypto.Util.number import *

A = [c1, c2, c3]
M = [n1, n2, n3]

x = crt(A, M)
flag = x ** (1 / e)

print(long_to_bytes(int(flag)))

# This is your destination: "https://pastes.io/1yjswxlvl2"
