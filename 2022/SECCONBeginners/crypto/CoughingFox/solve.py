from math import isqrt
from params import cipher


flag = list("ctf4b{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}")

for c in cipher:
    for i in range(len(cipher)):
        if isqrt(c - i) ** 2 == c - i:
            flag[i] = chr(isqrt(c - i) - i)

print("".join(flag))
