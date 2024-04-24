from Crypto.Util.number import *

with open("output.txt") as f:
    RR = eval(f.readline().replace("R = ", ""))
    S = eval(f.readline().replace("S = ", ""))

A = matrix(Zmod(3), RR)
b = vector(Zmod(3), S)
x = A.solve_right(b)

flag = int("".join(map(str, x)), 3)
flag = long_to_bytes(flag)
print(flag)
